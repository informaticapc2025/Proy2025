<template>
  <div class="posts-container">
    <div class="post-card" v-for="post in posts" :key="post.id">
      <div class="post-date">{{ currentDate }}</div>
      <div class="post-text">{{ post.text }}</div>
      <img v-if="post.image" :src="post.image" alt="Imagen del anuncio" class="post-image" />
    </div>
  </div>
</template>

<script>
export default {
  name: "PostsView",
  data() {
    return {
      currentDate: this.getFormattedDate(),
      posts: [
        {
          id: 1,
          text: "Se les informa a los estudiantes que el plato del día es Olluquito con Carne 😋🍴",
          image: "/images/Almuerzo1.png",
        },
        {
          id: 2,
          text: "Quisiéramos informarles que el día de mañana habrá corte de agua 💧 desde las 10 am hasta las 2 pm, por motivos de mantenimiento 👷🔧",
          image: null,
        },
        {
          id: 3,
          text: "Recuerda que puedes pedir información en el gimnasio de la UNMSM. Si eres alumnos sanmarquino y quieres inscribirte a la sala de pesas, o a otras actividades, debes ir a separar tu cupo un día antes de la fecha que quieras asistir, sugeto a disponibilidad de cupos. Cupos diarios limitados.",
          image: null,
        },
        {
        id: 4,
          text: `💐 ¡Feliz Día de la Madre! 💐
          Hoy rendimos homenaje a ese amor incondicional, a la fuerza que inspira y a la ternura que guía cada paso.
          Un saludo especial a todas las madres de la comunidad sanmarquina y del Perú, por ser ejemplo de valentía, sabiduría y entrega. Gracias por su inmenso aporte a la familia, a la sociedad y al país.
          ¡Que este día esté lleno de amor y reconocimiento por todo lo que son y todo lo que hacen!
          #DíaDeLaMadre`,
          image: "/images/Madre.jpg",
},
      ],
    };
  },
  methods: {
    getFormattedDate() {
      const date = new Date();
      const options = { day: '2-digit', month: 'long', year: 'numeric' };
      return date.toLocaleDateString('es-ES', options);
    }
  }
};
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

