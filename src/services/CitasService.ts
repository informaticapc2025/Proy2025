import { environment } from '@/environment/environment'
import type { CitaAlumno, CitaAdmin } from '@/models/Cita'
import axios from 'axios'

export class CitasService {
  private urlObtenerSolicitadasPorUsuario: string
  private urlObtenerPendientes: string
  private urlObtenerCulminadas: string
  private urlConsultar: String

  constructor() {
    this.urlObtenerSolicitadasPorUsuario = `${environment.baseUrlApi}${environment.endPoint.citas.obtenerSolicitadasPorUsuario}`
    this.urlObtenerPendientes = `${environment.baseUrlApi}${environment.endPoint.citas.obtenerPendientes}`
    this.urlObtenerCulminadas = `${environment.baseUrlApi}${environment.endPoint.citas.obtenerCulminadas}`
    this.urlConsultar = `${environment.baseUrlApi}${environment.endPoint.citas.consultar}`
  }

  async obtenerCitasSolicitadasPorUsuario(usuarioId: number): Promise<CitaAlumno[]> {
    return axios
      .get<CitaAlumno[]>(`${this.urlObtenerSolicitadasPorUsuario}/${usuarioId}`)
      .then((res: { data: CitaAlumno[] }) => res.data)
  }

  async obtenerCitasPendientes(): Promise<CitaAdmin[]> {
    return axios
      .get<CitaAdmin[]>(this.urlObtenerPendientes)
      .then((res: { data: CitaAdmin[] }) => res.data)
  }

  async obtenerCitasCulminadas(): Promise<CitaAdmin[]> {
    return axios
      .get<CitaAdmin[]>(this.urlObtenerCulminadas)
      .then((res: { data: CitaAdmin[] }) => res.data)
  }

  async consultarCita(citaId: number): Promise<CitaAdmin[]> {
    return axios
      .get<CitaAdmin[]>(`${this.urlConsultar}/${citaId}`)
      .then((res: { data: CitaAdmin[] }) => res.data)
  }
}

export default new CitasService()
