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
                                <h3 class="mb-0 text-center text-white">Sign in</h3>
                                <p class="text-center text-white">Enter your username and password.</p>
                                <ValidationObserver v-slot="{ handleSubmit }">
                                    <form class="mt-4 form-text" @submit.prevent="handleSubmit(submitForm)">
                                        <div class="form-group">
                                            <label>Username</label>
                                            <validation-provider name="username" rules="required"
                                                                 v-slot="{ errors }">
                                                <input v-model="username" type="text" class="form-control mb-0"
                                                       placeholder="Enter username">
                                                <span style="color: rgb(215 41 41)">{{ errors[0] }}</span>
                                            </validation-provider>
                                        </div>
                                        <div class="form-group">
                                            <label>Password</label>
                                            <!--                                        <a href="#" class="float-right text-dark">Forgot password?</a>-->
                                            <validation-provider name="password" rules="required|min:6|max:16"
                                                                 v-slot="{ errors }">
                                                <input v-model="password" type="password" class="form-control mb-0"
                                                       placeholder="Password">
                                                <span style="color: rgb(215 41 41)">{{ errors[0] }}</span>
                                            </validation-provider>
                                        </div>
                                        <!--                                    <div class="d-inline-block w-100">-->
                                        <!--                                        <div class="custom-control custom-checkbox d-inline-block mt-2 pt-1">-->
                                        <!--                                            <input type="checkbox" class="custom-control-input" id="customCheck1">-->
                                        <!--                                            <label class="custom-control-label" for="customCheck1">Remember Me</label>-->
                                        <!--                                        </div>-->
                                        <!--                                    </div>-->
                                        <div class="sign-info text-center">
                                            <button type="submit" class="btn btn-white d-block w-100 mb-2">Sign in
                                            </button>
                                            <span class="text-dark dark-color d-inline-block line-height-2">Don't have an account?
                                                <router-link :to="{name:'signup'}"
                                                             class="text-white">Sign up</router-link></span>
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
import axios from 'axios'
import {mapActions} from 'vuex'
import {ValidationObserver} from 'vee-validate'
import {ValidationProvider} from 'vee-validate/dist/vee-validate.full.esm'

export default {
    name: 'Login',
    data() {
        return {
            errors: [],
            username: '',
            password: ''
        }
    },
    components: {
        ValidationProvider,
        ValidationObserver
    },
    mounted() {
        document.title = 'Login | Book Store'
    },
    methods: {
        ...mapActions(['removeToken', 'setToken']),
        async submitForm() {
            axios.defaults.headers.common['Authorization'] = ''
            this.removeToken()

            await axios.post('/api/v1/token/login', {
                username: this.username,
                password: this.password
            })
                .then(response => {
                    const token = response.data.auth_token
                    this.setToken(token)
                    axios.defaults.headers.common['Authorization'] = 'Token ' + token

                    localStorage.setItem('token', token)

                    const toPath = {name: this.$route.query.to || 'home'}

                    this.$router.push(toPath)
                    this.$toast.success('Login successfully', {
                        type: 'success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 3000,
                        position: 'bottom-right'
                    })
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
