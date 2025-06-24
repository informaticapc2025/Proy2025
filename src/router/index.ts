import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

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
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/anuncios',
      name: 'anuncios',
      component: () => import('../views/PostsView.vue'),
    },
    {
      path: '/actividades',
      name: 'actividades',
      component: () => import('../views/ActivitiesView.vue'),
    },
    {
      path: '/permisos',
      name: 'permisos',
      component: () => import('../views/PermissionsView.vue'),
    },
    {
      path: '/quejas',
      name: 'quejas',
      component: () => import('../views/ReportsView.vue'),
    },
    {
      path: '/asistencia',
      name: 'asistencia',
      component: () => import('../views/AssistsView.vue'),
    },
    {
      path: '/citas',
      name: 'citas',
      component: () => import('../views/SessionsView.vue'),
    },
  ],
})

export default router
