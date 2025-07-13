import { environment } from '@/environment/environment'
import type { Reconocimiento, Cumpleanos } from '@/models/Reconocimiento'
import axios from 'axios'

export class ReconocimientosService {
  private urlObtenerReconocimientos: string
  private urlObtenerCumpleanos: string

  constructor() {
    this.urlObtenerReconocimientos = `${environment.baseUrlApi}${environment.endPoint.reconocimientos.obtenerReconocimientos}`
    this.urlObtenerCumpleanos = `${environment.baseUrlApi}${environment.endPoint.reconocimientos.obtenerCumpleanos}`
  }

  async obtenerReconocimientos(): Promise<Reconocimiento[]> {
    return axios
      .get<Reconocimiento[]>(this.urlObtenerReconocimientos)
      .then((res: { data: Reconocimiento[] }) => res.data)
  }

  async obtenerCumpleanos(): Promise<Cumpleanos[]> {
    return axios
      .get<Cumpleanos[]>(this.urlObtenerCumpleanos)
      .then((res: { data: Cumpleanos[] }) => res.data)
  }
}

export default new ReconocimientosService()
