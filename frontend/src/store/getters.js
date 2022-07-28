export default {
    headerTitle: state => state.headerTitle,
    isLoading: state => state.isLoading,
    isAuthentication: state => state.isAuthentication,
    token: state => state.token,
    cart: state => state.cart,
    cartTotalLength: (state) => {
        return state.cart.items.reduce((acc, curVal) => {
            return acc + curVal.quantity
        }, 0)
    },
    cartTotalPrice: (state) => {
        return state.cart.items.reduce((acc, curVal) => {
            return acc + (curVal.book.price * curVal.quantity)
        }, 0)
    }
}
