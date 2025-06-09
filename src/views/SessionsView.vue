<template>
  <div class="citas-wrapper">
    <!-- Panel lateral fijo -->
    <div class="sidebar-fijo">
      <UserCard />
      <SidebarMenu />
      <Salir />
    </div>

    <!-- Contenido principal -->
    <div class="contenido">
      <div class="titulo">
        <h2><span class="resaltado">Citas</span> Disponibles</h2>
      </div>

      <div class="citas-header">
        <div class="mes">Mayo</div>
        <div class="horario">
          <strong>Hora de atención</strong>
          <div>09:00am - 12:00pm</div>
          <div>02:00pm - 05:00pm</div>
        </div>
      </div>

      <div class="tabla-contenedor">
        <n-data-table ref="dataTableInst" :columns="columns" :data="data" :pagination="pagination" />
      </div>
    </div>

    <!-- Modal para agendar cita -->
    <n-modal v-model:show="showModal" preset="dialog" class="modal-cita">
      <template #header>
        <h2 style="color: #a1003c; text-align: center;">Agendar Cita</h2>
      </template>

      <div class="form-cita">
        <div>
          <label>Motivo:</label>
          <n-input placeholder="Motivo de la cita" v-model:value="form.motivo" />
        </div>

        <div>
          <label>Descripción:</label>
          <n-input type="textarea" placeholder="Describe el motivo..." v-model:value="form.descripcion" />
        </div>

        <div>
          <label>Área disponible:</label>
          <n-select
            v-model:value="form.area"
            :options="[
              { label: 'Psicología', value: 'psicologia' },
              { label: 'Bienestar', value: 'bienestar' }
            ]"
          />
        </div>

        <div class="horario-seleccionado">
          <label>Horario elegido:</label>
          <div class="slot-box">
            <strong>{{ selectedSlot?.day }}</strong>
            <span>{{ selectedSlot?.hour }}</span>
          </div>
        </div>

        <div style="text-align: center; margin-top: 16px;">
          <n-button type="primary" style="background-color: #a1003c;" @click="submitCita">Enviar</n-button>
        </div>
      </div>
    </n-modal>
  </div>
</template>

<script setup lang="ts">
import { ref, h } from 'vue'
import { NButton, NModal, NInput, NSelect, NDataTable } from 'naive-ui'
import UserCard from '../components/layout/UserCard.vue'
import SidebarMenu from '../components/layout/SidebarMenu.vue'
import Salir from '../components/layout/Salir.vue'

const showModal = ref(false)
const selectedSlot = ref<any>(null)

const form = ref({
  motivo: '',
  descripcion: '',
  area: ''
})

const submitCita = () => {
  console.log('Formulario enviado:', form.value, selectedSlot.value)
  showModal.value = false
}

const data = [
  { key: 1, slot: 1, day: 'Lunes 10', hour: '09:00am - 10:00am', status: 'Disponible' },
  { key: 2, slot: 2, day: 'Lunes 10', hour: '10:00am - 11:00am', status: 'No Disponible' },
  { key: 3, slot: 3, day: 'Lunes 10', hour: '11:00am - 12:00pm', status: 'Disponible' },
  { key: 4, slot: 4, day: 'Lunes 10', hour: '12:00pm - 01:00pm', status: 'Disponible' },
  { key: 5, slot: 5, day: 'Lunes 10', hour: '02:00pm - 03:00pm', status: 'No Disponible' },
  { key: 6, slot: 6, day: 'Lunes 10', hour: '03:00pm - 04:00pm', status: 'Disponible' },
  { key: 7, slot: 7, day: 'Lunes 10', hour: '04:00pm - 05:00pm', status: 'No Disponible' }
]

const columns = [
  { title: 'Horario', key: 'slot' },
  { title: 'Día', key: 'day' },
  { title: 'Hora', key: 'hour' },
  {
    title: 'Estado',
    key: 'status',
    render(row: any) {
      if (row.status === 'Disponible') {
        return h(
          NButton,
          {
            size: 'small',
            class: 'btn-disponible',
            onClick: () => {
              selectedSlot.value = row
              showModal.value = true
            }
          },
          { default: () => 'Disponible' }
        )
      } else {
        return h(
          NButton,
          {
            size: 'small',
            class: 'btn-no-disponible',
            disabled: true
          },
          { default: () => 'No Disponible' }
        )
      }
    }
  }
]

const pagination = ref({ pageSize: 7 })
</script>

<style scoped>
.citas-wrapper {
  display: flex;
  min-height: 100vh;
  background: url('/src/assets/background.jpg') no-repeat center center fixed;
  background-size: cover;
  padding: 30px;
}

/* Panel izquierdo */
.sidebar-fijo {
  width: 15%;
  min-width: 200px;
  padding: 10px 15px;
  display: flex;
  flex-direction: column;
  background-color: transparent;
  z-index: 100;
}

/* Contenido */
.contenido {
  flex: 1;
  background: rgba(217, 217, 217, 0.3);
  backdrop-filter: blur(8px);
  padding: 25px 30px;
  border-radius: 15px;
  margin-left: 20px;
  width: 100%;
}

.titulo {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 25px;
  color: white;
}

.titulo .resaltado {
  color: #a1003c;
}

.citas-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.mes {
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

.horario {
  text-align: right;
  font-size: 14px;
}

/* Tabla */
.tabla-contenedor {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

/* Botones */
.btn-disponible {
  background-color: #f0c929;
  color: black;
}
.btn-no-disponible {
  background-color: #bdbdbd;
  color: white;
}

/* Modal */
.modal-cita .n-dialog {
  border-radius: 12px;
  padding: 24px;
  background-color: #fff8f8;
}
.form-cita {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.form-cita label {
  font-weight: bold;
  margin-bottom: 4px;
  display: block;
}
.slot-box {
  background-color: #e0e0e0;
  padding: 10px;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  font-weight: bold;
}
</style>
