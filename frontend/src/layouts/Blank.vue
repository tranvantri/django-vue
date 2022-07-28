<template>
    <div>
        <slot/>
        <div class="iq-colorbox color-fix">
             <Loading/>
        </div>
    </div>
</template>

<script>
import Loading from './Loading'
export default {
    name: 'Blank',
    components: {Loading}
}
</script>

<style scoped>

</style>
