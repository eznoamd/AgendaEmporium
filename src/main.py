import sys
import logging
from PySide6.QtWidgets import QMainWindow, QApplication

from widgets.sidebar import Ui_MainWindow
from pages import setup_all as setup_pages
from utils.logs import setup_logging, get_logger

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.logger = get_logger(__name__)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icons_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.button_agendamento.setChecked(True)

        # Conexões dos botões laterais com as páginas do stackedWidget
        self.ui.button_agendamento.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_agendamentos)
        )
        self.ui.button_procedimento.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_procedimentos)
        )
        self.ui.button_status.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_status)
        )
        self.ui.button_profissional.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tecnicas)
        )
        self.ui.button_cliente.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_clientes)
        )

        # Mesma navegação para os botões do menu expandido
        self.ui.button_agendamento_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_agendamentos)
        )
        self.ui.button_procediento_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_procedimentos)
        )
        self.ui.button_status_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_status)
        )
        self.ui.button_profissional_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_tecnicas)
        )
        self.ui.button_cliente_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_clientes)
        )

        # Personalização de cada página do stackedWidget
        self.logger.debug("Inicializando páginas do stackedWidget")
        setup_pages(self.ui)
        self.logger.info("Janela principal inicializada")

def pick_style_path():
    if sys.platform == "win32":
        return "widgets/style.qss"
    return "./widgets/style.qss"

if __name__ == "__main__":
    # Configura o sistema de logs uma única vez, no início da aplicação
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Aplicação iniciando")

    app = QApplication(sys.argv)
    with open(pick_style_path(), "r") as f:
        style = f.read()
    app.setStyleSheet(style)

    window = MainWindow()
    window.show()

    logger.info("Aplicação em execução (janela principal exibida)")
    sys.exit(app.exec())