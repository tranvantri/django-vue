import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import BookDetail from '../views/BookDetail'

Vue.use(Router)

export default new Router({
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
        }
    ]
})
