<template>
  <div class="actividades-wrapper">
    <!-- Panel lateral izquierdo -->
    <div class="sidebar-fijo">
      <UserCard />
      <SidebarMenu />
      <Salir />
    </div>

    <!-- Contenido principal -->
    <div class="contenido">
      <div class="titulo">
        <h2><span class="resaltado">Actividades</span> Mis solicitudes</h2>
      </div>

      <div v-for="(actividad, index) in actividades" :key="index" class="actividad-card">
        <div class="info">
          <div class="titulo-actividad">
            📌 <strong>{{ actividad.nombre }}</strong>
          </div>
          <div class="descripcion">
            <small>Descripción</small><br />
            {{ actividad.descripcion || 'Sin descripción' }}
          </div>
          <div class="fecha">({{ actividad.fecha }})</div>
        </div>
        <div class="tipo">RECREACIÓN</div>
        <div class="accion">
          <n-button type="warning" ghost>Acceder al formulario</n-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { NButton } from 'naive-ui'
import UserCard from '../components/layout/UserCard.vue'
import SidebarMenu from '../components/layout/SidebarMenu.vue'
import Salir from '../components/layout/Salir.vue'

const actividades = ref([
  { nombre: 'Viaje a Chilca', fecha: '03 abr - 07 abr', descripcion: 'Viaje académico y recreativo' },
  { nombre: 'Viaje a Chilca', fecha: '03 abr - 07 abr', descripcion: 'Viaje académico y recreativo' },
  { nombre: 'Viaje a Chilca', fecha: '03 abr - 07 abr', descripcion: 'Viaje académico y recreativo' },
  { nombre: 'Viaje a Chilca', fecha: '03 abr - 07 abr', descripcion: '' }
])
</script>

<style scoped>
.actividades-wrapper {
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
  color: #c69c00;
}

/* Tarjetas */
.actividad-card {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: white;
  border-radius: 10px;
  padding: 18px 25px;
  margin-bottom: 18px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

.info {
  flex: 1;
}

.titulo-actividad {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.descripcion {
  font-size: 14px;
  color: #333;
}

.fecha {
  font-size: 13px;
  color: #666;
  margin-top: 4px;
}

.tipo {
  font-size: 13px;
  color: #555;
  width: 110px;
  text-align: center;
}

.accion {
  display: flex;
  justify-content: flex-end;
  min-width: 180px;
}
</style>
