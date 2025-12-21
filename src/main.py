import sys
from PySide6.QtWidgets import QApplication
from utils.logs import setup_logging
from utils.path import get_style_path
from ui.MainWindow import MainWindow


def main():
    setup_logging()

    app = QApplication(sys.argv)

    with open(get_style_path(), "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
