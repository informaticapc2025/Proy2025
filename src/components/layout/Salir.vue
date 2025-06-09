<template>
  <div class="logout-container">
    <button @click="salir" class="logout-button">Salir</button>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const salir = () => {
  localStorage.clear() // Limpia los datos del usuario
  router.push('/')     // Redirige a la ruta del login
}
</script>

<style scoped>
.logout-container {
  position: fixed;
  bottom: 20px;
  left: 20px; 
}

.logout-button {
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

.logout-button:hover {
  background-color: #c0392b;
}
</style>
