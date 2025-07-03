<template>
  <div class="pa-4">
    <v-row>
      <v-col cols="12" md="6">
        <v-card
          class="pa-4"
          style="border-radius: 16px; background-color: rgba(200, 210, 150, 0.3)"
        >
          <v-tabs v-model="activeTab" class="mb-4">
            <v-tab value="solicitud" class="custom-tab">
              <span :class="{ 'active-tab-text': activeTab === 'solicitud' }">
                Solicitud de vivienda
              </span>
            </v-tab>
            <v-tab value="area-comun" class="custom-tab">
              <span :class="{ 'active-tab-text': activeTab === 'area-comun' }"> Área Común </span>
            </v-tab>
          </v-tabs>

          <v-window v-model="activeTab">
            <v-window-item value="solicitud">
              <div class="mb-4">
                <p class="text-body-2 mb-4 text-grey-darken-2">
                  Registre el rango de días que estarás fuera de la vivienda universitaria:
                </p>

                <v-form @submit.prevent="submitRequest">
                  <div class="mb-3">
                    <label class="text-body-2 font-weight-medium mb-2 d-block"> Desde </label>
                    <v-select
                      v-model="form.desde"
                      :items="dateOptions"
                      variant="outlined"
                      density="comfortable"
                      hide-details
                      class="custom-select"
                    ></v-select>
                  </div>

                  <div class="mb-3">
                    <label class="text-body-2 font-weight-medium mb-2 d-block"> Hasta </label>
                    <v-select
                      v-model="form.hasta"
                      :items="dateOptions"
                      variant="outlined"
                      density="comfortable"
                      hide-details
                      class="custom-select"
                    ></v-select>
                  </div>

                  <div class="mb-4">
                    <label class="text-body-2 font-weight-medium mb-2 d-block"> Motivo </label>
                    <v-textarea
                      v-model="form.motivo"
                      variant="outlined"
                      rows="4"
                      hide-details
                      class="custom-textarea"
                    ></v-textarea>
                  </div>

                  <v-alert
                    type="warning"
                    variant="text"
                    class="mb-4 custom-alert"
                    density="compact"
                  >
                    <span class="text-caption text-red">
                      *Según el reglamento tu rango de salida de la ciudad universitaria tendrá a
                      ser revisada para su aprobación.
                    </span>
                  </v-alert>

                  <div class="d-flex justify-start">
                    <v-btn
                      type="submit"
                      color="#FFC107"
                      size="large"
                      style="
                        border-radius: 20px;
                        text-transform: none;
                        font-weight: 600;
                        color: #000;
                      "
                      min-width="100px"
                    >
                      Enviar
                    </v-btn>
                  </div>
                </v-form>
              </div>
            </v-window-item>

            <v-window-item value="area-comun">
              <div class="text-center pa-8">
                <v-icon size="64" color="grey-lighten-1" class="mb-4"> mdi-home-group </v-icon>
                <p class="text-h6 text-grey-darken-1">Área Común</p>
                <p class="text-body-2 text-grey">
                  Funcionalidad para áreas comunes próximamente disponible.
                </p>
              </div>
            </v-window-item>
          </v-window>
        </v-card>
      </v-col>

      <v-col cols="12" md="6">
        <v-card
          class="pa-4"
          style="border-radius: 16px; background-color: rgba(200, 210, 150, 0.3)"
        >
          <h3 class="text-h6 font-weight-bold mb-4 text-grey-darken-2">Reservas</h3>

          <div v-if="reservas.length === 0" class="text-center pa-8">
            <v-icon size="48" color="grey-lighten-1" class="mb-3"> mdi-calendar-blank </v-icon>
            <p class="text-body-2 text-grey">No tienes reservas registradas</p>
          </div>

          <div v-else>
            <v-card
              v-for="reserva in reservas"
              :key="reserva.id"
              class="mb-3 pa-3"
              variant="outlined"
              style="border-radius: 12px"
            >
              <div class="d-flex justify-space-between align-center">
                <div>
                  <p class="text-body-1 font-weight-medium mb-1">
                    {{ reserva.fechaInicio }} al {{ reserva.fechaFin }}
                  </p>
                  <div class="d-flex flex-column gap-1">
                    <v-chip
                      :color="getStatusColor(reserva.estado)"
                      size="small"
                      variant="flat"
                      class="text-caption"
                    >
                      {{ reserva.estado }}
                    </v-chip>
                  </div>
                </div>
                <v-btn
                  icon="mdi-close"
                  variant="text"
                  size="small"
                  color="red"
                  @click="deleteReserva(reserva.id)"
                >
                </v-btn>
              </div>
            </v-card>
          </div>
        </v-card>
      </v-col>
    </v-row>

    <!-- Snackbar para notificaciones -->
    <v-snackbar v-model="snackbar.show" :color="snackbar.color" timeout="3000">
      {{ snackbar.message }}
      <template v-slot:actions>
        <v-btn variant="text" @click="snackbar.show = false"> Cerrar </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'

