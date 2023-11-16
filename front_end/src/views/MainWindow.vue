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
import { ref } from 'vue';
import Header from '../components/Header.vue';
import SendTask from '../components/SendTask.vue';
import AcceptTask from '../components/AcceptTask.vue'

const mode=ref(1)

function changeMode1(){
    mode.value=!mode.value
}
</script>
<style scoped></style>
