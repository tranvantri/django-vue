<template>
    <!-- Page Content  -->
    <div id="content-page" class="content-page">
        <div class="container-fluid checkout-content">
            <div class="row">
                <div v-show="cart.step === 0" id="cart" class="card-block show p-0 col-12">
                    <div class="row align-item-center">
                        <div class="col-lg-8">
                            <div class="iq-card">
                                <div class="iq-card-header d-flex justify-content-between iq-border-bottom mb-0">
                                    <div class="iq-header-title">
                                        <h4 class="card-title">Shopping Cart</h4>
                                    </div>
                                </div>
                                <div class="iq-card-body">
                                    <ul v-if="cartTotalLength" class="list-inline p-0 m-0">
                                        <CartItem v-for="item in cart.items"
                                                  v-bind:key="item.book.id"
                                                  v-bind:initialItem="item"/>
                                    </ul>

                                    <p v-else>You don't have any books in your cart</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="iq-card">
                                <div class="iq-card-body">
                                    <p><b>Price Details</b></p>
                                    <div class="d-flex justify-content-between mb-1">
                                        <span>Total MRP</span>
                                        <span>${{ cartTotalPrice }}</span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>Delivery Charges</span>
                                        <span class="text-success">Free</span>
                                    </div>
                                    <hr>
                                    <div class="d-flex justify-content-between">
                                        <span class="text-dark"><strong>Total</strong></span>
                                        <span class="text-dark"><strong>${{ cartTotalPrice }}</strong></span>
                                    </div>
                                    <span v-if="cartTotalLength" @click.prevent="updateStep(1)"
                                          class="btn btn-primary d-block mt-3 next">Place
                                        order</span>
                                </div>
                            </div>
                            <div class="iq-card ">
                                <div class="card-body iq-card-body p-0 iq-checkout-policy">
                                    <ul class="p-0 m-0">
                                        <li class="d-flex align-items-center">
                                            <div class="iq-checkout-icon">
                                                <i class="ri-checkbox-line"></i>
                                            </div>
                                            <h6>Security policy (Safe and Secure Payment.)</h6>
                                        </li>
                                        <li class="d-flex align-items-center">
                                            <div class="iq-checkout-icon">
                                                <i class="ri-truck-line"></i>
                                            </div>
                                            <h6>Delivery policy (Home Delivery.)</h6>
                                        </li>
                                        <li class="d-flex align-items-center">
                                            <div class="iq-checkout-icon">
                                                <i class="ri-arrow-go-back-line"></i>
                                            </div>
                                            <h6>Return policy (Easy Retyrn.)</h6>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-show="cart.step === 1" id="address" class="card-block show p-0 col-12">
                    <div class="row align-item-center">
                        <div class="col-lg-8">
                            <div class="iq-card">
                                <div class="iq-card-header d-flex justify-content-between">
                                    <div class="iq-header-title">
                                        <h4 class="card-title">Add New Address</h4>
                                    </div>
                                </div>
                                <div class="iq-card-body">
                                    <form>
                                        <div class="row mt-3">
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>First Name: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.first_name" name="first_name"
                                                           required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Last Name: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.last_name" name="last_name"
                                                           required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Mobile Number: *</label>
                                                    <input type="number" class="form-control"
                                                           v-model="cart.userInfo.phone" name="phone" required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Email: *</label>
                                                    <input type="email" class="form-control"
                                                           v-model="cart.userInfo.email" name="email" required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Address: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.address" name="address" required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Place: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.place" name="place" required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Zip code: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.zipcode" name="zipcode" required="">
                                                </div>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="iq-card">
                                <div class="iq-card-body">
                                    <h4 class="mb-2">{{ fullName }}</h4>
                                    <div class="shipping-address">
                                        <p class="mb-0">{{ cart.userInfo.address }}</p>
                                        <p>{{ cart.userInfo.phone }}</p>
                                    </div>
                                    <hr>
                                    <span v-if="!checkRequired" @click.prevent="updateStep(2)"
                                          class="btn btn-primary d-block mt-1 next">Deliver To
                                        this Address</span>

                                    <span v-show="cart.step===1" @click.prevent="updateStep(0)"
                                          class="btn btn-outline-info d-block mt-1 next">Back</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div v-show="cart.step === 2" id="payment" class="card-block show p-0 col-12">
                    <div class="row align-item-center">
                        <div class="col-lg-8">
                            <stripe-element-card
                                ref="elementRef"
                                :pk="publishableKey"
                                @token="stripeTokenHandler"
                            />
                        </div>

                        <div class="col-lg-4">
                            <div class="iq-card">
                                <div class="iq-card-body">
                                    <h4 class="mb-2">Price Details</h4>
                                    <div class="d-flex justify-content-between">
                                        <span>Price {{ cartTotalLength }} Items</span>
                                        <span><strong>${{ cartTotalPrice }}</strong></span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>Delivery Charges</span>
                                        <span class="text-success">Free</span>
                                    </div>
                                    <hr>
                                    <div class="d-flex justify-content-between">
                                        <span>Amount Payable</span>
                                        <span><strong>${{ cartTotalPrice }}</strong></span>
                                    </div>
                                    <hr>
                                    <span v-show="cart.step===2"
                                          class="btn btn-primary d-block mt-1 next" @click="submitGenerateToken">Payment With Stripe</span>
                                    <span v-show="cart.step===2" @click.prevent="updateStep(1)"
                                          class="btn btn-outline-info d-block mt-1 next">Back</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CartItem from '../components/CartItem'
