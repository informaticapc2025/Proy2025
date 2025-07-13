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
      crearSalida: '/api/permisos/salida',
      obtenerSalidaPorUsuario: '/api/permisos/salida/usuario',
      todasLasSalidas: '/api/permisos/salida/admin',
      crearAreaComun: '/api/permisos/area-comun',
      obtenerAreaComunPorUsuario: '/api/permisos/area-comun/usuario',
      todasLasAreaComun: '/api/permisos/area-comun/admin',
    },
    citas: {
      obtenerSolicitadasPorUsuario: '/citas/alumno'
    }
  },
}
