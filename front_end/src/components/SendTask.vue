<template>
  <div id="container">
      <el-form ref="ruleFormRef" :model="ruleForm" :rules="rules" :size="'large'" class="demo-ruleForm"
               label-width="120px" status-icon>
          <el-form-item label="aa校区" prop="area">
              <el-select v-model="ruleForm.area" placeholder="选择校区">
                  <el-option label="校本部" value="校本部" />
                  <el-option label="北一区" value="北一区" />
                  <el-option label="北二区" value="北二区" />
                  <el-option label="东一区" value="东一区" />
                  <el-option label="东二区" value="东二区" />
                  <el-option label="良乡校区" value="良乡校区" />
              </el-select>
          </el-form-item>
          <el-form-item label="取餐地点" prop="fromAddress">
              <el-input v-model="ruleForm.fromAddress" placeholder='例："食堂一层", "外卖柜+手机尾号"' />
          </el-form-item>
          <el-form-item label="目标地点" prop="toAddress">
              <el-input v-model="ruleForm.toAddress" placeholder='例："甲A888"' />
          </el-form-item>
          <el-form-item label="已送达">
              <el-switch v-model="ruleForm.delivery" />
          </el-form-item>
          <el-form-item label="送达时间" v-if="!ruleForm.delivery" prop="date1">
              <el-col :span="8">
                  <el-date-picker v-model="ruleForm.date1" type="date" placeholder="选择日期" style="width: 100%"
                      value-format="YYYY-MM-DD" />
              </el-col>
              <el-col :span="1" class="text-center">
              </el-col>
              <el-col :span="8">
                  <el-time-select v-model="ruleForm.date2" start="00:00" step="00:15" end="23:30"
                      placeholder="选择时间" value-format="HH:MM" prop="date2" />
              </el-col>
          </el-form-item>
          <el-form-item label="送达时间" v-else>
              <el-col :span="8">
                  <el-date-picker v-model="ruleForm.date1" type="date" placeholder="选择日期" style="width: 100%"
                      value-format="YYYY-MM-DD" disabled />
              </el-col>
              <el-col :span="1" class="text-center">
              </el-col>
              <el-col :span="8">
                  <el-time-select v-model="ruleForm.date2" start="00:00" step="00:15" end="23:30"
                      placeholder="选择时间" disabled />
              </el-col>
          </el-form-item>
          <el-form-item label="备注">
              <el-input v-model="ruleForm.desc" type="textarea" />
          </el-form-item>
          <el-form-item>
              <el-button type="primary" @click="submitForm(ruleFormRef)">
                  Create
              </el-button>
              <el-button @click="resetForm(ruleFormRef)">Reset</el-button>
          </el-form-item>
      </el-form>
  </div>
  <ConfirmDialog v-model="showDialog" :form="form" @cancelDialog="cancelDialog"></ConfirmDialog>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance, FormRules } from 'element-plus'
import ConfirmDialog from './ConfirmDialog.vue';

interface RuleForm {
  area: string
  fromAddress: string
  toAddress: string
  date1: string
  date2: string
  delivery: boolean
  desc: string
}

const formSize = ref('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
  area: '',
  fromAddress: '',
  toAddress: '',
  date1: '',
  date2: '',
  delivery: false,
  desc: '',
})

const rules = reactive<FormRules<RuleForm>>({
  area: [
      {
          required: true,
          message: '',
          trigger: 'change'
      },
  ], fromAddress: [
      {
          required: true,
          message: '',
          trigger: 'change',
      },
  ],
  toAddress: [
      {
          required: true,
          message: '',
          trigger: 'change',
      },
  ],
  date1: [
      {
          required: true,
          message: '',
          trigger: 'change',
      },
  ],
  date2: [
      {
          required: true,
          message: '',
          trigger: 'change',
      },
  ],
})

const showDialog=ref(false)
const form=ref({})

function activeDialog(f){
  form.value=f
  showDialog.value=true
}

function cancelDialog(){
  showDialog.value=false
}

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
      if (valid) {
          activeDialog(ruleForm)
          console.log('submit!')
      } else {
          console.log('error submit!')
      }
  })
}

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}

</script>

<style scoped>
#container {
  width: 700px;
  height: 50%;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
</style>