import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from './vues/Login.vue'
import LoginComponent from './components/LoginComponent'
import RegistrationComponent from './components/RegistrationComponent'

Vue.config.productionTip = false

const routes = [
  {
    path: '/login',
    component: LoginComponent
  },
  {
    path: '/registration',
    component: RegistrationComponent
  }
]

const router = new VueRouter(
  routes
)

new Vue({
  router,
  render: h => h(Login)
}).$mount('#login')
