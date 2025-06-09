<template>
  <div class="posts-container">
    <div class="user-info">
      <span class="status-dot"></span>
      <span>{{ nombreUsuario }}</span>
    </div>

    <div class="admin-buttons" v-if="rol === 'admin'">
      <button @click="mostrarPublicacion = true">Realizar una Publicación</button>
      <button @click="mostrarReconocimiento = true">Realizar un Reconocimiento</button>
    </div>

    <div v-if="mostrarPublicacion" class="modal">
      <h2>Realizar una Publicación</h2>
      <textarea v-model="nuevaPublicacion.descripcion" placeholder="Descripción"></textarea>
      <input type="file" @change="handleImagen" />
      <button @click="publicar">Publicar</button>
    </div>

    <div v-if="mostrarReconocimiento" class="modal">
      <h2>Realizar un Reconocimiento</h2>
      <input v-model="nuevoReconocimiento.alumno" placeholder="Alumno" />
      <textarea v-model="nuevoReconocimiento.descripcion" placeholder="Descripción"></textarea>
      <button @click="reconocer">Publicar</button>
    </div>

    <div class="post-card" v-for="post in posts" :key="post.id">
      <div class="post-date">{{ formatDate(post.fecha) }}</div>
      <div class="post-text">{{ post.descripcion }}</div>
      <img v-if="post.imagen" :src="post.imagen" alt="Imagen del anuncio" class="post-image" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

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
  const { data } = await axios.get('http://localhost:5000/publicaciones')
  posts.value = data
}

const formatDate = fecha => new Date(fecha).toLocaleDateString('es-ES', { day: '2-digit', month: 'long', year: 'numeric' })

const handleImagen = e => {
  nuevaPublicacion.value.imagen = e.target.files[0]
}

const publicar = async () => {
  const formData = new FormData()
  formData.append('descripcion', nuevaPublicacion.value.descripcion)
  formData.append('imagen', nuevaPublicacion.value.imagen)
  formData.append('id_usuario', JSON.parse(localStorage.getItem('usuario')).id)
  await axios.post('http://localhost:5000/publicaciones', formData)
  mostrarPublicacion.value = false
  cargarPublicaciones()
}

const reconocer = async () => {
  await axios.post('http://localhost:5000/reconocimientos', {
    alumno: nuevoReconocimiento.value.alumno,
    descripcion: nuevoReconocimiento.value.descripcion,
    id_usuario: JSON.parse(localStorage.getItem('usuario')).id
  })
  mostrarReconocimiento.value = false
}
</script>

<style scoped>
.posts-container {
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}
.user-info {
  background: #333;
  color: white;
  padding: 10px 20px;
  border-radius: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.status-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: green;
}
.admin-buttons {
  margin: 15px 0;
  display: flex;
  gap: 10px;
}
.modal {
  background: white;
  border: 1px solid #ccc;
  padding: 20px;
  width: 80%;
  max-width: 500px;
  border-radius: 10px;
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
