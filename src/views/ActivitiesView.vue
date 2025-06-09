<template>
  <div class="actividades-wrapper">

    <div class="contenido">
      <div class="titulo">
        <h2><span class="resaltado">Actividades</span> Mis solicitudes</h2>
      </div>


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
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { NButton } from 'naive-ui'

const actividades = ref([
  {
    nombre: 'Viaje a Chilca',
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
    descripcion: 'Viaje académico y recreativo',
  },
  {
    nombre: 'Viaje a Chilca',
    fecha: '03 abr - 07 abr',
    descripcion: '',
  }
])
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
  box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
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
</style>
