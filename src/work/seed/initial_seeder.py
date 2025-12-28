# seed/initial_seeder.py
from work.seed.base import BaseSeeder
from model.StatusModel import StatusModel
from model.TipoModel import TipoModel
from model.TecnicaModel import TecnicaModel
from model.ClienteModel import ClienteModel
from utils.logs import get_logger

logger = get_logger(__name__)



class InitialDataSeeder(BaseSeeder):
    name = "initial_data"
    version = 1

    def run(self) -> None:
        if self.already_applied():
            print(f"[seed:{self.name}] Já aplicado (v{self.version})")
            return

        print(f"[seed:{self.name}] Inserindo dados iniciais")

        self._seed_statuses()
        self._seed_service_types()
        self._seed_technicians()
        self._seed_clients()

        self.mark_applied()
        print(f"[seed:{self.name}] Seed concluído com sucesso")

    def _reset_data(self) -> None:
        self.conn.execute("DELETE FROM statuses")
        self.conn.execute("DELETE FROM service_types")
        self.conn.execute("DELETE FROM technicians")
        self.conn.execute("DELETE FROM clients")

    def _seed_statuses(self):
        print("Inserindo statuses...")
        StatusModel().criar_status("Disponível", "#E0E0E0")
        print("  - Status: Disponível")
        StatusModel().criar_status("Agendado", "#4CAF50")
        print("  - Status: Agendado")
        StatusModel().criar_status("Cancelado", "#F44336")
        print("  - Status: Cancelado")
        StatusModel().criar_status("Reagendado", "#FF9800")
        print("  - Status: Reagendado")
        StatusModel().criar_status("Bloqueado", "#9E9E9E")
        print("  - Status: Bloqueado")

    def _seed_service_types(self):
        print("Inserindo tipos de serviço...")
        TipoModel().criar_tipo("Atendimento", None, None)
        print("  - Tipo: Atendimento")
        TipoModel().criar_tipo("Retorno", None, None)
        print("  - Tipo: Retorno")
        TipoModel().criar_tipo("Procedimento", None, None)
        print("  - Tipo: Procedimento")

    def _seed_technicians(self):
        print("Inserindo técnicos...")
        TecnicaModel().criar_tecnica("Técnico 1", 1)
        print("  - Técnico: Técnico 1")
        TecnicaModel().criar_tecnica("Técnico 2", 1)
        print("  - Técnico: Técnico 2")

    def _seed_clients(self):
        print("Inserindo clientes...")
        ClienteModel().criar_cliente("Cliente Demo 1", "C001")
        print("  - Cliente: Cliente Demo 1 (C001)")
        ClienteModel().criar_cliente("Cliente Demo 2", "C002")
        print("  - Cliente: Cliente Demo 2 (C002)")
