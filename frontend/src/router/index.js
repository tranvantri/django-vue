import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import BookDetail from '../views/BookDetail'
import SearchPage from '../views/SearchPage'
import Login from '../views/Login'
import Signup from '../views/Signup'
import Cart from '../views/Cart'
import SuccessPayment from '../views/SuccessPayment'
// import store from '../store'

Vue.use(Router)

const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/book/:id',
            name: 'book-detail',
            component: BookDetail
        },
        {
            path: '/search',
            name: 'search',
            component: SearchPage
        },
        {
            path: '/login',
            name: 'login',
            meta: {layout: 'blank'},
            component: Login
        },
        {
            path: '/signup',
            name: 'signup',
            meta: {layout: 'blank'},
            component: Signup
        },
        {
            path: '/cart',
            name: 'cart',
            meta: {requiredLogin: true},
            component: Cart
        },
        {
            path: '/success',
            name: 'success',
            meta: {requiredLogin: true},
            component: SuccessPayment
        }
    ]
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiredLogin) && !localStorage.getItem('token')) {
        next({name: 'login', query: {to: to.path}})
    } else if (to.matched.some(record => record.name === 'login') && localStorage.getItem('token')) {
        next({name: 'home'})
    } else {
        next()
    }
})

export default router
