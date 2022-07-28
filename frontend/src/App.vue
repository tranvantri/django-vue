<template>
    <div id="app">
        <Component :is='layout'>
            <router-view/>
        </Component>
    </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import axios from 'axios'

const defaultLayout = 'default'

export default {
    name: 'App',
    computed: {
        layout() {
            return (this.$route.meta.layout || defaultLayout) + '-layout'
        },
        ...mapGetters(['token', 'isAuthentication'])
    },
    methods: {
        ...mapActions(['initCartAction'])
    },
    created() {
        this.initCartAction()

        if (this.token) {
            axios.defaults.headers.common['Authorization'] = 'Token ' + this.token
        } else {
            axios.defaults.headers.common['Authorization'] = ''
        }
    }
}
</script>
