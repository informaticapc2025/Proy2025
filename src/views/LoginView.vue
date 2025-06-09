<template>
  <div class="login-wrapper">
    <div class="login-image">
      <img src="../assets/pngs/login.png" alt="Residencia Universitaria" />
    </div>
    <div class="login-form">
      <h2>Iniciar Sesión</h2>
      <input v-model="correo" type="text" placeholder="Correo" />
      <input v-model="contraseña" type="password" placeholder="Contraseña" />
      <button @click="iniciarSesion">Ingresar</button>
      <img src="../assets/OGBU-logo.png" alt="Logo GBU" class="logo" />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const correo = ref('')
const contraseña = ref('')
const router = useRouter()

const iniciarSesion = async () => {
  try {
    // 👇 Imprimir en consola para debug
    console.log("Correo:", correo.value)
    console.log("Contraseña:", contraseña.value)

    const { data } = await axios.post('http://localhost:5000/login', {
      correo: correo.value.trim(),         
      contraseña: contraseña.value.trim()  
    }, {
      headers: {
        'Content-Type': 'application/json'
      }
    })

    router.push('/anuncios')
  } catch (error) {
    alert('Credenciales inválidas')
  }
}
</script>


<style scoped>
.login-wrapper {
  display: flex;
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.login-image {
  flex: 2;
}

.login-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.login-form {
  flex: 1;
  background-color: #c5c5b2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 50px 30px;
  position: relative;
}

.login-form h2 {
  font-weight: bold;
  font-size: 20px;
  margin-bottom: 30px;
  color: white;
  align-self: flex-start;
}

.login-form input {
  margin-bottom: 20px;
  padding: 10px;
  font-size: 16px;
  width: 100%;
  border: none;
  border-radius: 5px;
  background-color: #e9e9e9;
}

.login-form button {
  background-color: #333;
  color: white;
  border: none;
  padding: 10px;
  font-size: 16px;
  width: 100%;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}

.login-form button:hover {
  background-color: #555;
}

.logo {
  position: absolute;
  bottom: 30px;
  right: 30px;
  width: 120px;
}
</style>
