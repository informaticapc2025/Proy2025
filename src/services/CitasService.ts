import { environment } from '@/environment/environment'
import type { Cita } from '@/models/Cita'
import axios from 'axios'

export class CitasService {
  private urlObtenerSolicitadasPorUsuario: string

  constructor() {
    this.urlObtenerSolicitadasPorUsuario = `${environment.baseUrlApi}${environment.endPoint.citas.obtenerSolicitadasPorUsuario}`
  }

  async obtenerCitasSolicitadasPorUsuario(usuarioId: number): Promise<Cita[]> {
    return axios
      .get<Cita[]>(`${this.urlObtenerSolicitadasPorUsuario}/${usuarioId}`)
      .then((res: { data: Cita[] }) => res.data)
  }
}

export default new CitasService()
