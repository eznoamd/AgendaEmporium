import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot

from widgets.sidebar import Ui_MainWindow
from pages import setup_all as setup_pages

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

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
        setup_pages(self.ui)

def pick_style_path():
    if sys.platform == "win32":
        return "widgets/style.qss"
    return "./widgets/style.qss"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open(pick_style_path(), "r") as f:
        style = f.read()
    app.setStyleSheet(style)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())