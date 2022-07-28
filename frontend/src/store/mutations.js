export default {
    setBreadcrumbs: (state, {breadcrumbs}) => {
        state.breadcrumbs = breadcrumbs
    },
    setIsLoading: (state, {isLoading}) => {
        state.isLoading = isLoading
    },
    initCart(state) {
        if (localStorage.getItem('cart')) {
            state.cart = JSON.parse(localStorage.getItem('cart'))
        } else {
            localStorage.setItem('cart', JSON.stringify(state.cart))
        }

        if (localStorage.getItem('token')) {
            state.token = localStorage.getItem('token')
            state.isAuthentication = true
        } else {
            state.token = ''
            state.isAuthentication = false
        }
    },
    addToCart(state, newItem) {
        const exists = state.cart.items.filter(item => item.book.id === newItem.book.id)

        if (exists.length) {
            exists[0].quantity = parseInt(exists[0].quantity) + parseInt(newItem.quantity)
        } else {
            state.cart.items.push(newItem)
        }

        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    incrementQuantity(state, newItem) {
        console.log(newItem.quantity)
        newItem.quantity += 1
        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    decrementQuantity(state, newItem) {
        newItem.quantity -= 1

        if (newItem.quantity === 0) {
            state.cart.items = state.cart.items.filter(item => item.book.id !== newItem.book.id)
        }

        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    removeFromCart(state, removeItem) {
        state.cart.items = state.cart.items.filter(item => item.book.id !== removeItem.book.id)
        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    updateStep(state, newStep) {
        state.cart.step = newStep
        localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    setToken(state, token) {
        state.token = token
        state.isAuthentication = true
        localStorage.setItem('token', token)
    },
    removeToken(state) {
        state.token = ''
        state.isAuthentication = false
        localStorage.setItem('token', '')
    }
}
