import { environment } from '@/environment/environment'
import type { Permiso } from '@/models/Permiso'
import axios from 'axios'

export class PermisosService {
  private urlCrearSalida: string
  private urlObtenerPorUsuario: string

  constructor() {
    this.urlCrearSalida = `${environment.baseUrlApi}${environment.endPoint.permisos.crear}`
    this.urlObtenerPorUsuario = `${environment.baseUrlApi}${environment.endPoint.permisos.obtenerPorUsuario}`
  }

  async crearPermiso(body: Partial<Permiso>): Promise<Permiso> {
    return axios
      .post<Permiso>(this.urlCrearSalida, body)
      .then(res => res.data);
  }

  async obtenerPermisosPorUsuario(
    usuarioId: number,
  ): Promise<Permiso[]> {
    return axios
      .get<Permiso[]>(`${this.urlObtenerPorUsuario}/${usuarioId}`)
      .then((res: { data: Permiso[] }) => res.data)
  }
}

export default new PermisosService()
