<template>
  <div id="container">
    <el-form :model="form" label-width="120px">
      <el-form-item label="校区">
        <el-select v-model="form.area" placeholder="选择校区">
          <el-option label="校本部" value="C" />
          <el-option label="北一区" value="N1" />
          <el-option label="北二区" value="N2" />
          <el-option label="东一区" value="E1" />
          <el-option label="东二区" value="E2" />
          <el-option label="良乡校区" value="L" />
        </el-select>
      </el-form-item>
      <el-form-item label="取餐地点">
        <el-input v-model="form.fromAddress" placeholder='例："食堂一层", "外卖柜+手机尾号"' />
      </el-form-item>
      <el-form-item label="目标地点">
        <el-input v-model="form.toAddress" placeholder='例："甲A888"' />
      </el-form-item>
      <el-form-item label="已送达">
        <el-switch v-model="form.delivery" />
      </el-form-item>
      <el-form-item label="送达时间" v-if="!form.delivery">
        <el-col :span="6">
          <el-date-picker v-model="form.date1" type="date" placeholder="Pick a date" style="width: 100%" />
        </el-col>
        <el-col :span="1" class="text-center">
        </el-col>
        <el-col :span="6">
          <el-time-picker v-model="form.date2" placeholder="Pick a time" style="width: 100%" />
        </el-col>
      </el-form-item>
      <el-form-item label="送达时间" v-else>
        <el-col :span="6">
          <el-date-picker v-model="form.date1" type="date" placeholder="Pick a date" style="width: 100%" disabled />
        </el-col>
        <el-col :span="1" class="text-center">
        </el-col>
        <el-col :span="6">
          <el-time-picker v-model="form.date2" placeholder="Pick a time" style="width: 100%" disabled />
        </el-col>
      </el-form-item>
      <el-form-item label="*备注">
        <el-input v-model="form.desc" type="textarea" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">Create</el-button>
        <el-button>Cancel</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'

// do not use same name with ref
const form = reactive({
  area: '',
  fromAddress: '',
  toAddress: '',
  date1: '',
  date2: '',
  delivery: false,
  desc: '',
})

const visible ='1'

const onSubmit = () => {

  console.log('submit!')
  console.log(form)
}
</script>

<style>
#container {
  width: 700px;
  height: 50%;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>