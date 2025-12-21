import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from utils.path import get_data_path


LOG_DIR = Path(get_data_path("logs"))
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"


def setup_logging() -> None:
    """Configura o logging da aplicação.

    Deve ser chamada uma vez, no início da aplicação (ex: em main.py).
    """

    logger = logging.getLogger()  # root logger
    logger.setLevel(logging.DEBUG)

    # Evita adicionar handlers duplicados se a função for chamada mais de uma vez
    if logger.handlers:
        return

    formatter = logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Handler para o console (terminal)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Handler para arquivo com rotação (evita arquivo gigante)
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,  # 5 MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def get_logger(name: str | None = None) -> logging.Logger:
    """Retorna um logger para o módulo especificado.

    Uso recomendado: get_logger(__name__)
    """

    return logging.getLogger(name)