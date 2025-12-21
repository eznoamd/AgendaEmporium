from PySide6.QtWidgets import QMainWindow
from ui.sidebar import Ui_MainWindow
from utils.logs import get_logger
from views import setup_all
from utils.path import get_style_path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.logger = get_logger(__name__)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self._setup_ui()
        setup_all(self.ui)

    def _setup_ui(self):
        self.ui.icons_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.button_agendamento.setChecked(True)

        self._connect_navigation()

    def _connect_navigation(self):
        nav = [
            (self.ui.button_agendamento, self.ui.page_agendamentos),
            (self.ui.button_procedimento, self.ui.page_procedimentos),
            (self.ui.button_status, self.ui.page_status),
            (self.ui.button_profissional, self.ui.page_tecnicas),
            (self.ui.button_cliente, self.ui.page_clientes),

            (self.ui.button_agendamento_2, self.ui.page_agendamentos),
            (self.ui.button_procediento_2, self.ui.page_procedimentos),
            (self.ui.button_status_2, self.ui.page_status),
            (self.ui.button_profissional_2, self.ui.page_tecnicas),
            (self.ui.button_cliente_2, self.ui.page_clientes),
        ]

        for button, page in nav:
            button.clicked.connect(
                lambda _, p=page: self.ui.stackedWidget.setCurrentWidget(p)
            )
