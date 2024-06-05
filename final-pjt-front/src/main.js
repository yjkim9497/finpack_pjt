import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import App from './App.vue'
const pinia = createPinia()
import router from './router'

pinia.use(piniaPluginPersistedstate)

const app = createApp(App)

// app.use(createPinia())
app.use(router)
app.use(pinia)
app.mount('#app')