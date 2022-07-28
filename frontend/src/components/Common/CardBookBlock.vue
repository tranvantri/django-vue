<template>
    <div class="iq-card iq-card-block iq-card-stretch iq-card-height">
        <div v-if="isShowHeader"
            class="iq-card-header d-flex justify-content-between align-items-center position-relative">
            <div class="iq-header-title">
                <h4 class="card-title mb-0">{{ title }}</h4>
            </div>
            <div class="iq-card-header-toolbar d-flex align-items-center">
                <router-link v-if="viewMoreData.isShow" :to="viewMoreData.url" class="btn btn-sm btn-primary view-more">View
                    More</router-link>
            </div>
        </div>
        <div class="iq-card-body">
            <div class="row">
                <BookItem v-for="book in books" v-bind:key="book.id" :book="book"/>
            </div>
        </div>
    </div>
</template>

<script>
import BookItem from './BookItem'

export default {
    name: 'CardBookBlock',
    components: {
        BookItem
    },
    props: {
        'books': {type: Array, required: true},
        'title': {type: String},
        'viewMoreData': {type: Object},
        'isShowHeader': {type: Boolean, default: true}
    }
}
</script>

<style scoped>

</style>
