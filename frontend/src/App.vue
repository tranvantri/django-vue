<template>
    <div id="app">
        <Component :is='layout'>
            <router-view :key="$route.fullPath"/>
        </Component>
    </div>
</template>

<script>
const defaultLayout = 'default'

export default {
    name: 'App',
    computed: {
        layout() {
            return (this.$route.meta.layout || defaultLayout) + '-layout'
        }
    }
}
</script>
