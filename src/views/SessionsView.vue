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
    <template v-if="!isAdmin">
      <n-data-table
        ref="dataTableInst"
        :columns="columnsAlumno"
        :data="dataAlumno"
        :pagination="pagination"
      />
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
    </template>
    <template v-else>
      <div>
        <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 16px">
          <n-input v-model:value="filtros.area" placeholder="Área" style="flex: 1; min-width: 150px" />
          <n-input v-model:value="filtros.nombre" placeholder="Nombre" style="flex: 1; min-width: 150px" />
          <n-input v-model:value="filtros.id_numero" placeholder="ID número" style="flex: 1; min-width: 150px" />
          <n-date-picker
            v-model:value="filtros.fecha"
            type="date"
            placeholder="Fecha"
            format="dd/MM/yyyy"
            value-format="yyyy-MM-dd"
          />
          <n-button @click="handleBuscar" type="primary" style="min-width: 100px">Buscar</n-button>
          <n-button @click="clearFilters" secondary style="min-width: 100px">Limpiar</n-button>
        </div>

        <!-- Tabs de citas -->
        <n-tabs v-model:value="tabActivo" type="line">
          <n-tab-pane name="pendientes" tab="Pendientes">
            <n-data-table
              ref="tablaPendientes"
              :columns="columnsAdmin"
              :data="dataPendiente"
              :pagination="pagination"
            />
          </n-tab-pane>

          <n-tab-pane name="culminadas" tab="Culminadas">
            <n-data-table
              ref="tablaCulminadas"
              :columns="columnsAdmin"
              :data="dataCulminada"
              :pagination="pagination"
            />
          </n-tab-pane>
        </n-tabs>
      </div>
    </template>
  </div>
</template>
<script lang="ts">
// @ts-ignore
import { dateFormatV2 } from '@/util/functions'
import { defineComponent, ref, h, onMounted, reactive } from 'vue'
import { NButton, NModal, NInput, NSelect, NDataTable } from 'naive-ui'
import CitasService from '@/services/CitasService'
import LoginService from '@/services/LoginService'
import type { CitaAdmin, CitaAlumno } from '@/models/Cita'

export default defineComponent({
  components: {
    NButton,
    NModal,
    NInput,
    NSelect,
    NDataTable,
  },
  setup() {
    const tabActivo = ref('pendientes')
    const dataAlumno = ref<CitaAlumno[]>([])
    const dataPendiente = ref<CitaAdmin[]>([])
    const dataCulminada = ref<CitaAdmin[]>([])
    const showModal = ref(false)
    const selectedSlot = ref<any>(null)
    const isAdmin = LoginService.isAdmin()
    const user = ref(LoginService.getCurrentUser())
    const form = ref({ motivo: '', descripcion: '', area: '' })
    const filtros = reactive({
      area: '',
      nombre: '',
      id_numero: '',
      fecha: null,
    })
    const columnsAdmin = [
      { title: 'Número', key: 'index' },
      { title: 'Fecha', key: 'fecha' },
      { title: 'Horario', key: 'horario' },
      { title: 'Area', key: 'area' },
      { title: 'Nombre', key: 'nombre' },
      { title: 'Estado', key: 'estado' },
    ]
    const columnsAlumno = [
      { title: 'Número', key: 'index' },
      { title: 'Fecha', key: 'fecha' },
      { title: 'Horario', key: 'horario' },
      { title: 'Motivo', key: 'motivo' },
      { title: 'Area', key: 'area' },
      {
        title: 'Estado',
        key: 'estado',
        render(row: any) {
          if (row.estado === 'Solicitado') {
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
              { default: () => 'Solicitado' },
            )
          } else {
            return h(
              NButton,
              {
                size: 'small',
                class: 'btn-no-disponible',
                disabled: true,
              },
              { default: () => 'Aprobado' },
            )
          }
        },
      },
    ]

    onMounted(async () => {
      chooseCitas()
    })

    const submitCita = () => {
      console.log('Formulario enviado:', form.value, selectedSlot.value)
      showModal.value = false
    }

    async function loadCitasSolicitadasPorUsuario() {
      try {
        const items = await CitasService.obtenerCitasSolicitadasPorUsuario(user.value.id)
        dataAlumno.value = items.map((a, i) => ({
          index: i + 1,
          area: a.area,
          descripcion: a.descripcion,
          estado: a.estado ?? '',
          fecha: dateFormatV2(a.fecha),
          horario: a.horario,
          id: a.id,
          motivo: a.motivo,
        }))
      } catch (error) {
        console.log(error)
      }
    }

    function getFilters() {
      const params: Record<string, any> = {}
      if (filtros.area) params.area = filtros.area
      if (filtros.nombre) params.nombre = filtros.nombre
      if (filtros.id_numero) params.id_numero = Number(filtros.id_numero)
      if (filtros.fecha) {
        const fechaObj = new Date(filtros.fecha)
        params.fecha = fechaObj.toISOString().split('T')[0]
      }
      return params
    }

    function clearFilters() {
      filtros.area = ''
      filtros.nombre = ''
      filtros.id_numero = ''
      filtros.fecha = null
      handleBuscar()
    }

    async function loadCitasPendientes() {
      try {
        const items = await CitasService.obtenerCitasPendientes(getFilters())
        dataPendiente.value = items.map((a, i) => ({
          index: i + 1,
          area: a.area,
          estado: a.estado,
          fecha: dateFormatV2(a.fecha),
          horario: a.horario,
          id: a.id,
          id_alumno: a.id_alumno,
          motivo: a.motivo,
          nombre: a.nombre,
        }))
      } catch (error) {
        console.log(error)
      }
    }

    async function loadCitasCulminadas() {
      try {
        const items = await CitasService.obtenerCitasCulminadas(getFilters())
        dataCulminada.value = items.map((a, i) => ({
          index: i + 1,
          area: a.area,
          estado: a.estado,
          fecha: dateFormatV2(a.fecha),
          horario: a.horario,
          id: a.id,
          id_alumno: a.id_alumno,
          motivo: a.motivo,
          nombre: a.nombre,
        }))
      } catch (error) {
        console.log(error)
      }
    }

    function chooseCitas() {
      if (isAdmin) {
        loadCitasPendientes()
        loadCitasCulminadas()
      } else {
        loadCitasSolicitadasPorUsuario()
      }
    }

    function handleBuscar() {
      if (tabActivo.value === 'pendientes') {
        loadCitasPendientes()
      } else {
        loadCitasCulminadas()
      }
    }

    return {
      filtros,
      dataAlumno,
      columnsAlumno,
      dataPendiente,
      dataCulminada,
      columnsAdmin,
      showModal,
      selectedSlot,
      form,
      submitCita,
      clearFilters,
      loadCitasPendientes,
      loadCitasCulminadas,
      handleBuscar,
      pagination: ref({ pageSize: 7 }),
      dataTableInst: ref(null),
      isAdmin,
      tabActivo
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
