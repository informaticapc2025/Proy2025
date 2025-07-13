<template>
  <div class="citas-container">
    <div class="citas-header">
      <div class="mes">Mayo</div>
      <div class="horario">
        <strong>Hora de atención</strong>
        <div>09:00am - 12:00pm</div>
        <div>02:00pm - 05:00pm</div>
      </div>
    </div>

    <n-data-table ref="dataTableInst" :columns="columns" :data="data" :pagination="pagination" />

    <!-- Modal para agendar cita -->
    <n-modal v-model:show="showModal" preset="dialog" class="modal-cita">
      <template #header>
        <h2 style="color: #a1003c; text-align: center">Agendar Cita</h2>
      </template>

      <div class="form-cita">
        <div>
          <label>Motivo:</label>
          <n-input placeholder="Motivo de la cita" v-model:value="form.motivo" />
        </div>

        <div>
          <label>Descripción:</label>
          <n-input
            type="textarea"
            placeholder="Describe el motivo..."
            v-model:value="form.descripcion"
          />
        </div>

        <div>
          <label>Área disponible:</label>
          <n-select
            v-model:value="form.area"
            :options="[
              { label: 'Psicología', value: 'psicologia' },
              { label: 'Bienestar', value: 'bienestar' },
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

        <div style="text-align: center; margin-top: 16px">
          <n-button type="primary" style="background-color: #a1003c" @click="submitCita"
            >Enviar</n-button
          >
        </div>
      </div>
    </n-modal>
  </div>
</template>

<script lang="ts">
// @ts-ignore
import { dateFormatV2 } from '@/util/functions'
import { defineComponent, ref, h, onMounted } from 'vue'
import { NButton, NModal, NInput, NSelect, NDataTable } from 'naive-ui'
import CitasService from '@/services/CitasService'
import LoginService from '@/services/LoginService'
import type { Cita } from '@/models/Cita'

export default defineComponent({
  components: {
    NButton,
    NModal,
    NInput,
    NSelect,
    NDataTable,
  },
  setup() {
    const data = ref<Cita[]>([])
    const showModal = ref(false)
    const selectedSlot = ref<any>(null)
    const user = ref(LoginService.getCurrentUser())
    const form = ref({ motivo: '', descripcion: '', area: ''})

    const submitCita = () => {
      console.log('Formulario enviado:', form.value, selectedSlot.value)
      showModal.value = false
    }

    onMounted(async () => {
      loadCitasSolicitadasPorUsuario()
    })

    async function loadCitasSolicitadasPorUsuario() {
      try {
        const items = await CitasService.obtenerCitasSolicitadasPorUsuario(user.value.id)
        data.value = items.map((a, i) => ({
        index: i + 1,
        area: a.area,
        descripcion: a.descripcion,
        estado: a.estado ?? '',
        fecha: dateFormatV2(a.fecha),
        horario: a.horario,
        id: a.id,
        motivo: a.motivo
      }))
      } catch (error) {
        console.log(error)
      }
    }

    const columns = [
      { title: 'Horario', key: 'index' },
      { title: 'Fecha', key: 'fecha' },
      { title: 'Horario', key: 'horario' },
      { title: 'Motivo', key: 'motivo' },
      { title: 'Area', key: 'area' },
      {
        title: 'Estado',
        key: 'estado',
        render(row: any) {
          if (row.estado === 'Aprobado') {
            return h(
              NButton,
              {
                size: 'small',
                class: 'btn-disponible',
                onClick: () => {
                  selectedSlot.value = row
                  showModal.value = true
                },
              },
              { default: () => 'Aprobado' },
            )
          } else {
            return h(
              NButton,
              {
                size: 'small',
                class: 'btn-no-disponible',
                disabled: true,
              },
              { default: () => 'Solicitado' },
            )
          }
        },
      },
    ]

    return {
      data,
      columns,
      showModal,
      selectedSlot,
      form,
      submitCita,
      pagination: ref({ pageSize: 7 }),
      dataTableInst: ref(null),
    }
  },
})
</script>

<style scoped>
.citas-container {
  background-color: rgba(184, 186, 163, 0.85);
  width: 95%;
  padding: 20px;
  border-radius: 15px;
  margin: 0 auto;
}
.citas-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}
.mes {
  font-size: 24px;
  font-weight: bold;
}
.horario {
  text-align: right;
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