import {mapActions, mapGetters} from 'vuex'
import axios from 'axios'
import {StripeElementCard} from '@vue-stripe/vue-stripe'

export default {
    name: 'Cart',
    components: {CartItem, StripeElementCard},
    data() {
        return {
            errors: [],
            publishableKey: 'pk_test_51J7HG4DxrR0RpsJ3fcCXfgkEgVywgyojzhwRDrdb7GxWoPuBXiU4BTdicaFMWTdj9vz7KSlbKkic65LDuOeXmKXk00XRVutLWr'
        }
    },
    created() {
        document.title = 'CheckOut | BookStore'
        this.setBreadcrumbs([
            {
                title: 'Home',
                url: {name: 'home'}
            },
            {title: 'Cart'}
        ])
    },
    computed: {
        ...mapGetters({
            cart: 'cart',
            cartTotalLength: 'cartTotalLength',
            cartTotalPrice: 'cartTotalPrice'
        }),
        checkRequired() {
            let userInfo = this.cart.userInfo

            return (userInfo.full_name === '' || userInfo.phone === '' || userInfo.address === '' || userInfo.zipcode === '')
        },
        fullName() {
            return `${this.cart.userInfo.first_name} ${this.cart.userInfo.last_name}`
        }
    },
    methods: {
        ...mapActions(['updateStep', 'updateUserInfo', 'setBreadcrumbs', 'setIsLoading', 'clearCart']),
        submitGenerateToken() {
            this.setIsLoading({isLoading: true})
            this.$refs.elementRef.submit()
        },
        async stripeTokenHandler(token) {
            const items = []

            for (let i = 0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    book: item.book.id,
                    quantity: item.quantity,
                    price: item.book.price * item.quantity
                }

                items.push(obj)
            }

            const userInfo = this.cart.userInfo

            const data = {
                'first_name': userInfo.first_name,
                'last_name': userInfo.last_name,
                'email': userInfo.email,
                'address': userInfo.address,
                'zipcode': userInfo.zipcode,
                'place': userInfo.place,
                'phone': userInfo.phone,
                'book_items': items,
                'stripe_token': token.id
            }

            await axios.post('/api/v1/checkout/', data)
                .then(() => {
                    this.clearCart()
                    this.$router.push({name: 'success'})
                }).catch(error => {
                    this.errors.push('Something went wrong. Please try again')
                    console.log(error)
                })

            this.setIsLoading({isLoading: false})
        }
    }
}
</script>

<style scoped>

</style>
