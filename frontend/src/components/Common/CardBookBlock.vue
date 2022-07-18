<template>
    <div class="iq-card iq-card-block iq-card-stretch iq-card-height">
        <div
            class="iq-card-header d-flex justify-content-between align-items-center position-relative">
            <div class="iq-header-title">
                <h4 class="card-title mb-0">{{ title }}</h4>
            </div>
            <div class="iq-card-header-toolbar d-flex align-items-center">
                <a v-if="viewMoreData.isShow" href="category.html" class="btn btn-sm btn-primary view-more">View
                    More</a>
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
        'title': {type: String, required: true},
        'viewMoreData': {type: Object, required: true}
    }

}
</script>

<style scoped>

</style>
