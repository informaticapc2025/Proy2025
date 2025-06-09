import { createRouter, createWebHistory } from 'vue-router'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/anuncios',
      name: 'anuncios',
      component: () => import('../views/PostsView.vue')
    },
    {
      path: '/actividades',
      name: 'actividades',
      component: () => import('../views/ActivitiesView.vue')
    },
    {
      path: '/permisos',
      name: 'permisos',
      component: () => import('../views/PermissionsView.vue')
    },
    {
      path: '/quejas',
      name: 'quejas',
      component: () => import('../views/ReportsView.vue')
    },
    {
      path: '/asistencia',
      name: 'asistencia',
      component: () => import('../views/AssistsView.vue')
    },
    {
      path: '/citas',
      name: 'citas',
      component: () => import('../views/SessionsView.vue')
    },
  ],
})

export default router
