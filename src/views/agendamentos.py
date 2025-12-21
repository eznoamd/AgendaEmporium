from PySide6.QtWidgets import QWidget
from utils.logs import get_logger


logger = get_logger(__name__)


def setup_page(page: QWidget) -> None:
    """Personalização da página de Agendamentos."""
    logger.info("Configurando página de Agendamentos")
    page.setObjectName("page_agendamentos_custom")
