<template>
    <CardBookBlock :viewMoreData="viewMoreData" v-if="trendyBooks.length" :books="trendyBooks" :title="'Trendy Books'"></CardBookBlock>
</template>

<script>
import CardBookBlock from './Common/CardBookBlock'
import axios from 'axios'

export default {
    name: 'TrendyBookBlock',
    components: {CardBookBlock},
    data() {
        return {
            trendyBooks: [],
            viewMoreData: {
                'isShow': false,
                'url': ''
            }
        }
    },
    mounted() {
        this.getTrendyBooks()
    },
    methods: {
        getTrendyBooks() {
            axios.get('/api/v1/books/', {
                params: {
                    limit: 4,
                    is_trendy: 1
                }
            }).then(response => {
                this.trendyBooks = response.data.results
            }).catch(error => {
                console.log(error)
            })
        }
    }
}
</script>

<style scoped>

</style>
