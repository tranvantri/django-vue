<template>
    <div class="col-sm-6 col-md-4 col-lg-3">
        <div class="iq-card iq-card-block iq-card-stretch iq-card-height browse-bookcontent">
            <div class="iq-card-body p-0">
                <div class="d-flex align-items-center">
                    <div class="col-6 p-0 position-relative image-overlap-shadow">
                        <a href="javascript:void();">
                            <img class="img-fluid rounded w-100"
                            :src="book.get_thumbnail"
                            :alt="book.name"></a>
                        <div class="view-book">
                            <router-link class="btn btn-sm btn-white"
                                         :to="{name:'book-detail', params:{id: book.id}}">
                                View Book
                            </router-link>
                        </div>
                    </div>
                    <div class="col-6">
                        <div class="mb-2">
                            <h6 class="mb-1">{{ book.name }}</h6>
                            <p class="font-size-13 line-height mb-1">{{ book.author.name }}</p>
                        </div>
                        <div class="price d-flex align-items-center">
                            <!--                            <span class="pr-1 old-price"></span>-->
                            <h6><b>${{ book.price }}</b></h6>
                        </div>
                        <div class="iq-product-action">
                            <a href="javascript:void();"><i
                                class="ri-shopping-cart-2-fill text-primary"></i></a>
                            <a href="javascript:void();" class="ml-2"><i
                                class="ri-heart-fill text-danger"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'BookItem',
    props: ['book']
}
</script>

<style scoped>

</style>
