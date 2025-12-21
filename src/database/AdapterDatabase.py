from .ConectorSQLite import ConectorSQLite
from utils.path import get_data_path

class AdapterDatabase:
    '''
    Classe que fornece uma interface para interagir com o banco de dados.
    '''

    # Inicializa o adaptador com o caminho do banco de dados
    def __init__(self, db_path = get_data_path("database/database.db")):
        self.conector = ConectorSQLite(db_path)

    # Implementa o protocolo de contexto conectando com o banco de dados
    def __enter__(self):
        self.conector.connect()
        return self

    # Implementa o protocolo de contexto desconectando do banco de dados
    # com rollback ou commit caso exista erro
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.conector.conn.rollback()
        else:
            self.conector.conn.commit()
        self.conector.close()

    '''
    Métodos para interagir com o banco de dados
    '''

    # Desativa uma linha mantendo histórico dos objetos
    def desative_line(self, obj):
        self.conector.desative_line(obj)

    # Reativa uma linha
    def ative_line(self, obj):
        self.conector.ative_line(obj)

    # Seleciona uma linha do banco de dados
    def select(self, obj, id=None):
        return self.conector.select(obj, id)

    # Insere uma linha no banco de dados
    def insert(self, obj):
        return self.conector.insert(obj)

    # Atualiza uma linha no banco de dados
    def update(self, obj):
        self.conector.update(obj)
