export const environment = {
  baseUrlApi: 'http://localhost:5000',
  endPoint: {
    login: {
      crear: '/login',
    },
    anuncios: {
      listar: '/anuncios'
    },
    actividades: {
      obtenerPorUsuario: '/actividades/usuario',
      obtenerTodas: '/actividades/admin',
      obtenerPorId: '/actividades',
      obtenerAprobadas: '/actividades/aprobadas',
      crear: '/actividades',
      actualizar: '/actividades',
      eliminar: '/actividades',
    },
    quejas: {
      obtenerPorUsuario: '/quejas/usuario',
      listar: '/quejas',
      crear: '/quejas'
    },
    reconocimientos: {
      obtenerReconocimientos: '/reconocimientos',
      obtenerCumpleanos: '/cumpleaños'
    },
    permisos: {
      crear: '/api/permisos/salida',
      obtenerPorUsuario: '/api/permisos/salida/usuario'
    }
  },
}
