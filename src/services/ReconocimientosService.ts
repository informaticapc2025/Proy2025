import { environment } from '@/environment/environment'
import type { Reconocimiento } from '@/models/Reconocimiento'
import axios from 'axios'

export class ReconocimientosService {
  private urlObtenerReconocimientos: string

  constructor() {
    this.urlObtenerReconocimientos = `${environment.baseUrlApi}${environment.endPoint.reconocimientos.obtenerReconocimientos}`
  }

  async obtenerReconocimientos(): Promise<Reconocimiento[]> {
    return axios
      .get<Reconocimiento[]>(this.urlObtenerReconocimientos)
      .then((res: { data: Reconocimiento[] }) => res.data)
  }
}

export default new ReconocimientosService()
