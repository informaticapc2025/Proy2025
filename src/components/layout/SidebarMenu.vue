<template>
   <n-card class="card-sidemenu">
      <n-menu
        :options="menuOptions"
        :value="route.path"
        @update:value="navigate"
      />
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
      label: 'Actividades',
      key: '/actividades',
    },
    {
      label: 'Permisos',
      key: '/permisos',
    },
    {
      label: 'Quejas',
      key: '/quejas',
    },
    {
      label: 'Asistencias',
      key: '/asistencias',
    },
    {
      label: 'Citas',
      key: '/citas',
    }
  ]
  
  function navigate(key) {
    router.push(key)
  }
</script>
  
<style scoped>
  .card-sidemenu {
    background-color: #7E271B;
    padding: 10px;
    border-radius: 25px;
    border: none;
  }
</style>
