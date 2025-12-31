import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ShippingView from '../views/ShippingView.vue'
import ItemsView from '../views/ItemsView.vue'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
      {
      path: '/about',
      name: 'about',
      component: AboutView,
    },
      {
      path: '/shipping',
      name: 'shipping',
      component: ShippingView,
    },
        {
      path: '/items',
      name: 'items',
      component: ItemsView,
    },
  ],
})

export default router
