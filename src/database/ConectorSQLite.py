import sqlite3
from utils.logs import get_logger

logger = get_logger(__name__)


class ConectorSQLite:
    '''
    Classe responsável por gerenciar a conexão de baixo nível com o banco SQLite
    e executar operações genéricas de CRUD.
    '''

    # Inicializa o conector com o caminho do banco de dados
    def __init__(self, db_path="agenda.db"):
        self.db_path = db_path
        self.conn = None
        self.cur = None

    # Estabelece conexão com o banco de dados e configura o cursor
    def connect(self):
        logger.debug("Conectando ao banco SQLite: %s", self.db_path)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()

        # Garante integridade referencial
        self.cur.execute("PRAGMA foreign_keys = ON;")

        logger.info("Conexão com SQLite estabelecida com sucesso")

        return self.conn

    # Fecha o cursor e a conexão com o banco de dados, se existirem
    def close(self):
        logger.debug("Fechando conexão com o banco SQLite")
        try:
            if self.cur:
                self.cur.close()
            if self.conn:
                self.conn.close()
            logger.info("Conexão com o banco SQLite fechada")
        except Exception:
            logger.exception("Erro ao fechar conexão com o banco SQLite")

    #
    # Operações genéricas
    #

    # Desativa uma linha mantendo o registro no banco (soft delete)
    def desative_line(self, obj):
        query = f"UPDATE {obj.table} SET active = 0 WHERE id = ?"
        logger.debug("Desativando linha em %s com id=%s", obj.table, obj.id)
        self.cur.execute(query, (obj.id,))

    # Reativa uma linha anteriormente desativada
    def ative_line(self, obj):
        query = f"UPDATE {obj.table} SET active = 1 WHERE id = ?"
        logger.debug("Ativando linha em %s com id=%s", obj.table, obj.id)
        self.cur.execute(query, (obj.id,))

    # Seleciona linhas da tabela, com ou sem filtro por id
    def select(self, obj, id=None):
        if id is None:
            query = f"SELECT * FROM {obj.table}"
            logger.debug("Selecionando todas as linhas de %s", obj.table)
            self.cur.execute(query)
        else:
            query = f"SELECT * FROM {obj.table} WHERE id = ?"
            logger.debug("Selecionando linha de %s com id=%s", obj.table, id)
            self.cur.execute(query, (id,))
        return [dict(row) for row in self.cur.fetchall()]

    # Insere uma nova linha na tabela a partir dos atributos do objeto
    def insert(self, obj):
        keys = [k for k in obj.__dict__.keys() if k != "table"]
        values = [getattr(obj, k) for k in keys]
        placeholders = ", ".join(["?"] * len(values))

        query = f"""
            INSERT INTO {obj.table} ({', '.join(keys)})
            VALUES ({placeholders})
        """

        logger.debug("Inserindo em %s com campos=%s", obj.table, keys)
        self.cur.execute(query, tuple(values))
        obj.id = self.cur.lastrowid
        logger.info("Registro inserido em %s com id=%s", obj.table, obj.id)
        return obj.id

    # Atualiza uma linha existente na tabela com base no id do objeto
    def update(self, obj):
        keys = [k for k in obj.__dict__.keys() if k not in ("table", "id")]
        values = [getattr(obj, k) for k in keys]
        set_clause = ", ".join([f"{k} = ?" for k in keys])

        query = f"""
            UPDATE {obj.table}
            SET {set_clause}
            WHERE id = ?
        """

        logger.debug("Atualizando registro em %s id=%s com campos=%s", obj.table, obj.id, keys)
        self.cur.execute(query, tuple(values) + (obj.id,))
