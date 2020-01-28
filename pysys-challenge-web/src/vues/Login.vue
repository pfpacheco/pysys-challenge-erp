<template>
  <div id="login">
    <LoginComponent></LoginComponent>
  </div>
</template>

<script>
import LoginComponent from '../components/LoginComponent'

export default {
  name: 'login',
  components: {
    LoginComponent
  },
  routes: ['/login']
}
</script>

<style>
  @import "../assets/css/demo.css";
  @import "../assets/css/style.css";
</style>
