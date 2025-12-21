from database.AdapterDatabase import AdapterDatabase
from model.base.BaseModel import BaseModel
from utils.logs import get_logger


logger = get_logger(__name__)


class TecnicaModel(BaseModel):

    table = "technicians"

    def __init__(self, id=None, name=None, active=1):
        self.id = id
        self.name = name
        self.active = active

    def criar_tecnica(self, name, active=1):
        # cria tudo necessario no atual obj para enviar para o banco
        self.name = name
        self.active = active

        # conecta ao banco e insere o obj
        logger.info("Criando técnico name=%s", name)
        with AdapterDatabase() as db:
            db.insert(obj=self)

        # verifica se houve erro
        logger.debug("Técnico criado com id=%s", self.id)
        return True

    def deletar_tecnica(self, id):
        #conecta ao banco e desativa o obj
        self.id = id
        logger.info("Desativando técnico id=%s", id)
        with AdapterDatabase() as db:
            db.desative_line(obj=self)

        #verifica se houve erro
        return True

    def get_all(self):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaTecnica = db.select(obj=self)
        return listaTecnica

    def get_by_id(self, id):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaTecnica = db.select(obj=self, id=id)
        return listaTecnica