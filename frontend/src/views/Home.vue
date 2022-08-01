<template>
    <div>
        <!-- Page Content  -->
        <div id="content-page" class="content-page">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-lg-12">
                        <div class="iq-card-transparent iq-card-block iq-card-stretch iq-card-height rounded">
                            <div class="newrealease-contens">
                                <ul id="newrealease-slider" class="list-inline p-0 m-0 d-flex align-items-center">
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/01.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/02.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/03.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/04.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/05.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/06.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/07.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/08.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                    <li class="item">
                                        <a href="javascript:void(0);">
                                            <img src="static/assets/images/new_releases/09.jpg"
                                                 class="img-fluid w-100 rounded"
                                                 alt="">
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-12">
                        <CardBookBlock :viewMoreData="viewMoreData" :books="latestBooks" :title="'Browse Books'"/>
                    </div>

                    <!-- Favorite Book -->
                    <div class="col-lg-12">
                        <!--                        <CardBookBlock :title="'Trendy Books'"/>-->
                    </div>
                    <!--  TrendyBook -->
                    <div class="col-lg-12">
                        <TrendyBookBlock/>
                    </div>

                </div>
            </div>
        </div>

    </div>
</template>

<script>

import CardBookBlock from '@/components/Common/CardBookBlock'
import TrendyBookBlock from '@/components/TrendyBookBlock'
import axios from 'axios'
import {mapActions} from 'vuex'
// import {mapActions} from 'vuex'

export default {
    name: 'Home',
    components: {
        CardBookBlock,
        TrendyBookBlock
    },
    data() {
        return {
            latestBooks: [],
            viewMoreData: {
                isShow: true,
                url: {name: 'search'}
            }
        }
    },
    beforeCreate() {
        document.title = 'Home | Book Store'
    },
    mounted() {
        this.getLatestBooks()
        // this.setHeaderTitle('Home')
    },
    created() {
        this.setBreadcrumbs([])
    },
    methods: {
        ...mapActions(['setIsLoading', 'setBreadcrumbs']),
        async getLatestBooks() {
            this.setIsLoading({isLoading: true})
            await axios.get('/api/v1/books/', {
                params: {
                    limit: 8
                }
            }).then(response => {
                this.latestBooks = response.data.results
                this.setIsLoading({isLoading: false})
            }).catch(error => {
                console.log(error)
                this.setIsLoading({isLoading: false})
            })
        }
    }
}
</script>

<style scoped>

</style>
