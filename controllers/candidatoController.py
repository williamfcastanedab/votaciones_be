from repositories.candidatoRepository import CandidatoRepository
from models.candidato import Candidato
from repositories.partidoPoliticoRepository import PartidoPoliticoRepository
from models.partidoPolitico import PartidoPolitico

class CandidatoController():
    def __init__(self):
        self.rC = CandidatoRepository()
        self.rPP = PartidoPoliticoRepository()

    def index(self):
        return self.rC.findAll()

    def create(self,infoCandidato):
        newCandidato = Candidato(infoCandidato)
        return self.rC.save(newCandidato)

    def show(self,ca_id):
        theCandidato = Candidato(self.rC.findById(ca_id))
        return theCandidato.__dict__

    def update(self,ca_id,infoCandidato):
        updateCandidato = Candidato(self.rC.findById(ca_id))
        updateCandidato.ca_partidoPolitico = infoCandidato["ca_partidoPolitico"]
        updateCandidato.ca_cedula = infoCandidato["ca_cedula"]
        updateCandidato.ca_nombres = infoCandidato["ca_nombres"]
        updateCandidato.ca_apellidos = infoCandidato["ca_apellidos"]
        updateCandidato.ca_resolucion = infoCandidato["ca_resolucion"]
        return self.rC.save(updateCandidato)

    def delete(self,ca_id):
        return self.rC.delete(ca_id)

    def asignarPartidoPolitico(self,ca_id,papo_id):
        candidatoActual = Candidato(self.rC.findById(ca_id))
        partidoPoliticoActual = PartidoPolitico(self.rPP.findById(papo_id))
        candidatoActual.partidoPolitico = partidoPoliticoActual
        return self.rC.save(candidatoActual)