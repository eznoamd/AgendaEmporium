from PySide6.QtWidgets import QWidget
from utils.logs import get_logger


logger = get_logger(__name__)


def setup_page(page: QWidget) -> None:
    """Personalização da página de Status."""
    logger.info("Configurando página de Status")
    page.setObjectName("page_status_custom")
