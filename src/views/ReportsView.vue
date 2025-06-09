<template>
  <div class="quejas-wrapper">
    <!-- Panel lateral fijo -->
    <div class="sidebar-fijo">
      <UserCard />
      <SidebarMenu />
      <Salir />
    </div>

    <!-- Contenido principal -->
    <div class="contenido">
      <div class="titulo">
        <h2><span class="resaltado">Quejas</span> Mis reportes</h2>
      </div>

      <div class="tabla-contenedor">
        <n-space vertical :size="12">
          <n-space class="botones">
            <n-button @click="sortName">Ordenar por Nombre</n-button>
            <n-button @click="filterAddress">Filtrar por Dirección (London)</n-button>
            <n-button @click="clearFilters">Limpiar Filtros</n-button>
            <n-button @click="clearSorter">Limpiar Orden</n-button>
          </n-space>
          <n-data-table
            ref="dataTableInst"
            :columns="columns"
            :data="data"
            :pagination="pagination"
          />
        </n-space>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { NButton, NSpace, NDataTable } from 'naive-ui'
import UserCard from '../components/layout/UserCard.vue'
import SidebarMenu from '../components/layout/SidebarMenu.vue'
import Salir from '../components/layout/Salir.vue'

const columns = [
  { title: 'Nombre', key: 'name' },
  { title: 'Edad', key: 'age', sorter: (a, b) => a.age - b.age },
  {
    title: 'Nota Chino',
    key: 'chinese',
    sorter: { compare: (a, b) => a.chinese - b.chinese, multiple: 3 },
  },
  {
    title: 'Nota Matemáticas',
    key: 'math',
    sorter: { compare: (a, b) => a.math - b.math, multiple: 2 },
  },
  {
    title: 'Nota Inglés',
    key: 'english',
    sorter: { compare: (a, b) => a.english - b.english, multiple: 1 },
  },
  {
    title: 'Dirección',
    key: 'address',
    filterOptions: [
      { label: 'London', value: 'London' },
      { label: 'New York', value: 'New York' },
    ],
    filter: (value, row) => row.address.includes(value),
  },
]

const data = [
  { key: 0, name: 'John Brown', age: 32, address: 'New York No. 1', chinese: 98, math: 60, english: 70 },
  { key: 1, name: 'Jim Green', age: 42, address: 'London No. 1', chinese: 98, math: 66, english: 89 },
  { key: 2, name: 'Joe Black', age: 32, address: 'Sidney No. 1', chinese: 98, math: 66, english: 89 },
  { key: 3, name: 'Jim Red', age: 32, address: 'London No. 2', chinese: 88, math: 99, english: 89 },
]

const dataTableInst = ref(null)
const pagination = ref({ pageSize: 5 })

const filterAddress = () => {
  dataTableInst.value?.filter({ address: ['London'] })
}
const sortName = () => {
  dataTableInst.value?.sort('name', 'ascend')
}
const clearFilters = () => {
  dataTableInst.value?.filter(null)
}
const clearSorter = () => {
  dataTableInst.value?.sort(null)
}
</script>

<style scoped>
.quejas-wrapper {
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

/* Contenido principal */
.contenido {
  flex: 1;
  background: rgba(217, 217, 217, 0.3);
  backdrop-filter: blur(8px);
  margin-left: 20px;
  padding: 25px 30px;
  border-radius: 15px;
  width: 100%;
}

.titulo {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 25px;
  color: white;
  display: flex;
  align-items: center;
  gap: 10px;
}

.titulo .resaltado {
  color: #9e7c00;
}

.botones {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
}

.tabla-contenedor {
  background-color: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.n-data-table,
.n-data-table-tbody {
  background-color: transparent;
}
</style>
