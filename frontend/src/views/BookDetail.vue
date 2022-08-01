<template>
    <div>
        <!-- Page Content  -->
        <div id="content-page" class="content-page">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-12">
                        <div class="iq-card iq-card-block iq-card-stretch iq-card-height">
                            <div class="iq-card-header d-flex justify-content-between align-items-center">
                                <h4 class="card-title mb-0">Books Description</h4>
                            </div>
                            <div class="iq-card-body pb-0">
                                <div class="description-contens align-items-top row">
                                    <div class="col-md-6">
                                        <div class="iq-card-transparent iq-card-block iq-card-stretch iq-card-height">
                                            <div class="iq-card-body p-0">
                                                <div class="row align-items-center">
                                                    <div class="col-3">
                                                        <!--                                                        <ul id="description-slider-nav"-->
                                                        <!--                                                            class="list-inline p-0 m-0 d-flex align-items-center">-->
                                                        <!--                                                            <li>-->
                                                        <!--                                                                <a href="javascript:void(0);">-->
                                                        <!--                                                                    <img :src="book.get_image"-->
                                                        <!--                                                                         :alt="book.name"-->
                                                        <!--                                                                         class="img-fluid rounded w-100">-->
                                                        <!--                                                                </a>-->
                                                        <!--                                                            </li>-->

                                                        <!--                                                        </ul>-->
                                                    </div>
                                                    <div class="col-9">
                                                        <ul class="list-inline p-0 m-0  d-flex align-items-center">
                                                            <li>
                                                                <a href="javascript:void(0);">
                                                                    <img :src="book.get_image"
                                                                         :alt="book.name"
                                                                         class="img-fluid w-100 rounded">
                                                                </a>
                                                            </li>
                                                        </ul>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="iq-card-transparent iq-card-block iq-card-stretch iq-card-height">
                                            <div class="iq-card-body p-0">
                                                <h3 class="mb-3">{{ book.name }}</h3>
                                                <div class="price d-flex align-items-center font-weight-500 mb-2">
                                                    <!--                                                    <span class="font-size-20 pr-2 old-price">$99</span>-->
                                                    <span class="font-size-24 text-dark">${{ book.price }}</span>
                                                </div>
                                                <div class="mb-3 d-block">
                                                </div>
                                                <span class="text-dark mb-4 pb-4 iq-border-bottom d-block">{{
                                                        book.description
                                                    }}</span>
                                                <div class="text-primary mb-4">Author: <span
                                                    class="text-body" v-if="book.author">{{ book.author.name }}</span>
                                                </div>
                                                <div class="mb-4 d-flex align-items-center">
                                                    <i @click="addToCartHandle" class="btn btn-primary view-more mr-2">Add To Cart</i>
                                                </div>
                                                <div class="mb-3">
                                                    <a href="#" class="text-body text-center"><span
                                                        class="avatar-30 rounded-circle bg-primary d-inline-block mr-2"><i
                                                        class="ri-heart-fill"></i></span><span>Add to Wishlist</span></a>
                                                </div>
                                                <div class="iq-social d-flex align-items-center">
                                                    <h5 class="mr-2">Share:</h5>
                                                    <ul class="list-inline d-flex p-0 mb-0 align-items-center">
                                                        <li>
                                                            <a href="#"
                                                               class="avatar-40 rounded-circle bg-primary mr-2 facebook"><i
                                                                class="fa fa-facebook" aria-hidden="true"></i></a>
                                                        </li>
                                                        <li>
                                                            <a href="#"
                                                               class="avatar-40 rounded-circle bg-primary mr-2 twitter"><i
                                                                class="fa fa-twitter" aria-hidden="true"></i></a>
                                                        </li>
                                                        <li>
                                                            <a href="#"
                                                               class="avatar-40 rounded-circle bg-primary mr-2 youtube"><i
                                                                class="fa fa-youtube-play" aria-hidden="true"></i></a>
                                                        </li>
                                                        <li>
                                                            <a href="#"
                                                               class="avatar-40 rounded-circle bg-primary pinterest"><i
                                                                class="fa fa-pinterest-p" aria-hidden="true"></i></a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-12">
                        <TrendyBookBlock/>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import TrendyBookBlock from '../components/TrendyBookBlock'
import axios from 'axios'
import {mapActions} from 'vuex'

export default {
    name: 'BookDetail',
    data() {
        return {
            book: {}
        }
    },
    components: {
        TrendyBookBlock
    },
    mounted() {
        this.getBook()
    },
    created() {
        this.setBreadcrumbs([
            {
                title: 'Home',
                url: {name: 'home'}
            },
            {title: 'Book Detail'}

        ])
    },
    methods: {
        ...mapActions(['setIsLoading', 'addToCart', 'setBreadcrumbs']),
        async getBook() {
            this.setIsLoading({isLoading: true})
            await axios.get(`/api/v1/book/${this.$route.params.id}`)
                .then(response => {
                    this.book = response.data
                    document.title = this.book.name + ' | Book Store'
                    this.setIsLoading({isLoading: false})
                })
                .catch(error => {
                    console.log(error)
                    this.setIsLoading({isLoading: false})
                })
        },
        addToCartHandle() {
            const item = {
                book: this.book,
                quantity: 1
            }

            this.addToCart(item)
             this.$toast.success('Add to cart successfully', {
                        type: 'success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right'
                    })
        }
    },
    watch: {
        $route(to, from) {
            this.getBook()
        }
    }
}
</script>

<style scoped>

</style>
