<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <Header @changeMode="changeMode1">|</Header>
            </el-header>
            <el-main>
                <SendTask v-if="mode"></SendTask>
                <AcceptTask v-else></AcceptTask>
            </el-main>
        </el-container>
    </div>
</template>

<script setup>
import {onMounted, ref} from 'vue';
import Header from '../components/Header.vue';
import SendTask from '../components/SendTask.vue';
import AcceptTask from '../components/AcceptTask.vue'
import {getCookies} from "@/store/cookie";

const mode = ref(1)

function changeMode1() {
    mode.value = !mode.value
}

onMounted(() => {
    getCookies()
})
</script>
<style scoped>
.common-layout {
    font-family: source, serif;
}
</style>
