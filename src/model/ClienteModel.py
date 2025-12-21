from database.AdapterDatabase import AdapterDatabase
from model.base.BaseModel import BaseModel
from utils.logs import get_logger


logger = get_logger(__name__)


class ClienteModel(BaseModel):

    table = "clients"

    def __init__(self, id=None, name=None, code=None, active=1):
        self.id = id
        self.name = name
        self.code = code
        self.active = active

    def criar_cliente(self, name, code):
        # Cria tudo necessario no atual obj para enviar para o banco
        self.name = name
        self.code = code
        self.active = 1

        # Conecta ao banco e insere o obj
        logger.info("Criando cliente name=%s code=%s", name, code)
        with AdapterDatabase() as db:
            db.insert(obj=self)

        logger.debug("Cliente criado com id=%s", self.id)
        return True

    def get_all(self):
        # Conecta ao banco e pega toda a tabela
        logger.debug("Buscando todos os clientes")
        with AdapterDatabase() as db:
            listaCliente = db.select(obj=self)
        logger.debug("%d clientes encontrados", len(listaCliente))
        return listaCliente

    def get_by_id(self, id):
        # Conecta ao banco e pega toda a tabela
        logger.debug("Buscando cliente por id=%s", id)
        with AdapterDatabase() as db:
            listaCliente = db.select(obj=self, id=id)
        return listaCliente