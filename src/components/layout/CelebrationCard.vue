<template>
  <n-card class="card-celebration">
    <div class="header-cc">
      <i class="fa-solid fa-cake-candles"></i>
      <p>Cumpleaños de hoy</p>
    </div>

    <n-list>
      <n-list-item>
        <div style="display: flex; align-items: center; gap: 2px">
          <img :src="cake" alt="cumpleaños" style="width: 20px; height: 25px" />
          <span>¡Feliz cumpleaños, Juan!</span>
        </div>
      </n-list-item>
      <n-list-item>
        <div style="display: flex; align-items: center; gap: 2px">
          <img :src="cake" alt="cumpleaños" style="width: 20px; height: 25px" />
          <span>¡Feliz cumpleaños, Juan!</span>
        </div>
      </n-list-item>
      <n-list-item>
        <div style="display: flex; align-items: center; gap: 2px">
          <img :src="cake" alt="cumpleaños" style="width: 20px; height: 25px" />
          <span>¡Feliz cumpleaños, Juan!</span>
        </div>
      </n-list-item>
    </n-list>
  </n-card>

  <n-card class="card-celebration">
  <div class="header-cc">
    <i class="fa-solid fa-award"></i>
    <p>Reconocimientos</p>
  </div>
  <n-list>
    <n-list-item v-for="(reconocimiento, index) in reconocimientoItems" :key="index">
      <div style="display: flex; align-items: center; gap: 2px">
        <img :src="cupe" alt="cumpleaños" style="width: 20px; height: 20px" />
        <div style="display: grid">
          <span>{{ reconocimiento.descripcion }}</span>
          <span style="font-size: 12px">{{ formatDate(reconocimiento.fecha) }}</span>
        </div>
      </div>
    </n-list-item>
  </n-list>
</n-card>
</template>

<script setup>
import cake from '@/assets/pngs/cake.jpg'
import cupe from '@/assets/pngs/trophy.jpg'
import { useRouter, useRoute } from 'vue-router'
import ReconocimientosService from '@/services/ReconocimientosService'
import { onMounted, ref } from 'vue'

const router = useRouter()
const route = useRoute()
const reconocimientoItems = ref([])

async function loadReconocimientos() {
  try {
    const reconocimientos = await ReconocimientosService.obtenerReconocimientos()
    reconocimientoItems.value = reconocimientos.map((a) => ({
      descripcion: a.descripcion,
      fecha: a.fecha,
    }))
  } catch (error) {
    console.error(error)
  }
}

function formatDate(fecha) {
  if (!fecha) return ''
  const partes = fecha.split('-')
  return `${partes[2]}/${partes[1]}/${partes[0]}`
}

onMounted(async () => {
  await loadReconocimientos()
})
</script>

<style scoped>
.card-celebration {
  background-color: #eef1dc;
  border-radius: 10px;
  margin-bottom: 30px;
  box-shadow: 0px 6px 5px rgba(0, 0, 0, 0.15);
}
.card-celebration .n-list {
  background-color: transparent;
}
.n-list-item {
  padding: 3px !important;
}
.header-cc {
  background-color: white;
  color: #4d2d0b;
  padding: 5px 8px;
  border-radius: 8px;
  font-size: 18px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.header-cc p {
  font-weight: 600 !important;
}
</style>
