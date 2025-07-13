import { environment } from '@/environment/environment'
import type { Queja } from '@/models/Queja'
import axios from 'axios'

export class QuejasService {
  private urlObtenerPorUsuario: string
  private urlCrear: string

  constructor() {
    this.urlObtenerPorUsuario = `${environment.baseUrlApi}${environment.endPoint.quejas.obtenerPorUsuario}`
    this.urlCrear = `${environment.baseUrlApi}${environment.endPoint.quejas.crear}`
  }

  async obtenerActividadesPorUsuario(
    usuarioId: number,
  ): Promise<Queja[]> {
    return axios
      .get<Queja[]>(`${this.urlObtenerPorUsuario}/${usuarioId}`)
      .then((res: { data: Queja[] }) => res.data)
  }

 async crearQueja(body: FormData): Promise<Queja> {
    return axios
      .post<Queja>(`${this.urlCrear}`, body, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(res => res.data);
  }
}

export default new QuejasService()
