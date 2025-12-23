from PySide6.QtWidgets import QWidget, QVBoxLayout
from views.agendamentos.agendamentos_view import AgendamentosView


def setup_page(page: QWidget) -> None:
    """
    Adapter de inicialização da página de Agendamentos.
    """
    layout = QVBoxLayout(page)
    view = AgendamentosView(page)
    layout.addWidget(view)

    page._view = view
