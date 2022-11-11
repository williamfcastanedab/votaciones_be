from models.votacion import Votacion
from models.candidato import Candidato
from models.resultados import Resultados
from models.partidoPolitico import PartidoPolitico
from repositories.votacionRepository import VotacionRepository
from repositories.candidatoRepository import CandidatoRepository
from repositories.resultadosRepository import ResultadosRepository
from repositories.partidoPoliticoRepository import PartidoPoliticoRepository

class VotacionController():
    def __init__(self):
        self.rV = VotacionRepository()
        self.rC = CandidatoRepository()
        self.rR = ResultadosRepository()
        self.rPP = PartidoPoliticoRepository()
    
    def index(self):
        return self.rV.findAll()

    def createVC(self,infoVotacion,ca_id,re_id):
        newVotacion = Votacion(infoVotacion)
        theCandidato = Candidato(self.rC.findById(ca_id))
        theResultados = Resultados(self.rR.findById(re_id))
        newVotacion.candidato = theCandidato
        newVotacion.resultados = theResultados
        return self.rV.save(newVotacion)

    def createVPP(self,infoVotacion,papo_id,re_id):
        newVotacion = Votacion(infoVotacion)
        thePartidoPolitico = PartidoPolitico(self.rC.findById(papo_id))
        theResultados = Resultados(self.rR.findById(re_id))
        newVotacion.partidoPolitico = thePartidoPolitico
        newVotacion.resultados = theResultados
        return self.rV.save(newVotacion)

    def show(self,vo_id):
        theVotacion = Votacion(self.rV.findById(vo_id))
        return theVotacion.__dict__

    def updateVC(self,vo_id,infoVotacion,ca_id,re_id):
        theVotacion = Votacion(self.rV.findById(vo_id))
        theCandidato = Candidato(self.rC.findById(ca_id))
        theResultados = Resultados(self.rR.findById(re_id))
        theVotacion.candidato = theCandidato
        theVotacion.resultados = theResultados
        return self.rV.save(theVotacion)

    def updateVPP(self,vo_id,infoVotacion,papo_id,re_id):
        theVotacion = Votacion(self.rV.findById(vo_id))
        thePartidoPolitico = PartidoPolitico(self.rC.findById(papo_id))
        theResultados = Resultados(self.rR.findById(re_id))
        theVotacion.partidoPolitico = thePartidoPolitico
        theVotacion.resultados = theResultados
        return self.rV.save(theVotacion)

    def delete(self,vo_id):
        return self.rV.delete(vo_id)