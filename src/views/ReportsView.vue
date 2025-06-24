<template>
  <div class="about">
    <h1>Mis reportes</h1>
  </div>
  <div style="background-color: rgba(184, 186, 163, 0.85); width: 95%; padding: 20px">
    <!-- <v-select
      v-model="selectedAddress"
      :items="addressOptions"
      label="Filtrar por dirección"
      clearable
      style="max-width: 300px; margin-bottom: 16px"
    ></v-select> -->
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
    <ModalQueja v-model="showModal" :item="selectedItem" />
  </div>
</template>
<script>
import ModalQueja from './modal/ModalQueja.vue'

export default {
  name: 'ReportsView',
  components: { ModalQueja },
  data() {
    return {
      selectedAddress: null,
      showModal: false,
      selectedItem: null,
      data: [
        {
          numero: 'UNMSM-43255',
          asunto: 'Me robaron mi espejo dentro de mi cuarto',
          motivo: 'Robo',
          fecha: '15/03/2025',
          estado: 'Recibido',
        },
        {
          numero: 'UNMSM-69873',
          asunto: 'Rompieron Macetas del parque',
          motivo: 'Destrucción de bienes',
          fecha: '12/03/2025',
          estado: 'Pendiente',
        },
        {
          numero: 'UNMSM-96342',
          asunto: 'Ruidos molestos en la residencia',
          motivo: 'Ruido excesivo',
          fecha: '12/03/2025',
          estado: 'Pendiente',
        },
        {
          numero: 'UNMSM-78521',
          asunto: 'Vidrios rotos en el aula 302',
          motivo: 'Destrucción de bienes',
          fecha: '11/03/2025',
          estado: 'En revisión',
        },
        {
          numero: 'UNMSM-54789',
          asunto: 'Basura acumulada en la biblioteca',
          motivo: 'Falta de limpieza',
          fecha: '10/03/2025',
          estado: 'En proceso',
        },
        {
          numero: 'UNMSM-23874',
          asunto: 'Mal funcionamiento de luces en pasillo',
          motivo: 'Infraestructura dañada',
          fecha: '09/03/2025',
          estado: 'Resuelto',
        },
        {
          numero: 'UNMSM-87456',
          asunto: 'Robo de bicicleta en el estacionamiento',
          motivo: 'Robo',
          fecha: '08/03/2025',
          estado: 'Cerrado',
        },
        {
          numero: 'UNMSM-65231',
          asunto: 'Fuga de agua en los baños del pabellón',
          motivo: 'Daño estructural',
          fecha: '07/03/2025',
          estado: 'En revisión',
        },
      ],
    }
  },
  computed: {
    filteredData() {
      if (!this.selectedAddress) return this.data
      return this.data.filter((item) => item.address.includes(this.selectedAddress))
    },
  },
  methods: {
    openModal(item) {
      console.log('Opening modal for item:')
      this.selectedItem = item
      this.showModal = true
    },

    openModalNuevo() {
      this.selectedItem = {
        numero: '',
        asunto: '',
        motivo: '',
        fecha: '',
        estado: '',
        descripcion: '',
      }
      this.showModal = true
    },
  },
}
</script>
<style>
.n-data-table,
.n-data-table-tbody {
  background-color: transparent;
}
</style>
