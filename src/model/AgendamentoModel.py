from database.AdapterDatabase import AdapterDatabase
from model.base.BaseModel import BaseModel
from utils.logs import get_logger


logger = get_logger(__name__)


class AgendamentoModel(BaseModel):

    table = "appointments"

    def __init__(
        self,
        id=None,
        date=None,
        start_time=None,
        end_time=None,
        status_id=None,
        technician_id=None,
        client_id=None,
        service_type_id=None,
        notes=None,
        rescheduled=0,
        active=1,
        created_at=None,
        updated_at=None,
    ):
        self.id = id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.status_id = status_id
        self.technician_id = technician_id
        self.client_id = client_id
        self.service_type_id = service_type_id
        self.notes = notes
        self.rescheduled = rescheduled
        self.active = active
        self.created_at = created_at
        self.updated_at = updated_at

    def criar_agendamento(
        self,
        date,
        start_time,
        end_time,
        status_id,
        technician_id,
        client_id=None,
        service_type_id=None,
        notes=None,
    ):
        # cria tudo necessario no atual obj para enviar para o banco
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.status_id = status_id
        self.technician_id = technician_id
        self.client_id = client_id
        self.service_type_id = service_type_id
        self.notes = notes
        self.rescheduled = 0
        self.active = 1

        # conecta ao banco e insere o obj
        logger.info(
            "Criando agendamento date=%s start=%s end=%s status_id=%s technician_id=%s",
            date,
            start_time,
            end_time,
            status_id,
            technician_id,
        )
        with AdapterDatabase() as db:
            db.insert(obj=self)

        # verifica se houve erro
        logger.debug("Agendamento criado com id=%s", self.id)
        return True

    def get_all(self):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaAgendamento = db.select(obj=self)
        return listaAgendamento

    def get_by_id(self, id):
        #conecta ao banco e pega toda a tabela
        with AdapterDatabase() as db:
            listaAgendamento = db.select(obj=self, id=id)
        return listaAgendamento

