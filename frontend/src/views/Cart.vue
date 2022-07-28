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
                                                    <label>Full Name: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.full_name" name="fname" required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Mobile Number: *</label>
                                                    <input type="number" class="form-control"
                                                           v-model="cart.userInfo.phone" name="mno" required="">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <div class="form-group">
                                                    <label>Address: *</label>
                                                    <input type="text" class="form-control"
                                                           v-model="cart.userInfo.address" name="address" required="">
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
                                    <h4 class="mb-2">{{cart.userInfo.full_name}}</h4>
                                    <div class="shipping-address">
                                        <p class="mb-0">{{cart.userInfo.address}}</p>
                                        <p>{{cart.userInfo.phone}}</p>
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
                            <div class="iq-card">
                                <div class="iq-card-header d-flex justify-content-between">
                                    <div class="iq-header-title">
                                        <h4 class="card-title">Payment Options</h4>
                                    </div>
                                </div>
                                <div class="iq-card-body">
                                    <div class="d-flex justify-content-between align-items-center">
                                        <div class="d-flex justify-content-between align-items-center">
                                            <img src="images/booking/cart.png" alt="" height="40" width="50">
                                            <span>US Unlocked Debit Card 12XX XXXX XXXX 0000</span>
                                        </div>
                                        <span>Nik John</span>
                                        <span>28/2020</span>
                                    </div>
                                    <form class="mt-3">
                                        <div class="d-flex align-items-center">
                                            <span>Enter CVV: </span>
                                            <div class="cvv-input ml-3 mr-3">
                                                <input type="text" class="form-control" required="">
                                            </div>
                                            <button type="submit" class="btn btn-primary">Continue</button>
                                        </div>
                                    </form>
                                    <hr>
                                    <div class="card-lists">
                                        <div class="form-group">
                                            <div class="custom-control custom-radio">
                                                <input type="radio" id="credit" name="customRadio"
                                                       class="custom-control-input">
                                                <label class="custom-control-label" for="credit"> Credit / Debit / ATM
                                                    Card</label>
                                            </div>
                                            <div class="custom-control custom-radio">
                                                <input type="radio" id="netbaking" name="customRadio"
                                                       class="custom-control-input">
                                                <label class="custom-control-label" for="netbaking"> Net Banking</label>
                                            </div>
                                            <div class="custom-control custom-radio">
                                                <input type="radio" id="emi" name="emi" class="custom-control-input">
                                                <label class="custom-control-label" for="emi"> EMI (Easy
                                                    Installment)</label>
                                            </div>
                                            <div class="custom-control custom-radio">
                                                <input type="radio" id="cod" name="cod" class="custom-control-input">
                                                <label class="custom-control-label" for="cod"> Cash On Delivery</label>
                                            </div>
                                        </div>
                                    </div>
                                    <hr>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4">
                            <div class="iq-card">
                                <div class="iq-card-body">
                                    <h4 class="mb-2">Price Details</h4>
                                    <div class="d-flex justify-content-between">
                                        <span>Price 3 Items</span>
                                        <span><strong>$1000.00</strong></span>
                                    </div>
                                    <div class="d-flex justify-content-between">
                                        <span>Delivery Charges</span>
                                        <span class="text-success">Free</span>
                                    </div>
                                    <hr>
                                    <div class="d-flex justify-content-between">
                                        <span>Amount Payable</span>
                                        <span><strong>$1000.00</strong></span>
                                    </div>
                                    <hr>
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

export default {
    name: 'Cart',
    components: {CartItem},
    computed: {
        ...mapGetters({
            cart: 'cart',
            cartTotalLength: 'cartTotalLength',
            cartTotalPrice: 'cartTotalPrice'
        }),
        checkRequired() {
            let userInfo = this.cart.userInfo

            return (userInfo.full_name === '' || userInfo.phone === '' || userInfo.address === '')
        }
    },
    methods: {
        ...mapActions(['updateStep', 'updateUserInfo'])
    }
}
</script>

<style scoped>

</style>
