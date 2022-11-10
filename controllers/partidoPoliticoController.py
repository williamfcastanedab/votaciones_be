from repositories.partidoPoliticoRepository import PartidoPoliticoRepository
from models.partidoPolitico import PartidoPolitico
        
class PartidoPoliticoController():
    def __init__(self):
        self.rPP = PartidoPoliticoRepository()

    def index(self):
        return self.rPP.findAll()

    def create(self,infoPartidoPolitico):
        newPartidoPolitico = PartidoPolitico(infoPartidoPolitico)
        return self.rPP.save(newPartidoPolitico)

    def show(self,papo_id):
        thePartidoPolitico = PartidoPolitico(self.rPP.findById(papo_id))
        return thePartidoPolitico.__dict__

    def update(self,papo_id,infoPartidoPolitico):
        updatePartidoPolitico = PartidoPolitico(self.rPP.findById(papo_id))
        updatePartidoPolitico.papo_nombrePP = infoPartidoPolitico["papo_nombrePP"]
        updatePartidoPolitico.papo_lemaPP = infoPartidoPolitico["papo_lemaPP"]
        return self.rPP.save(updatePartidoPolitico)

    def delete(self,papo_id):
        return self.rPP.delete(papo_id)