<template>
  <n-card class="card-sidemenu">
    <n-menu :options="menuOptions" :value="route.path" @update:value="navigate" />
  </n-card>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const selectedKey = ref(route.path)

const menuOptions = [
  {
    label: 'Anuncios',
    key: '/anuncios',
  },
  {
    label: 'Quejas',
    key: '/quejas',
  },
  {
    label: 'Actividades',
    key: '/actividades',
  },
  {
    label: 'Permisos',
    key: '/permisos',
  },
  {
    label: 'Citas',
    key: '/citas',
  },
  {
    label: 'Asistencias',
    key: '/asistencias',
  },
]

function navigate(key) {
  router.push(key)
}
</script>

<style scoped>
.card-sidemenu {
  background-color: #7e271b;
  width: 100%;
  padding: 10px;
  border-radius: 25px;
  border: none;
}
</style>
