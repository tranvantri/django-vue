<template>
    <!-- Page Content  -->
    <div id="content-page" class="content-page">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="iq-card-transparent mb-0">
                        <div class="d-block text-center">
                            <h2 class="mb-3">Search by Book Name</h2>
                            <div class="w-100 iq-search-filter">
                                <ul class="list-inline p-0 m-0 row justify-content-center search-menu-options">
                                    <li class="search-menu-opt">
                                        <div class="iq-dropdown">
                                            <div class="form-group mb-0">
                                                <select v-model="category_id"
                                                        class="form-control form-search-control bg-white border-0"
                                                        id="exampleFormControlSelect2">
                                                    <option :value="0">Category</option>
                                                    <option v-for="category in categories" :value="category.id"
                                                            :key="category.id">
                                                        {{ category.name }}
                                                    </option>
                                                </select>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="search-menu-opt">
                                        <div class="iq-dropdown">
                                            <div class="form-group mb-0">
                                                <select v-model="author_id"
                                                        class="form-control form-search-control bg-white border-0"
                                                        id="exampleFormControlSelect4">
                                                    <option :value="0">Author</option>
                                                    <option v-for="author in authors" :value="author.id"
                                                            :key="author.id">
                                                        {{ author.name }}
                                                    </option>
                                                </select>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="search-menu-opt">
                                        <div class="iq-search-bar search-book d-flex align-items-center">
                                            <form @submit.prevent="onSubmitSearch" id="searchFrom" class="searchbox">
                                                <input type="text" class="text search-input" v-model="q"
                                                       placeholder="search here...">
                                                <a class="search-link" href="#"><i class="ri-search-line"></i></a>
                                            </form>
                                            <button type="submit" form="searchFrom"
                                                    class="btn btn-primary search-data ml-2">Search
                                            </button>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-12">
                    <CardBookBlock v-if="books.length > 0" :books="books" :is-show-header="false"/>
                    <p v-else class="text-center">No book found.</p>
                </div>

                <div class="col-lg-12" style="text-align: center;height: 74px;">
                    <button v-if="isShowMore" @click="handleShowMore" style="position: absolute;"
                            class="btn btn-primary show-more ml-2">Show
                        More
                    </button>
                </div>

                <div class="col-lg-12">
                    <TrendyBookBlock/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TrendyBookBlock from '../components/TrendyBookBlock'
import CardBookBlock from '../components/Common/CardBookBlock'
import axios from 'axios'
import {mapActions} from 'vuex'

export default {
    name: 'SearchPage',
    components: {
        CardBookBlock,
        TrendyBookBlock
    },
    data() {
        return {
            books: [],
            categories: [],
            authors: [],
            q: this.$route.query.q ? this.$route.query.q : '',
            author_id: this.$route.query.author_id ? this.$route.query.author_id : 0,
            category_id: this.$route.query.category_id ? this.$route.query.category_id : 0,
            isShowMore: false,
            page: 1
        }
    },
    created() {
        document.title = (this.$route.query.q ? this.$route.query.q + ' | ' : '') + 'Book Store'
        this.getAuthors()
        this.getCategories()
        this.getBooks()
    },
    methods: {
        ...mapActions(['setIsLoading']),
        resetPage() {
            this.page = 1
        },
        onSubmitSearch() {
            this.resetPage()
            const query = {q: this.q}
            if (this.category_id > 0) {
                query.category_id = this.category_id
            }

            if (this.author_id > 0) {
                query.author_id = this.author_id
            }

            this.$router.push({name: this.$route.name, query})
            this.books = []
            this.getBooks()
        },
        getCategories() {
            axios.get('/api/v1/categories/')
                .then(response => {
                    this.categories = response.data
                }).catch(error => {
                console.log(error)
            })
        },
        getAuthors() {
            axios.get('/api/v1/authors/')
                .then(response => {
                    this.authors = response.data
                }).catch(error => {
                console.log(error)
            })
        },
        async getBooks() {
            this.setIsLoading({isLoading: true})
            const params = {
                limit: 8,
                page: this.page
            }

            if (this.q) {
                params.q = this.q
            }

            if (this.author_id > 0) {
                params.author_id = this.author_id
            }

            if (this.category_id > 0) {
                params.category_id = this.category_id
            }

            await axios.get('/api/v1/books/', {
                params
            }).then(response => {
                this.books.push(...response.data.results)
                this.setIsLoading({isLoading: false})
                this.isShowMore = response.data.next !== null
            }).catch(error => {
                console.log(error)
                this.setIsLoading({isLoading: false})
                this.page = 1
            })
        },
        handleShowMore() {
            this.page += 1
            this.getBooks()
        }
    }
}
</script>

<style scoped>

</style>
