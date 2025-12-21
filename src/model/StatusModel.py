from database.AdapterDatabase import AdapterDatabase
from model.base.BaseModel import BaseModel

class StatusModel(BaseModel):

    table = "statuses"

    def __init__(self, id=None, name=None, color_hex=None, active=1):
        self.id = id
        self.name = name
        self.color_hex = color_hex
        self.active = active

    def criar_status(self, name, color_hex, active=1):
        # cria tudo necessario no atual obj para enviar para o banco
        self.name = name
        self.color_hex = color_hex
        self.active = active

        # conecta ao banco e insere o obj
        with AdapterDatabase() as db:
            db.insert(obj=self)

        # verifica se houve erro
        return True

    def get_all(self):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaStatus = db.select(obj=self)
        return listaStatus

    def get_by_id(self, id):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaStatus = db.select(obj=self, id=id)
        return listaStatus