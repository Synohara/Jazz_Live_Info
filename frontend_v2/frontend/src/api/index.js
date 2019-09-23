import axios from 'axios'

import lives from './lives'

const client = axios.create({
  baseURL: process.env.VUE_APP_API_ENDPOINT,
})

client.lives = lives(client)

client.install = function (Vue) {
  Object.defineProperty(Vue.prototype, '$request', {
    get () {
      return client
    },
  })
}

export default client