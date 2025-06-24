<template>
  <div class="pa-4">
    <v-card
      class="pa-6"
      style="
        border-radius: 16px;
        background-color: rgba(184, 186, 163, 0.85);
        border: 3px solid #4a90e2;
      "
      elevation="4"
    >
      <h2 class="text-h4 font-weight-bold mb-6" style="color: #b8860b">Reporte de Asistencia</h2>

      <v-row class="mb-6">
        <v-col cols="12" sm="6">
          <v-select
            v-model="selectedYear"
            :items="years"
            label="Año"
            variant="outlined"
            density="comfortable"
            class="custom-select"
            @update:model-value="updateAttendanceData"
          ></v-select>
        </v-col>
        <v-col cols="12" sm="6">
          <v-select
            v-model="selectedMonth"
            :items="months"
            item-title="name"
            item-value="value"
            label="Mes"
            variant="outlined"
            density="comfortable"
            class="custom-select"
            @update:model-value="updateAttendanceData"
          ></v-select>
        </v-col>
      </v-row>

      <v-card class="pa-0" style="border-radius: 12px; background-color: #f5f5f5" elevation="2">
        <v-row class="ma-0 pa-4" style="background-color: #e0e0e0; border-radius: 12px 12px 0 0">
          <v-col cols="6" class="pa-2">
            <h4 class="text-h6 font-weight-bold text-grey-darken-2">Fecha</h4>
          </v-col>
          <v-col cols="6" class="pa-2 text-center">
            <h4 class="text-h6 font-weight-bold text-grey-darken-2">Asistencia</h4>
          </v-col>
        </v-row>

        <div v-for="(record, index) in attendanceRecords" :key="index">
          <v-row
            class="ma-0 pa-4 align-center"
            :class="{ 'bg-grey-lighten-4': index % 2 === 0 }"
            style="border-bottom: 1px solid #e0e0e0"
          >
            <v-col cols="6" class="pa-2">
              <span class="text-body-1 font-weight-medium text-grey-darken-2">
                {{ record.fecha }}
              </span>
            </v-col>
            <v-col cols="6" class="pa-2 text-center">
              <v-btn
                :color="getStatusColor(record.status)"
                size="small"
                style="border-radius: 16px; text-transform: none; font-weight: 500"
                min-width="100px"
                @click="handleStatusClick(record)"
              >
                {{ getStatusText(record.status) }}
              </v-btn>
            </v-col>
          </v-row>
        </div>
      </v-card>
      <v-row class="mt-4">
        <v-col cols="12">
          <v-card class="pa-4" style="border-radius: 12px; background-color: #f8f9fa">
            <h4 class="text-h6 font-weight-bold mb-3 text-grey-darken-2">Resumen del Mes</h4>
            <v-row>
              <v-col cols="4" class="text-center">
                <div class="text-h5 font-weight-bold text-green">
                  {{ attendanceSummary.attended }}
                </div>
                <div class="text-body-2 text-grey-darken-1">Asistió</div>
              </v-col>
              <v-col cols="4" class="text-center">
                <div class="text-h5 font-weight-bold text-red">
                  {{ attendanceSummary.absent }}
                </div>
                <div class="text-body-2 text-grey-darken-1">No asistió</div>
              </v-col>
              <v-col cols="4" class="text-center">
                <div class="text-h5 font-weight-bold text-blue">
                  {{ attendanceSummary.reports }}
                </div>
                <div class="text-body-2 text-grey-darken-1">Reportes</div>
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </v-card>

    <v-dialog v-model="reportDialog" max-width="500px">
      <v-card class="pa-4">
        <v-card-title class="text-h5 font-weight-bold"> Reporte Detallado </v-card-title>
        <v-card-text>
          <p><strong>Fecha:</strong> {{ selectedRecord?.fecha }}</p>
          <p><strong>Estado:</strong> {{ getStatusText(selectedRecord?.status) }}</p>
          <p><strong>Hora de entrada:</strong> 08:30 AM</p>
          <p><strong>Hora de salida:</strong> 17:00 PM</p>
          <p><strong>Observaciones:</strong> Asistencia completa registrada correctamente.</p>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click="reportDialog = false"> Cerrar </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-snackbar v-model="snackbar.show" :color="snackbar.color" timeout="3000">
      {{ snackbar.message }}
      <template v-slot:actions>
        <v-btn variant="text" @click="snackbar.show = false"> Cerrar </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>
