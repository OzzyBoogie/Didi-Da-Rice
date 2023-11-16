<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false">
        <el-switch v-model="showSwitch" @click="$emit('changeMode')" size="large" class="ml-2 vertical-center" inline-prompt
            style="--el-switch-on-color: #13ce66; --el-switch-off-color: #409EFF; margin-left: 5px;" active-text="接单"
            inactive-text="下单" />
        <div class="center">
            <span>滴滴打饭</span>
        </div>
        <div class="flex-grow" />
        <div class="vertical-center">
            <el-avatar class="avatar" src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                @click="showDrawer" />
        </div>
    </el-menu>
    <Drawer v-model="drawer"></Drawer>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue'
import Drawer from './Drawer.vue';
import { UserFilled } from '@element-plus/icons-vue'
import { store } from '../store/store'

defineEmits(["changeMode"])

const activeIndex = ref('1')
const showSwitch = ref()
const drawer = ref(false)

function showDrawer() {
    drawer.value = true
}
</script>
  
<style>
.flex-grow {
    flex-grow: 1;
}

.center {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.vertical-center {
    margin: auto 0 auto 0;
}

.example-showcase .el-dropdown-link {
    cursor: pointer;
    color: var(--el-color-primary);
    display: flex;
    align-items: center;
}

.avatar:hover {
    cursor: pointer;
}
</style>
  