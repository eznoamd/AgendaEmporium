from database.AdapterDatabase import AdapterDatabase
from model.base.BaseModel import BaseModel
from utils.logs import get_logger


logger = get_logger(__name__)


class TipoModel(BaseModel):

    table = "service_types"

    def __init__(self, id=None, name=None, duration=None, filters=None, active=1):
        self.id = id
        self.name = name
        self.duration = duration 
        self.filters = filters
        self.active = active

    def criar_tipo(self, name, duration, filters):
        # cria tudo necessario no atual obj para enviar para o banco
        self.name = name
        self.duration = duration
        self.filters = filters
        self.active = 1

        # conecta ao banco e insere o obj
        logger.info("Criando tipo de serviço name=%s", name)
        with AdapterDatabase() as db:
            db.insert(obj=self)

        logger.debug("Tipo de serviço criado com id=%s", self.id)
        return True
    
    def deletar_tipo(self, id):
        # conecta ao banco e deleta o obj
        self.id = id
        logger.info("Desativando tipo de serviço id=%s", id)
        with AdapterDatabase() as db:
            db.desative_line(obj=self)

        # verifica se houve erro
        return True
    
    def get_all(self):
        #conecta ao banco e pega toda a tabela
        logger.debug("Buscando todos os tipos de serviço")
        with AdapterDatabase() as db:
            listaTipo = db.select(obj=self)
        return listaTipo
    
    '''
    Isso aqui em baixo
    '''
    def get_by_id(self, id):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaTipo = db.select(obj=self, id=id)
        return listaTipo