const activeTab = ref('solicitud')

// Formulario
const form = reactive({
  desde: '',
  hasta: '',
  motivo: '',
})

// Opciones de fechas (simuladas)
const dateOptions = [
  '01/01/2025',
  '02/01/2025',
  '03/01/2025',
  '15/01/2025',
  '20/01/2025',
  '01/02/2025',
  '15/02/2025',
  '01/03/2025',
  '15/03/2025',
  '01/04/2025',
  '15/04/2025',
  '17/04/2025',
  '24/04/2025',
]

// Reservas existentes
const reservas = ref([
  {
    id: 1,
    fechaInicio: '17/04/25',
    fechaFin: '24/04/25',
    estado: 'Aprobado',
  },
  {
    id: 2,
    fechaInicio: '01/05/25',
    fechaFin: '05/05/25',
    estado: 'En revisión',
  },
  {
    id: 3,
    fechaInicio: '10/05/25',
    fechaFin: '15/05/25',
    estado: 'Denegado',
  },
])

// Estado del snackbar
const snackbar = reactive({
  show: false,
  message: '',
  color: 'success',
})

// Función para obtener color del estado
const getStatusColor = (estado) => {
  switch (estado) {
    case 'Aprobado':
      return 'success'
    case 'Denegado':
      return 'error'
    case 'En revisión':
      return 'warning'
    default:
      return 'grey'
  }
}

// Función para enviar solicitud
const submitRequest = () => {
  if (!form.desde || !form.hasta || !form.motivo) {
    snackbar.message = 'Por favor completa todos los campos'
    snackbar.color = 'error'
    snackbar.show = true
    return
  }

  // Agregar nueva reserva
  const newReserva = {
    id: Date.now(),
    fechaInicio: form.desde,
    fechaFin: form.hasta,
    estado: 'En revisión',
  }

  reservas.value.unshift(newReserva)

  // Limpiar formulario
  form.desde = ''
  form.hasta = ''
  form.motivo = ''

  snackbar.message = 'Solicitud enviada exitosamente'
  snackbar.color = 'success'
  snackbar.show = true
}

// Función para eliminar reserva
const deleteReserva = (id) => {
  if (confirm('¿Estás seguro de que quieres eliminar esta reserva?')) {
    const index = reservas.value.findIndex((r) => r.id === id)
    if (index > -1) {
      reservas.value.splice(index, 1)
      snackbar.message = 'Reserva eliminada'
      snackbar.color = 'info'
      snackbar.show = true
    }
  }
}
</script>

<style scoped>
.custom-tab {
  text-transform: none;
  font-weight: 500;
}

.active-tab-text {
  color: #ffc107;
  font-weight: 600;
  border-bottom: 2px solid #ffc107;
  padding-bottom: 4px;
}

.custom-select :deep(.v-field),
.custom-textarea :deep(.v-field) {
  border-radius: 8px;
  background-color: #f5f5f5;
}

.custom-select :deep(.v-field--focused),
.custom-textarea :deep(.v-field--focused) {
  background-color: white;
}

.custom-alert :deep(.v-alert__content) {
  padding: 8px 0;
}

:deep(.v-tabs-slider) {
  background-color: #ffc107;
}

:deep(.v-tab--selected) {
  color: #ffc107;
}
</style>
