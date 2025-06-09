<template>
  <div class="card">
    <div class="section">
      <h3>
        <i class="fa-solid fa-balloon"></i>
        Cumpleaños de Hoy
      </h3>
      <ul>
        <li v-for="cumple in cumpleaños" :key="cumple.id">
          <i class="fa-solid fa-cake-candles"></i>
          {{ cumple.nombre }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const cumpleaños = ref([])

onMounted(async () => {
  const { data } = await axios.get('http://localhost:5000/usuarios')
  const hoy = new Date().toISOString().slice(5, 10) // MM-DD
  cumpleaños.value = data.filter(u => u.rol === 'alumno' && u.fecha_cumpleaños?.slice(5, 10) === hoy)
})
</script>

<style scoped>
.card {
  background-color: #f4fce3;
  border-radius: 20px;
  padding: 15px;
  margin-bottom: 20px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}
.logo {
  width: 100%;
  margin-bottom: 15px;
}
.section h3 {
  font-size: 1rem;
  background-color: #e6f0fa;
  padding: 5px 10px;
  border-radius: 12px;
  display: inline-block;
  margin-bottom: 10px;
}
ul {
  padding: 0;
  list-style: none;
  margin: 0;
}
li {
  font-size: 0.95rem;
  padding: 4px 0;
}
</style>