from PySide6.QtWidgets import QWidget
from utils.logs import get_logger


logger = get_logger(__name__)


def setup_page(page: QWidget) -> None:
    """Personalização da página de Técnicas/Profissionais."""
    logger.info("Configurando página de Técnicas/Profissionais")
    page.setObjectName("page_tecnicas_custom")
