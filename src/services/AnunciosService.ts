import { environment } from '@/environment/environment'
import axios from 'axios'
import type { Anuncio } from '@/models/Anuncio'

export class AnunciosService {
  private urlListar: string

  constructor() {
    this.urlListar = `${environment.baseUrlApi}${environment.endPoint.anuncios.listar}`
  }

  async listarAnuncios(): Promise<Anuncio[]> {
    return axios
      .get<Anuncio[]>(this.urlListar)
      .then((res: { data: Anuncio[] }) => res.data)
  }
}

export default new AnunciosService()