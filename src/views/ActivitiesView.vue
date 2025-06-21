<template>
  <v-card class="contenido">
    <v-tabs v-model="tab" align-tabs="start" color="primary">
      <v-tab :value="1">Actividades</v-tab>
      <v-tab :value="2">Mis Solicitudes</v-tab>
    </v-tabs>

    <v-tabs-window v-model="tab">
      <v-tabs-window-item :value="1">
        <div class="text-right">
          <v-btn variant="outlined" class="mb-6" @click="openModalNuevo">Nueva Queja</v-btn>
        </div>
        <v-container fluid>
          <div v-for="(actividad, index) in actividades" :key="index" class="actividad-card">
            <div class="info">
              <div class="titulo-actividad">
                📌 <strong>{{ actividad.nombre }}</strong>
                <div class="fecha">({{ actividad.fecha }})</div>
              </div>
              <div class="descripcion">
                <small>Descripción</small><br />
                {{ actividad.descripcion || 'Sin descripción' }}
              </div>
            </div>
            <div class="tipo">RECREACIÓN</div>
            <div class="accion">
              <n-button type="warning" ghost>Acceder al formulario</n-button>
            </div>
          </div>
        </v-container>
      </v-tabs-window-item>

      <v-tabs-window-item :value="2">
        <v-container fluid>
          <div class="pa-4">
            <v-card class="elevation-2" style="border-radius: 12px">
              <v-data-table
                :headers="headers"
                :items="items"
                class="custom-table"
                hide-default-footer
                :items-per-page="-1"
              >
                <!-- Slot personalizado para la columna de código -->
                <template v-slot:item.codigo="{ item }">
                  <span class="text-body-2 font-weight-medium text-grey-darken-1">
                    {{ item.codigo }}
                  </span>
                </template>

                <!-- Slot personalizado para la columna de título -->
                <template v-slot:item.titulo="{ item }">
                  <span class="text-body-2 font-weight-medium">
                    {{ item.titulo }}
                  </span>
                </template>

                <!-- Slot personalizado para la columna de fecha -->
                <template v-slot:item.fecha="{ item }">
                  <span class="text-body-2 text-grey-darken-1">
                    {{ item.fecha }}
                  </span>
                </template>

                <!-- Slot personalizado para la columna de resumen -->
                <template v-slot:item.resumen="{ item }">
                  <span class="text-body-2 text-grey-darken-1">
                    {{ item.resumen }}
                  </span>
                </template>

                <!-- Slot personalizado para la columna de acciones -->
                <template v-slot:item.acciones="{ item }">
                  <v-menu>
                    <template v-slot:activator="{ props }">
                      <v-btn
                        icon="mdi-dots-horizontal"
                        variant="text"
                        size="small"
                        v-bind="props"
                        class="text-grey-darken-1"
                      ></v-btn>
                    </template>
                    <v-list density="compact">
                      <v-list-item @click="editItem(item)">
                        <v-list-item-title>
                          <v-icon size="small" class="me-2">mdi-pencil</v-icon>
                          Editar
                        </v-list-item-title>
                      </v-list-item>
                      <v-list-item @click="viewItem(item)">
                        <v-list-item-title>
                          <v-icon size="small" class="me-2">mdi-eye</v-icon>
                          Ver detalles
                        </v-list-item-title>
                      </v-list-item>
                      <v-list-item @click="deleteItem(item)" class="text-red">
                        <v-list-item-title>
                          <v-icon size="small" class="me-2">mdi-delete</v-icon>
                          Eliminar
                        </v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-menu>
                </template>
              </v-data-table>
            </v-card>

            <!-- Snackbar para mostrar mensajes -->
            <v-snackbar v-model="snackbar.show" :color="snackbar.color" timeout="3000">
              {{ snackbar.message }}
              <template v-slot:actions>
                <v-btn variant="text" @click="snackbar.show = false"> Cerrar </v-btn>
              </template>
            </v-snackbar>
          </div>
        </v-container>
      </v-tabs-window-item>
    </v-tabs-window>
  </v-card>
  <ModalActividades v-model="showModal" :item="selectedItem" />
</template>

