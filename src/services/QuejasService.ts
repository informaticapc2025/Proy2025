import { environment } from '@/environment/environment'
import type { Queja } from '@/models/Queja'
import axios from 'axios'

export class QuejasService {
  private urlObtenerPorUsuario: string
  private urlObtenerPorId: string
  private urlCrear: string
  private urlActualizar: string
  private urlEliminar: string

  constructor() {
    this.urlObtenerPorUsuario = `${environment.baseUrlApi}${environment.endPoint.actividades.obtenerPorUsuario}`
    this.urlObtenerPorId = `${environment.baseUrlApi}${environment.endPoint.actividades.obtenerPorId}`
    this.urlCrear = `${environment.baseUrlApi}${environment.endPoint.actividades.crear}`
    this.urlActualizar = `${environment.baseUrlApi}${environment.endPoint.actividades.actualizar}`
    this.urlEliminar = `${environment.baseUrlApi}${environment.endPoint.actividades.eliminar}`
  }

  obtenerActividadesPorUsuario(
    usuarioId: number,
    // nombreActividad?: string
  ): Promise<Queja[]> {
    // if (nombreActividad) {
    //   params['nombreActividad'] = nombreActividad;
    // }

    return axios
      .get<Queja[]>(`${this.urlObtenerPorUsuario}/${usuarioId}`)
      .then((res: { data: Queja[] }) => res.data)
  }

  //   obtenerActividadPorId(id: number): Promise<Queja> {
  //     return axios
  //       .get<Queja>(`${this.urlObtenerPorId}/${id}`)
  //       .then(res => res.data);
  //   }

  //   crearActividad(body: Partial<Queja>): Promise<Queja> {
  //     return axios
  //       .post<Queja>(`${this.urlCrear}`, body)
  //       .then(res => res.data);
  //   }

  //   actualizarActividad(id: number, body: Partial<Queja>): Promise<Queja> {
  //     return axios
  //       .put<Queja>(`${this.urlActualizar}/${id}`, body)
  //       .then(res => res.data);
  //   }

  //   eliminarActividad(id: number): Promise<void> {
  //     return axios
  //       .delete(`${this.urlEliminar}/${id}`)
  //       .then(() => undefined);
  //   }
}

export default new QuejasService()
