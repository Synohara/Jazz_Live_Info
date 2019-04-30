import Vue from 'vue'
import App from './App'
import router from './router'
import Vuetify from 'vuetify' 
import api from './api' 

Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(api) 

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
