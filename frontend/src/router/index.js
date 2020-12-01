import Vue from 'vue'
import VueRouter from 'vue-router'
// import constants from '../lib/constants.js'
import Main from '../views/Main.vue'
import Perfume from '../views/Perfume.vue'
import test_sik from '../views/test_sik.vue'
import PerfumeDetail from '../views/PerfumeDetail.vue'
import Profile from '../views/Profile.vue'
import SearchPerfume from '../views/SearchPerfume.vue'
import RecommendPerfume from '../views/RecommendPerfume.vue'
import vueMoment from 'vue-moment'
Vue.use(VueRouter)
Vue.use(vueMoment)
const routes = [{
        path: '/',
        name: 'Main',
        component: Main
    },
    {
        path: '/perfume',
        name: 'Perfume',
        component: Perfume
    },
    {
        path: '/test_sik',
        name: 'test_sik',
        component: test_sik
    },
    {
        path: '/perfumedetail/:id',
        name: 'PerfumeDetail',
        component: PerfumeDetail
    },
    {
        path: '/user/profile',
        name: 'Profile',
        component: Profile
    },
    {
        path: '/searchperfume',
        name: 'SearchPerfume',
        component: SearchPerfume
    },
    {
        path: '/recommendperfume',
        name: 'RecommendPerfume',
        component: RecommendPerfume
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router