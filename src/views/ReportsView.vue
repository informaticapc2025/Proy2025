<template>
  <div class="about">
    <h1>Mis reportes</h1>
  </div>

  <div style="background-color: rgba(184, 186, 163, 0.85); width: 95%; padding: 20px">
    <div class="text-right">
      <v-btn variant="outlined" class="mb-6" @click="openModalNuevo">Nueva Queja</v-btn>
    </div>

    <v-data-table :items="filteredData" class="elevation-1" :items-per-page="5">
      <template #headers>
        <tr>
          <th>N° Reporte</th>
          <th>Asunto</th>
          <th>Motivo</th>
          <th>Fecha</th>
          <th>Estado</th>
          <th>Acción</th>
        </tr>
      </template>
      <template #item="{ item }">
        <tr>
          <td>{{ item.numero }}</td>
          <td>{{ item.asunto }}</td>
          <td>{{ item.motivo }}</td>
          <td>{{ item.fecha }}</td>
          <td>{{ item.estado }}</td>
          <td>
            <button
              @click="openModal(item)"
              style="background: none; border: none; cursor: pointer"
              title="Ver detalle"
            >
              <i class="fa-solid fa-eye" style="color: #1976d2; font-size: 20px"></i>
            </button>
          </td>
        </tr>
      </template>
    </v-data-table>

    <ModalQueja v-model="showModal" :item="selectedItem" :user="user" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import QuejasService from '@/services/QuejasService'
import ModalQueja from './modal/ModalQueja.vue'
import LoginService from '@/services/LoginService'

const showModal = ref(false)
const selectedItem = ref(null)
const data = ref([])
const user = ref(null)

const selectedAddress = ref(null)

const filteredData = computed(() => {
  if (!selectedAddress.value) return data.value
  return data.value.filter((item) => item.address?.includes(selectedAddress.value))
})

// Cargar actividades al montar el componente
onMounted(async () => {
  await loadUser()
  await loadQuejas()
})

async function loadUser() {
  user.value = await LoginService.getCurrentUser()
}

async function loadQuejas() {
  try {
    const quejas = await QuejasService.obtenerActividadesPorUsuario(user.value.id)
    data.value = quejas.map((a) => ({
      numero: a.codigo,
      asunto: a.asunto,
      motivo: a.motivo ?? '',
      fecha: a.fecha,
      estado: a.estado
    }))
  } catch (error) {
    console.error(error)
  }
}

function openModal(item) {
  selectedItem.value = item
  showModal.value = true
}

function openModalNuevo() {
  selectedItem.value = {
    numero: '',
    asunto: '',
    motivo: '',
    fecha: '',
    estado: '',
    descripcion: '',
  }
  showModal.value = true
}
</script>

<style scoped>
.n-data-table,
.n-data-table-tbody {
  background-color: transparent;
}
</style>
