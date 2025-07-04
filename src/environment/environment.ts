export const environment = {
  baseUrlApi: 'http://localhost:5000',
  endPoint: {
    login: {
      crear: '/login',
    },
    actividades: {
      obtenerPorUsuario: '/actividades/usuario',
      obtenerPorId: '/actividades',
      crear: '/actividades',
      actualizar: '/actividades',
      eliminar: '/actividades',
    },
  },
}