<script setup>
import { ref, reactive, computed } from 'vue'

const selectedYear = ref('2024')
const selectedMonth = ref('marzo')
const reportDialog = ref(false)
const selectedRecord = ref(null)

const years = ['2022', '2023', '2024', '2025']
const months = [
  { name: 'Enero', value: 'enero' },
  { name: 'Febrero', value: 'febrero' },
  { name: 'Marzo', value: 'marzo' },
  { name: 'Abril', value: 'abril' },
  { name: 'Mayo', value: 'mayo' },
  { name: 'Junio', value: 'junio' },
  { name: 'Julio', value: 'julio' },
  { name: 'Agosto', value: 'agosto' },
  { name: 'Septiembre', value: 'septiembre' },
  { name: 'Octubre', value: 'octubre' },
  { name: 'Noviembre', value: 'noviembre' },
  { name: 'Diciembre', value: 'diciembre' },
]

const attendanceRecords = ref([
  { fecha: 'Lunes 3', status: 'report' },
  { fecha: 'Martes 4', status: 'absent' },
  { fecha: 'Miércoles 5', status: 'absent' },
  { fecha: 'Jueves 6', status: 'attended' },
  { fecha: 'Viernes 7', status: 'attended' },
  { fecha: 'Lunes 10', status: 'report' },
  { fecha: 'Martes 11', status: 'attended' },
  { fecha: 'Miércoles 12', status: 'absent' },
])

const snackbar = reactive({
  show: false,
  message: '',
  color: 'success',
})

// Función para obtener color del estado
const getStatusColor = (status) => {
  switch (status) {
    case 'attended':
      return 'success'
    case 'absent':
      return 'error'
    case 'report':
      return 'success'
    default:
      return 'grey'
  }
}

// Función para obtener texto del estado
const getStatusText = (status) => {
  switch (status) {
    case 'attended':
      return 'Asistió'
    case 'absent':
      return 'No asistió'
    case 'report':
      return 'Ver reporte'
    default:
      return 'Sin datos'
  }
}

// Resumen de asistencia
const attendanceSummary = computed(() => {
  const attended = attendanceRecords.value.filter((r) => r.status === 'attended').length
  const absent = attendanceRecords.value.filter((r) => r.status === 'absent').length
  const reports = attendanceRecords.value.filter((r) => r.status === 'report').length

  return { attended, absent, reports }
})

// Función para manejar click en estado
const handleStatusClick = (record) => {
  if (record.status === 'report') {
    selectedRecord.value = record
    reportDialog.value = true
  } else {
    snackbar.message = `Estado: ${getStatusText(record.status)} - ${record.fecha}`
    snackbar.color = record.status === 'attended' ? 'success' : 'error'
    snackbar.show = true
  }
}

// Función para actualizar datos de asistencia
const updateAttendanceData = () => {
  snackbar.message = `Datos actualizados para ${selectedMonth.value} ${selectedYear.value}`
  snackbar.color = 'info'
  snackbar.show = true

  // Aquí podrías hacer una llamada a la API para obtener nuevos datos
  console.log('Actualizando datos para:', selectedYear.value, selectedMonth.value)
}
</script>

<style scoped>
.custom-select :deep(.v-field) {
  border-radius: 8px;
  background-color: #f5f5f5;
}

.custom-select :deep(.v-field--focused) {
  background-color: white;
}

.custom-select :deep(.v-field__input) {
  color: #424242;
  font-weight: 500;
}
</style>
