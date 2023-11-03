<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import Login from './views/Login.vue'
</script>

<template>
  <div id="app">
    <RouterView></RouterView>
  </div>
</template>

<style scoped>
#app {
  padding: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgb(151,157,167);
}
</style>
