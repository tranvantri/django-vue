export default {
    setBreadcrumbs({commit}, breadcrumbs) {
        commit('setBreadcrumbs', breadcrumbs)
    },
    setIsLoading({commit}, {isLoading}) {
        commit('setIsLoading', {isLoading})
    },
    initCartAction({commit}) {
        commit('initCart')
    },
    setToken({commit}, token) {
        commit('setToken', token)
    },
    removeToken({commit}) {
        commit('removeToken')
    },
    addToCart({commit}, newItem) {
        commit('addToCart', newItem)
    },
    decrementQuantity({commit}, newItem) {
        commit('decrementQuantity', newItem)
    },
    incrementQuantity({commit}, newItem) {
        commit('incrementQuantity', newItem)
    },
    removeFromCart({commit}, removeItem) {
        commit('removeFromCart', removeItem)
    },
    updateStep({commit}, newStep) {
        commit('updateStep', newStep)
    },
    clearCart({commit}) {
        commit('clearCart')
    }

}
