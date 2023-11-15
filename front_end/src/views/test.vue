<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <Header>|</Header>
            </el-header>
            <el-main>
                <MainPost @create="create" @cancle="cancle"></MainPost>
            </el-main>
        </el-container>
    </div>
    <ConfirmDialog v-model="activeDialog" :form="form" @cancelDialog="cancelDialog"></ConfirmDialog>
</template>

<script setup>
import { ref } from 'vue';
import Header from '../components/Header.vue';
import MainPost from '../components/MainPost.vue';
import ConfirmDialog from '../components/ConfirmDialog.vue';

const activeDialog=ref(false)
const form=ref({})
function create(f){
    form.value=f
    activeDialog.value=true
}

function cancelDialog(){
    activeDialog.value=false
}
</script>
<style scoped></style>
