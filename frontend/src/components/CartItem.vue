<template>
    <li class="checkout-product">
        <div class="row align-items-center">
            <div class="col-sm-2">
                                             <span class="checkout-product-img">
                                             <a href="javascript:void();"><img class="img-fluid rounded"
                                                                               :src="item.book.get_thumbnail"
                                                                               :alt="item.book.name"></a>
                                             </span>
            </div>
            <div class="col-sm-4">
                <div class="checkout-product-details">
                    <h5>{{ item.book.name }}</h5>
                    <div class="price">
                        <h5>{{ item.book.price }}</h5>
                    </div>
                </div>
            </div>
            <div class="col-sm-6">
                <div class="row">
                    <div class="col-sm-10">
                        <div class="row align-items-center mt-2">
                            <div class="col-sm-7 col-md-6">
                                <button @click="decrementQuantity(item)" type="button" class="fa fa-minus qty-btn"
                                        id="btn-minus"></button>
                                <input type="text" style="display: inline-block;
    width: 30px;
    height: 28px;
    border: 1px solid var(--iq-border);
    text-align: center;" :value="item.quantity">

                                <button @click="incrementQuantity(item)" type="button" class="fa fa-plus qty-btn"
                                        id="btn-plus"></button>
                            </div>
                            <div class="col-sm-5 col-md-6">
                                <span class="product-price">${{ ItemTotal }}</span>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-2">
                        <i @click="removeFromCart(item)" class="text-dark font-size-20"><i
                            class="ri-delete-bin-7-fill"></i></i>
                    </div>
                </div>
            </div>
        </div>
    </li>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        console.log(this.initialItem.quantity)
        return {
            item: this.initialItem
        }
    },
    computed: {
        ItemTotal() {
            return (parseInt(this.item.quantity) * parseFloat(this.item.book.price)).toFixed(2)
        },
        ...mapGetters(['cart'])
    },
    methods: {
        ...mapActions(['removeFromCart', 'incrementQuantity', 'decrementQuantity'])
    }
}
</script>

<style scoped>

</style>