<script setup>
import { ref, reactive } from 'vue'
import { NButton } from 'naive-ui'
import ModalActividades from './modal/ModalActividades.vue'
const tab = ref(1)
const actividades = [
  {
    nombre: 'Viaje a Chilcas',
    fecha: '03 abr - 07 abr',
    descripcion: 'Viaje académico y recreativo',
  },
  {
    nombre: 'Viaje a Chilcas',
    fecha: '03 abr - 07 abr',
    descripcion: 'Viaje académico y recreativo',
  },
  {
    nombre: 'Viaje a Chilca',
    fecha: '03 abr - 07 abr',
    descripcion: 'Viaje académico y recreativo',
  },
  {
    nombre: 'Viaje a Chilca',
    fecha: '03 abr - 07 abr',
    descripcion: '',
  },
]
const headers = [
  {
    title: 'Código',
    align: 'start',
    sortable: true,
    key: 'codigo',
    width: '100px',
  },
  {
    title: 'Título',
    align: 'start',
    sortable: true,
    key: 'titulo',
    width: '250px',
  },
  {
    title: 'Fecha',
    align: 'start',
    sortable: true,
    key: 'fecha',
    width: '150px',
  },
  {
    title: 'Resumen',
    align: 'start',
    sortable: false,
    key: 'resumen',
  },
  {
    title: 'Acciones',
    align: 'center',
    sortable: false,
    key: 'acciones',
    width: '100px',
  },
]
const items = ref([
  {
    id: 1,
    codigo: '0001',
    titulo: 'Visita a Chilca, descripcion importante',
    fecha: '(03 abr - 07 abr)',
    resumen:
      'Visita a Chilca, descripcion importante Visita a Chilca, descripcion importante. Esta es una descripción más detallada del evento.',
  },
  {
    id: 2,
    codigo: '0002',
    titulo: 'Reunión de seguimiento proyecto',
    fecha: '(10 abr - 12 abr)',
    resumen:
      'Reunión para revisar el progreso del proyecto y definir próximos pasos. Se discutieron los entregables pendientes.',
  },
  {
    id: 3,
    codigo: '0003',
    titulo: 'Capacitación equipo técnico',
    fecha: '(15 abr - 16 abr)',
    resumen:
      'Sesión de capacitación para el equipo técnico sobre nuevas herramientas y metodologías de trabajo.',
  },
  {
    id: 4,
    codigo: '0004',
    titulo: 'Evaluación de resultados Q1',
    fecha: '(20 abr - 22 abr)',
    resumen:
      'Evaluación trimestral de resultados y métricas de desempeño del primer quarter del año.',
  },
  {
    id: 5,
    codigo: '0005',
    titulo: 'Planificación estratégica',
    fecha: '(25 abr - 30 abr)',
    resumen:
      'Sesiones de planificación estratégica para definir objetivos y metas del próximo período.',
  },
])
const snackbar = reactive({
  show: false,
  message: '',
  color: 'success',
})
const showModal = ref(false)
const selectedItem = ref(null)

function openModal(item) {
  selectedItem.value = item
  showModal.value = true
}

function openModalNuevo() {
  console.log('Abrir modal para nueva actividad')
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

//Mis actividades
// Funciones para las acciones
const editItem = (item) => {
  snackbar.message = `Editando elemento: ${item.titulo}`
  snackbar.color = 'info'
  snackbar.show = true
  console.log('Editar:', item)
}

const viewItem = (item) => {
  snackbar.message = `Viendo detalles de: ${item.titulo}`
  snackbar.color = 'info'
  snackbar.show = true
  console.log('Ver:', item)
}

const deleteItem = (item) => {
  if (confirm(`¿Estás seguro de que quieres eliminar "${item.titulo}"?`)) {
    const index = items.value.findIndex((i) => i.id === item.id)
    if (index > -1) {
      items.value.splice(index, 1)
      snackbar.message = `Elemento eliminado: ${item.titulo}`
      snackbar.color = 'success'
      snackbar.show = true
    }
  }
}
</script>

<style scoped>
.actividades-wrapper {
  display: flex;
  gap: 20px;
  padding: 30px;
  background: url('/ruta/a/tu/fondo.png') no-repeat center;
  background-size: cover;
  min-height: 100vh;
  position: relative;
}

.perfil {
  position: absolute;
  top: 20px;
  left: 20px;
  background: #1e1e1e;
  color: white;
  padding: 8px 16px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  gap: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.estado {
  width: 10px;
  height: 10px;
  background: limegreen;
  border-radius: 50%;
}

.sidebar {
  width: 220px;
  margin-top: 100px;
}

.contenido {
  flex: 1;
  background: rgba(200, 210, 150, 0.3);
  padding: 20px;
  border-radius: 20px;
  margin-left: auto;
}

.titulo {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 20px;
}

.titulo .resaltado {
  color: #b28700;
  margin-right: 10px;
}

.actividad-card {
  display: flex;
  align-items: center;
  background: #f5f5f5;
  border-radius: 12px;
  padding: 15px 20px;
  margin-bottom: 16px;
  justify-content: space-between;
  box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
}

.info {
  flex: 1;
}

.titulo-actividad {
  font-size: 16px;
  font-weight: bold;
}

.fecha {
  font-size: 13px;
  color: #555;
}

.descripcion {
  font-size: 14px;
  margin-top: 5px;
}

.tipo {
  font-size: 12px;
  text-align: center;
  color: #555;
  width: 100px;
}

.accion {
  min-width: 160px;
  display: flex;
  justify-content: flex-end;
}

/*Mis actividades*/
.custom-table :deep(.v-data-table__wrapper) {
  border-radius: 12px;
}

.custom-table :deep(.v-data-table-header) {
  background-color: #f5f5f5;
}

.custom-table :deep(.v-data-table-header__content) {
  font-weight: 600;
  color: #424242;
}

.custom-table :deep(.v-data-table__td) {
  padding: 16px 12px;
  border-bottom: 1px solid #e0e0e0;
}

.custom-table :deep(.v-data-table__th) {
  padding: 16px 12px;
  font-size: 0.875rem;
  font-weight: 600;
  color: #616161;
}

.custom-table :deep(tbody tr:hover) {
  background-color: #f8f9fa;
}

.custom-table :deep(tbody tr:last-child td) {
  border-bottom: none;
}
</style>
