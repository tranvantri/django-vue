// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Default from './layouts/Default'
import Blank from './layouts/Blank'
import axios from 'axios'
import store from './store'
import VueToast from 'vue-toast-notification'
import 'vue-toast-notification/dist/theme-sugar.css'

Vue.use(VueToast)
Vue.component('default-layout', Default)
Vue.component('blank-layout', Blank)
Vue.config.productionTip = false

axios.defaults.baseURL = 'http://127.0.0.1:8000'

/* eslint-disable no-new */
new Vue({
    el: '#app',
    router,
    store,
    components: {App},
    template: '<App/>'
})
