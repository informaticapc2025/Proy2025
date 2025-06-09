<template>
  <n-card class="user-card">
    <div style="display: flex; align-items: center; gap: 5px">
      <i class="fa-solid fa-circle icon-green"></i>
      <p>{{ nombreUsuario }}</p>
    </div>
  </n-card>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const nombreUsuario = ref('Usuario')

onMounted(() => {
  const usuario = JSON.parse(localStorage.getItem('usuario'))
  if (usuario && usuario.nombre) {
    nombreUsuario.value = usuario.nombre
  }
})
</script>

<style scoped>
.user-card {
  background-color: #373b41;
  padding: 15px;
  color: white;
  border-radius: 20px;
}
.icon-green {
  color: green;
}
.icon-red {
  color: red;
}
</style>
