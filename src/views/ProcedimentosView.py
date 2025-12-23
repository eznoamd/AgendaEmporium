from PySide6.QtWidgets import QWidget, QVBoxLayout
from views.procedimentos.procedimento_view import ProcedimentoView


def setup_page(page: QWidget) -> None:
    """
    Adapter de inicialização da página de Procedimentos.
    """
    layout = QVBoxLayout(page)
    view = ProcedimentoView(page)
    layout.addWidget(view)

    page._view = view
