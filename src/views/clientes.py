from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from utils.logs import get_logger


logger = get_logger(__name__)


def setup_page(page: QWidget) -> None:
    """Personalização da página de Clientes.

    Cria uma tabela e tenta listar os clientes usando ClienteModel.get_all().
    Qualquer erro de import ou banco não impede a janela de abrir.
    """
    page.setObjectName("page_clientes_custom")

    logger.info("Configurando página de Clientes")

    # Layout principal da página (vertical simples)
    layout = page.layout()
    if layout is None:
        layout = QVBoxLayout(page)
        page.setLayout(layout)

    # Tabela de clientes
    table = QTableWidget(page)
    table.setObjectName("table_clientes")
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["ID", "Nome", "Código"])

    clientes = []

    try:
        # Import atrasado para evitar quebrar o app na inicialização
        from model.ClienteModel import ClienteModel

        model = ClienteModel()
        logger.debug("Carregando lista de clientes para a página")
        clientes = model.get_all() or []
        logger.info("%d clientes carregados na página", len(clientes))
    except Exception:
        # Em caso de erro (sem banco, sem driver, etc.), só não preenche a tabela
        logger.exception("Erro ao carregar clientes para a página")
        clientes = []

    table.setRowCount(len(clientes))

    for row, cliente in enumerate(clientes):
        # Como o cursor é dictionary=True, cada linha é um dict
        id_val = str(cliente.get("id", ""))
        nome_val = str(cliente.get("name", ""))
        codigo_val = str(cliente.get("code", ""))

        table.setItem(row, 0, QTableWidgetItem(id_val))
        table.setItem(row, 1, QTableWidgetItem(nome_val))
        table.setItem(row, 2, QTableWidgetItem(codigo_val))

    table.resizeColumnsToContents()

    layout.addWidget(table)
