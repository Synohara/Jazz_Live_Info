import Vue from 'vue'
import Router from 'vue-router'
import LiveIndex from '@/components/Live/Index'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'LiveIndex',
      component: LiveIndex,
    },
    {
      path: '/:page',
      name: 'LiveIndexPage',
      component: LiveIndex,
    },
  ],
})