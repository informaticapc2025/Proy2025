<template>
  <div class="recognition-card">
    <h3>
      <i class="fa-solid fa-award" style="margin-right: 5px; color: #8ca1af"></i>
      Reconocimientos
    </h3>
    <div v-if="reconocimientos.length === 0" class="empty">
      Aún no hay reconocimientos
    </div>
    <div v-else>
      <div
        class="reconocimiento"
        v-for="(item, index) in reconocimientos"
        :key="index"
      >
        <i class="fa-solid fa-trophy"></i>
        <div class="info">
          <div class="nombre">{{ item.alumno }}</div>
          <div class="descripcion">{{ item.descripcion }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const reconocimientos = ref([])

onMounted(async () => {
  try {
    const { data } = await axios.get('http://localhost:5000/reconocimientos')
    reconocimientos.value = data
  } catch (error) {
    console.error('Error al obtener reconocimientos', error)
  }
})
</script>

<style scoped>
.recognition-card {
  background-color: #f2fbe7;
  border-radius: 15px;
  padding: 20px;
  margin-top: 15px;
  box-shadow: 2px 2px 8px #ccc;
}

h3 {
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 10px;
  background-color: #fff;
  padding: 8px 12px;
  border-radius: 12px;
  width: fit-content;
}

.reconocimiento {
  display: flex;
  align-items: flex-start;
  margin-bottom: 10px;
}

.reconocimiento i {
  font-size: 1.5rem;
  margin-right: 10px;
  color: #f1c40f;
}

.info {
  display: flex;
  flex-direction: column;
}

.nombre {
  font-weight: bold;
  font-size: 0.95rem;
}

.descripcion {
  font-size: 0.85rem;
  color: #666;
}

.empty {
  color: #aaa;
  font-style: italic;
}
</style>
