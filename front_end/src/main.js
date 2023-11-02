import './assets/main.css'

import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'

const app = createApp(App).mount('#app')
app.use(ElementPlus)