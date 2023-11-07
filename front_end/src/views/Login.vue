<template>
  <div id="login">
    <div id="account" class="input_div">
      <input class="inputs" v-model="account" @keydown.enter="login" placeholder="Please input" size="large" />
    </div>
    <div id="password" class="input_div">
      <input class="inputs" v-model="password" @keydown.enter="login" placeholder="Please input" size="large" />
    </div>
    <div class="input_div" style="padding-top: 40px" @click="login">
      <button id="button">
        登录
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { ElMessage } from "element-plus";

const account = ref('admin')
const password = ref('123456')

const login = () => {
  console.log(account)
  if (account.value == '' || password.value == '') {
    msg_error("请输入账号和密码")
  } else if (account.value == 'admin' && password.value == '123456') {

    location.replace("https://ys.mihoyo.com/");
  } else {
    msg_error("账号或密码错误！")
  }

}
const msg_error = (msg) => {
  ElMessage.error(msg)
}
</script>

<style scoped>
#login {
  width: 75vw;
  height: 35vh;
  min-height: 300px;
  border-radius: 15px;
  background-color: rgb(39, 42, 55);
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  padding-top: 80px;
}


.inputs {
  width: 60%;
  height: 50px;
  background-color: rgb(66, 70, 86);
  border-radius: 10px;
  border: 2px solid rgb(34, 135, 225);
  padding: 10px;
  box-sizing: border-box;
  transition: 0.2s;
  font-size: 20px;
  color: #fff;
  font-weight: 100;
  outline: none;
}

.input_div {
  margin-bottom: 20px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

#account::before {
  content: "账号：";
  font-size: 28px;
  color: #f2f2f2;
}

#password::before {
  content: "密码：";
  font-size: 28px;
  color: #f2f2f2;
}

#button {
  width: 100px;
  height: 50px;
  color: #f2f2f2;
  font-size: 20px;
  background: rgb(34, 135, 225);
  border: 0;
  border-radius: 20px;
}

#button:hover {
  cursor: pointer;
}
</style>