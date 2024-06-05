import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import ProductListView from '@/views/ProductListView.vue'
import ExchangeCalcView from '@/views/ExchangeCalcView.vue'
import ProductDetail from '@/components/ProductDetail.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import MapView from '@/views/MapView.vue'
import BoardView from '@/views/BoardView.vue'
import BoardDetail from '@/views/BoardDetail.vue'
import CreateView from '@/views/CreateView.vue'
import JoinListView from '@/views/JoinListView.vue'
import UserUpdate from '@/views/userUpdate.vue'
import BoardUpdate from '@/views/BoardUpdate.vue'
import { useUserStore } from '@/stores/user'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/products',
      name: 'products',
      component: ProductListView
    },    
    {
      path: '/products/:id',
      name: 'productsDetail',
      component: ProductDetail
    },
    {
      path: '/exchange',
      name: 'exchange',
      component: ExchangeCalcView
    },
    {
      path:'/signup',
      name:'signup',
      component: SignUpView
    },
    {
      path:'/login',
      name:'login',
      component: LoginView
    },
    {
      path:'/profile',
      name:'profile',
      component: UserProfileView
    },
    {
      path:'/map',
      name:'map',
      component: MapView
    },
    {
      path:'/board',
      name:'board',
      component: BoardView
    },
    {
      path:'/boards/:id',
      name:'detail',
      component:BoardDetail
    },
    {
      path:'/create',
      name:'create',
      component:CreateView
    },
    {
      path:'/joinList',
      name:'joinList',
      component:JoinListView
    },
    {
      path:'/userUpdate/:id',
      name:'userUpdate',
      component:UserUpdate
    },
    {
      path:'/boardUpdate/:id',
      name: 'boardUpdate',
      component:BoardUpdate
    }

  ]
})

router.beforeEach((to,from)=>{
  const store = useUserStore()
  if((to.name === 'signup' || to.name==='login')&&(store.isLogin)){
    alert('이미 로그인이 되어있습니다.')
    return { name : 'main'}
  }
})

export default router
