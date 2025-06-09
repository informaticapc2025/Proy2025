<template>
  <div class="layout-wrapper">
    <!-- Panel izquierdo fijo -->
    <div class="sidebar-fijo">
      <UserCard />
      <SidebarMenu />
      <div class="admin-buttons" v-if="rol === 'admin'">
        <button class="admin-button" @click="mostrarPublicacion = true">Realizar una Publicación</button>
        <button class="admin-button" @click="mostrarReconocimiento = true">Realizar un Reconocimiento</button>
      </div>
      <Salir />
    </div>

    <!-- Panel derecho fijo -->
    <div class="derecha-fija">
      <img src="/src/assets/OGBU-logo.png" class="logo" />
      <CelebrationCard />
      <RecognitionCard />
    </div>

    <!-- Contenido scrollable -->
    <div class="contenido-scroll">
      <div class="posts-container">
        <div class="post-card" v-for="post in posts" :key="post.id">
          <div class="post-date">{{ formatDate(post.fecha_publicacion) }}</div>
          <div class="post-text">{{ post.descripcion }}</div>
          <img v-if="post.imagen" :src="post.imagen" alt="Imagen del anuncio" class="post-image" />
        </div>
      </div>
    </div>

    <!-- Modal publicación -->
    <div v-if="mostrarPublicacion" class="modal">
      <button class="close-btn" @click="mostrarPublicacion = false">&times;</button>
      <h2>Realizar una Publicación</h2>
      <textarea v-model="nuevaPublicacion.descripcion" placeholder="Descripción"></textarea>
      <input type="file" @change="handleImagen" />
      <button class="publicar" @click="publicar">Publicar</button>
    </div>

    <!-- Modal reconocimiento -->
    <div v-if="mostrarReconocimiento" class="modal">
      <button class="close-btn" @click="mostrarReconocimiento = false">&times;</button>
      <h2>Realizar un Reconocimiento</h2>
      <input v-model="nuevoReconocimiento.alumno" placeholder="Alumno" />
      <textarea v-model="nuevoReconocimiento.descripcion" placeholder="Descripción"></textarea>
      <button class="publicar" @click="reconocer">Publicar</button>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

import UserCard from '../components/layout/UserCard.vue'
import SidebarMenu from '../components/layout/SidebarMenu.vue'
import CelebrationCard from '../components/layout/CelebrationCard.vue'
import RecognitionCard from '../components/layout/RecognitionCard.vue'
import Salir from '../components/layout/Salir.vue'

const posts = ref([])
const nombreUsuario = ref('')
const rol = ref('')
const mostrarPublicacion = ref(false)
const mostrarReconocimiento = ref(false)

const nuevaPublicacion = ref({ descripcion: '', imagen: null })
const nuevoReconocimiento = ref({ alumno: '', descripcion: '' })

onMounted(async () => {
  const user = JSON.parse(localStorage.getItem('usuario'))
  if (user) {
    nombreUsuario.value = user.nombre
    rol.value = user.rol
  }
  cargarPublicaciones()
})

const cargarPublicaciones = async () => {
  const { data } = await axios.get('http://localhost:5000/anuncios')
  posts.value = data
}

const formatDate = fecha => {
  return new Date(fecha).toLocaleDateString('es-PE', {
    timeZone: 'America/Lima',
    day: '2-digit',
    month: 'long',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}






const handleImagen = e => {
  nuevaPublicacion.value.imagen = e.target.files[0]
}

const publicar = async () => {
  if (!nuevaPublicacion.value.descripcion.trim()) {
    alert('Por favor, complete la descripción.')
    return
  }
  const formData = new FormData()
  formData.append('descripcion', nuevaPublicacion.value.descripcion)
  formData.append('imagen', nuevaPublicacion.value.imagen)
  formData.append('id_usuario', JSON.parse(localStorage.getItem('usuario')).id)
  await axios.post('http://localhost:5000/anuncios', formData, {
  headers: {
    'Content-Type': 'multipart/form-data'
  }
  })

  mostrarPublicacion.value = false
  cargarPublicaciones()
}

const reconocer = async () => {
  if (!nuevoReconocimiento.value.alumno.trim() || !nuevoReconocimiento.value.descripcion.trim()) {
    alert('Por favor, complete todos los campos.')
    return
  }
  await axios.post('http://localhost:5000/reconocimientos', {
    alumno: nuevoReconocimiento.value.alumno,
    descripcion: nuevoReconocimiento.value.descripcion,
    id_usuario: JSON.parse(localStorage.getItem('usuario')).id
  })
  mostrarReconocimiento.value = false
}
</script>

<style scoped>
.layout-wrapper {
  display: flex;
  background: url('../assets/fondo.png') no-repeat center center fixed;
  background-size: cover;
  position: relative;
}

/* Panel izquierdo */
.sidebar-fijo {
  position: fixed;
  left: 0;
  top: 0;
  bottom: 0;
  width: 15%;
  background-color: transparent;
  padding: 20px;
  z-index: 100;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

/* Panel derecho */
.derecha-fija {
  position: fixed;
  right: 0;
  top: 0;
  bottom: 0;
  width: 25%;
  background-color: transparent;
  padding: 20px;
  z-index: 100;
}

/* Contenido scrollable */
.contenido-scroll {
  margin-left: 30%;
  margin-right: 25%;
  padding: 20px;
}



/* Posts */
.posts-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

/* Botones admin */
.admin-buttons {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
  align-items: start;
}

.admin-button {
  background-color: #f1f1d1;
  border: none;
  padding: 10px;
  width: 100%;
  text-align: left;
  border-radius: 10px;
  cursor: pointer;
  font-weight: bold;
}

.admin-button:hover {
  background-color: #e1e1c1;
}

/* Modal */
.modal {
  background: white;
  border: 1px solid #ccc;
  padding: 20px;
  width: 80%;
  max-width: 500px;
  border-radius: 10px;
  position: absolute;
  top: 100px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 999;
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 15px;
  background: none;
  border: none;
  font-size: 24px;
  cursor: pointer;
}

.publicar {
  background-color: #f0b400;
  border: none;
  padding: 10px 15px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  color: #333;
  margin-top: 10px;
}

.post-card {
  background-color: #eaf0e6;
  border-radius: 15px;
  padding: 15px;
  max-width: 600px;
  width: 90%;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.post-date {
  font-size: 0.9rem;
  color: #686868;
  margin-bottom: 8px;
}

.post-text {
  font-size: 1rem;
  color: #333;
  margin-bottom: 10px;
  white-space: pre-line;
}

.post-image {
  display: block;
  margin: 0 auto;
  width: 100%;
  max-width: 450px;
  border-radius: 10px;
  margin-top: 10px;
}

</style>

<style>
html, body {
  height: 100%;
  overflow-y: auto;
  margin: 0;
  scrollbar-width: none;  
  -ms-overflow-style: none;  
}

body::-webkit-scrollbar {
  width: 0px; 
  background: transparent;
}
</style>

