from .AgendamentosView import setup_page as setup_agendamentos
from .ProcedimentosView import setup_page as setup_procedimentos
from .StatusView import setup_page as setup_status
from .TecnicasView import setup_page as setup_tecnicas
from .ClientesView import setup_page as setup_clientes


def setup_all(ui):
    """Configura todas as páginas do stackedWidget.

    Cada função de setup recebe o QWidget correspondente à página.
    """
    setup_agendamentos(ui.page_agendamentos)
    setup_procedimentos(ui.page_procedimentos)
    setup_status(ui.page_status)
    setup_tecnicas(ui.page_tecnicas)
    setup_clientes(ui.page_clientes)
