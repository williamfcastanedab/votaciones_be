from repositories.mesaRepository import MesaRepository
from models.mesa import Mesa

class MesaController():
    def __init__(self):
        self.mR = MesaRepository()

    def index(self):
        return self.mR.findAll()

    def create(self,infoMesa):
        newMesa = Mesa(infoMesa)
        return self.mR.save(newMesa)

    def show(self,me_id):
        theMesa = Mesa(self.mR.findById(me_id))
        return theMesa.__dict__

    def update(self,me_id,infoMesa):
        updateMesa = Mesa(self.mR.findById(me_id))
        updateMesa.me_numeroMesa = infoMesa["me_numeroMesa"]
        updateMesa.me_numeroCiudadanosInscritos = infoMesa["me_numeroCiudadanosInscritos"]
        return self.mR.save(updateMesa)

    def delete(self,me_id):
        return self.mR.delete(me_id)