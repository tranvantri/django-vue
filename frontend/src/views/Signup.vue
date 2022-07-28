<template>
    <!-- Sign in Start -->
    <section class="sign-in-page">
        <div class="container p-0">
            <div class="row no-gutters height-self-center">
                <div class="col-sm-12 align-self-center page-content rounded">
                    <div class="row m-0">
                        <div v-if="errors.length" style="margin: 0 auto;width: 48%;">
                            <p class="alert alert-danger" v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </div>
                    <div class="row m-0">
                        <div class="col-sm-12 sign-in-page-data">
                            <div class="sign-in-from bg-primary rounded">
                                <h3 class="mb-0 text-center text-white">Sign Up</h3>
                                <p class="text-center text-white">Enter your email address and password to access admin
                                    panel.</p>

                                <ValidationObserver v-slot="{ handleSubmit }">
                                    <form class="mt-4 form-text" @submit.prevent="handleSubmit(submitForm)">
                                        <div class="form-group">
                                            <label>Username</label>
                                            <validation-provider name="username" rules="required" v-slot="{ errors }">
                                                <input v-model="username" type="text" class="form-control mb-0"
                                                       placeholder="UserName">
                                                <span style="color: rgb(215 41 41)">{{ errors[0] }}</span>
                                            </validation-provider>
                                        </div>

                                        <div class="form-group">
                                            <label for="">Password</label>
                                            <validation-provider name="password" rules="required|min:8|max:16"
                                                                 vid="confirmation"
                                                                 v-slot="{ errors }">
                                                <input v-model="password" type="password" class="form-control mb-0"
                                                       placeholder="Password">
                                                <span style="color: rgb(215 41 41)">{{ errors[0] }}</span>
                                            </validation-provider>
                                        </div>

                                        <div class="form-group">
                                            <label>Confirm Password</label>
                                            <validation-provider name="confirm_password"
                                                                 rules="required|confirmed:confirmation"
                                                                 v-slot="{ errors }">
                                                <input v-model="confirm_password" type="password"
                                                       class="form-control mb-0"
                                                       placeholder="Confirm Password">
                                                <span style="color: rgb(215 41 41)">{{ errors[0] }}</span>
                                            </validation-provider>
                                        </div>

                                        <div class="sign-info text-center">
                                            <button type="submit" class="btn btn-white d-block w-100 mb-2">Sign Up
                                            </button>
                                            <span class="text-dark d-inline-block line-height-2">Already Have Account ? <router-link
                                                :to="{name:'login'}" class="text-white">Log In</router-link></span>
                                        </div>
                                    </form>
                                </ValidationObserver>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- Sign in END -->
</template>

<script>

// import axios from 'axios'
import {ValidationObserver} from 'vee-validate'
import {ValidationProvider} from 'vee-validate/dist/vee-validate.full.esm'
import axios from 'axios'

export default {
    name: 'Signup',
    data() {
        return {
            errors: [],
            username: '',
            password: '',
            confirm_password: ''
        }
    },
    components: {
        ValidationProvider,
        ValidationObserver
    },
    methods: {
        async submitForm() {
            await axios.post('/api/v1/users/', {
                username: this.username,
                password: this.password
            })
                .then(response => {
                    this.$toast.success('SignUp successfully. Please login', {
                        type: 'success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right'
                    })
                    this.$router.push({name: 'login'})
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                            this.errors.push(`${error.response.data[property]}`)
                        }
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>

<style scoped>

</style>
