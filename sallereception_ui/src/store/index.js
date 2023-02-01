import { createStore } from 'vuex'

export default createStore({
  state: {
    user: null,
    url:'http://localhost:8000/api',
    users: [],
    client: [],
    reservation:[],
    type_fete :[],
    type_decor : []
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
