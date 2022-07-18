<template>
    <CardBookBlock :viewMoreData="viewMoreData" v-if="favoriteBooks.length" :books="favoriteBooks" :title="'Trendy Books'"></CardBookBlock>
</template>

<script>
import CardBookBlock from './Common/CardBookBlock'
import axios from 'axios'

export default {
    name: 'FavoriteBookBlock',
    components: {CardBookBlock},
    data() {
        return {
            favoriteBooks: [],
            viewMoreData: {
                'isShow': false,
                'url': ''
            }
        }
    },
    mounted() {
        this.getFavoriteBooks()
    },
    methods: {
        getFavoriteBooks() {
            axios.get('/api/v1/books/', {
                params: {
                    limit: 4,
                    is_favorite: 1
                }
            }).then(response => {
                this.favoriteBooks = response.data.results
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>

</style>
