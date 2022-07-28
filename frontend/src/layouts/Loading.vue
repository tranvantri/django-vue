<template>
   <div v-if="isLoading" class="buy-button"><a class="color-full" ><i class="fa fa-spinner fa-spin"></i></a></div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
    name: 'Loading',
     computed: {
        ...mapGetters(['isLoading'])
    }
}
</script>

<style scoped>

</style>
