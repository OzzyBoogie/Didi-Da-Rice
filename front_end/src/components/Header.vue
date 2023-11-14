<template>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" :ellipsis="false" @select="handleSelect">
        <el-switch v-model="value1" size="large" class="ml-2 vertical-center" inline-prompt
            style="--el-switch-on-color: #13ce66; --el-switch-off-color: #409EFF; margin-left: 5px;" active-text="接单" inactive-text="下单" />
        <div class="center">
            <span>滴滴打饭</span>
        </div>
        <div class="flex-grow" />
        <div class="vertical-center">
            <el-avatar :icon="UserFilled" />
        </div>
    </el-menu>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue'
import { UserFilled } from '@element-plus/icons-vue'

const activeIndex = ref('1')
const handleSelect = (key: string, keyPath: string[]) => {
    console.log(key, keyPath)
}
const value1 = ref()

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
</style>
  