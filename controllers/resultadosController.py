from repositories.resultadosRepository import ResultadosRepository
from models.resultados import Resultados

from repositories.mesaRepository import MesaRepository
from models.mesa import Mesa
        
class ResultadosController():
    def __init__(self):
        self.rR = ResultadosRepository()
        self.rM = MesaRepository()

    def index(self):
        return self.rR.findAll()

    def create(self,infoResultados):
        newResultados = Resultados(infoResultados)
        return self.rR.save(newResultados)

    def show(self,re_id):
        theResultados = Resultados(self.rR.findById(re_id))
        return theResultados.__dict__

    def update(self,re_id,infoResultados):
        updateResultados = Resultados(self.rR.findById(re_id))
        updateResultados.re_numeroVotos = infoResultados["re_numeroVotos"]
        updateResultados.re_mesa = infoResultados["re_mesa"]
        return self.rR.save(updateResultados)

    def delete(self,re_id):
        return self.rR.delete(re_id)

    def asignarMesa(self,re_id,me_id):
        resultadosActual = Resultados(self.rR.findById(re_id))
        mesaActual = Mesa(self.rM.findById(me_id))
        resultadosActual.mesa = mesaActual
        return self.rR.save(resultadosActual)