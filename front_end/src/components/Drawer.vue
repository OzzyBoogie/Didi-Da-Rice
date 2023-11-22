<template>
    <el-drawer :show-close="false"
               :size="350" :with-header="false"
               style="border-radius: 15px 0 0 15px;">
        <div>
            <el-upload :before-upload="beforeUploadAvatar"
                       action=''
                       class="title"
            >
                <el-tooltip
                    class="box-item"
                    effect="dark"
                    content="修改头像"
                    placement="top"
                >
                    <el-avatar class="avatar" :size="200" :src="info.avatar"/>
                </el-tooltip>
            </el-upload>
            <h3 class="title">{{ info.username }}</h3>
        </div>
        <el-descriptions class="body-outer" :column="1" direction="vertical">
            <el-descriptions-item label="电话号码" align="center">{{ info.phone }}</el-descriptions-item>
            <el-descriptions-item label="其他" align="center">~</el-descriptions-item>
        </el-descriptions>
        <template #footer>
            <div style="flex: auto">
                <el-button class="btn" type="info" @click="showInnerDrawer">
                    <el-icon :size="20">
                        <Edit/>
                    </el-icon>
                </el-button>
            </div>
        </template>
        <el-drawer v-model="innerDrawer"
                   :append-to-body="true"
                   :show-close="false"
                   :size="300"
                   :with-header="false"
                   style="border-radius: 15px 0 0 15px;"
                   title="I'm inner Drawer"
        >
            <div>
                <p class="title-inner">修改信息</p>
            </div>
            <div class="body-inner" style="width: 200px">
                <el-descriptions class="body" :column="1" direction="vertical">
                    <el-descriptions-item label="昵称" align="left">
                        <el-input v-model="input_name" @input='isSubmitDisabled'/>
                    </el-descriptions-item>
                    <el-descriptions-item label="电话号码" align="left">
                        <el-input v-model="input_phone" @input='isSubmitDisabled'/>
                    </el-descriptions-item>
                </el-descriptions>
            </div>
            <template #footer>
                <div style="flex: auto">
                    <el-button v-if="submit_disabled" type="primary" disabled>Submit</el-button>
                    <el-button v-else type="primary" :loading="loading" @click="submitInfo">{{
                            loading ? 'Submitting ...' : 'Submit'
                        }}
                    </el-button>
                    <el-button @click="cancelForm">Cancel</el-button>
                </div>
            </template>
        </el-drawer>
    </el-drawer>
</template>

<script lang="ts" setup>
import {ref} from 'vue'
import {store} from '@/store/store'
import {Edit} from '@element-plus/icons-vue';
import axios from "axios";
import {url} from '@/settings';
import {showMessage} from '@/components/js/ShowMessage'

const info = ref(store)

const loading = ref(false)
const innerDrawer = ref(false)
const input_name = ref(store.username)
const input_phone = ref(store.phone)
const submit_disabled = ref(true)
function showInnerDrawer() {
    innerDrawer.value = true
}

function isInfoChanged() {
    return (input_name.value != store.username || input_phone.value != store.phone);   // 信息被修改则返回true
}

function isSubmitDisabled() {
    submit_disabled.value = !isInfoChanged();
}

function submitInfo() {
    loading.value = true
    const data = new FormData()
    data.append('account', store.account)
    data.append('name', input_name.value)
    data.append('phone', input_phone.value)
    axios.post(url + '/update_info', data).then(function (response) {
        if (response.data['code'] == 200) {
            store.username = input_name.value
            store.phone = input_phone.value
            showMessage('修改成功！', 'success')
            loading.value = false
            innerDrawer.value = false
        } else {
            showMessage("修改失败！", "error")
            loading.value = false
        }
    })
}

function cancelForm() {
    innerDrawer.value = false
}

function beforeUploadAvatar() {
    axios.post(url + '/update_info').then(function (response) {
        if (response.data['code'] == 400) {
            showMessage('修改失败! (失败原因：淫秽色情)', 'error')
        }
    })
    return false
}
</script>

<style scoped>
.avatar {
    width: 120px;
    height: 120px;
    margin: 30px auto auto;
    display: flex;
    justify-content: center;
    align-items: center;
}

.title {
    margin: 20px 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.title-inner {
    margin: 50px 0 30px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
}

.body-outer {
    margin-top: 50px;
}

.body-inner {
    margin: 0 auto;
}

.btn {
    width: 50px;
    height: 50px;
}
</style>