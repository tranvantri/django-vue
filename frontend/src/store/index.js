import state from './state'
import mutations from './mutations'
import actions from './actions'
import getters from './getters'
import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)

const storeConfig = {
    state,
    getters,
    mutations,
    actions
}

export default new Vuex.Store(storeConfig)
