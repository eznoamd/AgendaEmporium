import os
from pathlib import Path
from dotenv import load_dotenv

import sys

load_dotenv()

def get_style_path() -> Path:
    """Retorna o caminho completo para o arquivo de estilo (style.qss)."""

    if getattr(sys, "frozen", False):
        base = Path(sys.executable).parent
    else:
        base = Path(__file__).resolve().parent.parent

    return base / "ui" / "style.qss"


def get_data_path(path: str = "") -> Path:
    """Retorna o caminho base da pasta de dados, opcionalmente com sufixo."""

    base = Path("../data")
    return base / path


def get_sql_path() -> Path:
    """Retorna o caminho do arquivo SQL definido via variável de ambiente SQL_NAME."""

    sql_name = os.getenv("SQL_NAME", "bancolite")
    return Path("work/sql") / f"{sql_name}.sql"


def get_database_path() -> Path:
    """Retorna o caminho do banco de dados definido via variável DB_NAME."""

    db_name = os.getenv("DB_NAME", "database")
    return Path("../data/database") / f"{db_name}.db"