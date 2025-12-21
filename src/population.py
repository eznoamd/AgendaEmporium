"""Script para popular o banco SQLite com dados iniciais.

Rode este arquivo diretamente, por exemplo:

    python population.py

Ele usa os próprios models do sistema para inserir registros
nas tabelas statuses, service_types, technicians e clients.
"""

from model.StatusModel import StatusModel
from model.TipoModel import TipoModel
from model.TecnicaModel import TecnicaModel
from model.ClienteModel import ClienteModel
from utils.logs import setup_logging, get_logger


logger = get_logger(__name__)

def seed_statuses() -> None:
    """Popula a tabela de statuses se estiver vazia."""
    model = StatusModel()
    existentes = model.get_all() or []
    if existentes:
        logger.info("[statuses] Já existe dado, não será reaplicado.")
        return

    dados = [
        ("Disponível", "#E0E0E0"),
        ("Agendado", "#4CAF50"),
        ("Cancelado", "#F44336"),
        ("Reagendado", "#FF9800"),
        ("Bloqueado", "#9E9E9E"),
    ]

    for nome, cor in dados:
        StatusModel().criar_status(nome, cor)

    logger.info("[statuses] Dados iniciais inseridos.")


def seed_service_types() -> None:
    """Popula a tabela de tipos de serviço (service_types) se estiver vazia."""
    model = TipoModel()
    existentes = model.get_all() or []
    if existentes:
        logger.info("[service_types] Já existe dado, não será reaplicado.")
        return

    dados = [
        ("Atendimento", None),
        ("Retorno", None),
        ("Procedimento", None),
    ]

    for nome, filtros in dados:
        TipoModel().criar_tipo(nome, filtros)

    logger.info("[service_types] Dados iniciais inseridos.")


def seed_technicians() -> None:
    """Popula a tabela de técnicos (technicians) se estiver vazia."""
    model = TecnicaModel()
    existentes = model.get_all() or []
    if existentes:
        logger.info("[technicians] Já existe dado, não será reaplicado.")
        return

    dados = [
        ("Técnico 1", 1),
        ("Técnico 2", 1),
    ]

    for nome, ativo in dados:
        TecnicaModel().criar_tecnica(nome, ativo)

    logger.info("[technicians] Dados iniciais inseridos.")


def seed_clients() -> None:
    """Popula a tabela de clientes (clients) se estiver vazia."""
    model = ClienteModel()
    existentes = model.get_all() or []
    if existentes:
        logger.info("[clients] Já existe dado, não será reaplicado.")
        return

    dados = [
        ("Cliente Demo 1", "C001"),
        ("Cliente Demo 2", "C002"),
    ]

    for nome, codigo in dados:
        ClienteModel().criar_cliente(nome, codigo)

    logger.info("[clients] Dados iniciais inseridos.")


def main() -> None:
    setup_logging()
    logger.info("Iniciando população do banco...")
    try:
        seed_statuses()
        seed_service_types()
        seed_technicians()
        seed_clients()
    except Exception as exc:
        logger.exception("Erro ao popular o banco: %s", exc)
    else:
        logger.info("População concluída.")


if __name__ == "__main__":
    main()

