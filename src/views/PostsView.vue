<template>
  <div class="posts-container">
    <div class="post-card" v-for="post in posts" :key="post.id">
      <div class="post-date">{{ formatDate(post.fecha_publicacion) }}</div>
      <div class="post-text">{{ post.descripcion }}</div>
      <img v-if="post.imagen" :src="post.imagen" alt="Imagen del anuncio" class="post-image" />
    </div>
  </div>
</template>

<script>
import AnunciosService from '@/services/AnunciosService'

export default {
  name: 'PostsView',
  data() {
    return {
      posts: [],
    }
  },
  methods: {
    formatDate(dateStr) {
      const date = new Date(dateStr)
      const options = { day: '2-digit', month: 'long', year: 'numeric' }
      return date.toLocaleDateString('es-ES', options)
    },
    async fetchPosts() {
      try {
        this.posts = await AnunciosService.listarAnuncios()
      } catch (error) {
        console.error('Error al obtener anuncios:', error)
      }
    },
  },
  mounted() {
    this.fetchPosts()
  },
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
  font-weight: normal;
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
