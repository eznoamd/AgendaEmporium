import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSlot

from widgets.sidebar import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icons_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.button_agendamento.setChecked(True)


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