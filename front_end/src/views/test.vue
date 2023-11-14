<script setup>
import Header from '../components/Header.vue';
import MainPost from '../components/MainPost.vue';
</script>
<template>
    <div class="common-layout">
        <el-container>
            <el-header>
                <Header>|</Header>
            </el-header>
            <el-main>
                <MainPost></MainPost>
            </el-main>
        </el-container>
    </div>
</template>
  
<style scoped></style>
