import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
        path: '/',
        redirect:'/login'
    },
    {
        path: '/test',
        component: () => import('../components/TheWelcome.vue')
    },
    {
        path: '/login',
        component: () => import('../views/Login.vue')
    },
    {
        path: '/main',
        component: () => import('../components/HelloWorld.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router