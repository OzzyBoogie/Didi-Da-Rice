<template>
    <el-drawer style="border-radius: 15px 0 0 15px;" :show-close="false" :with-header="false">
        <div>
            <el-avatar class="avatar" :size="150" :src="info.avatar" />
            <h3 class="username">{{ info.name }}</h3>
        </div>
        <el-descriptions class="body" :column="1" direction="vertical">
            <el-descriptions-item label="电话号码" align="center">{{ info.phone }}</el-descriptions-item>
            <el-descriptions-item label="其他" align="center">~</el-descriptions-item>
        </el-descriptions>
        <template #footer>
            <div style="flex: auto">
                <el-button class="btn" type="info" @click="">
                    <el-icon :size="20"><Edit /></el-icon>
                </el-button>
            </div>
        </template>
    </el-drawer>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue'
import { store } from '../store/store'
import { Edit } from '@element-plus/icons-vue';

const info = ref(store)
</script>
  
<style scoped>
.avatar {
    margin: auto;
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;

}

.avatar:hover {
    cursor: auto;
}

.username {
    margin: 20px 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.body {
    margin-top: 50px;
}

.btn{
    width: 50px;
    height: 50px;
}
.ico{
    width: 50px;
    height: 50px;
}
</style>