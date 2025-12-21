from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QStackedWidget, QPushButton, QHBoxLayout
)
from PySide6.QtCore import Qt
from utils.logs import get_logger
from .calendar_panel_widget import CalendarPanelWidget
from .day_schedule_table_widget import DayScheduleTableWidget

logger = get_logger(__name__)


class AgendamentosView(QWidget):
    PAGE_CALENDAR = 0
    PAGE_DAY = 1

    def __init__(self, parent=None):
        super().__init__(parent)

        self.stack = QStackedWidget()

        self.calendar_panel = CalendarPanelWidget()
        self.day_table = DayScheduleTableWidget()

        self._build_calendar_page()
        self._build_day_page()

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.stack.setCurrentIndex(self.PAGE_CALENDAR)

    def _build_calendar_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.calendar_panel)
        self.calendar_panel.day_selected.connect(self.open_day)

        self.stack.addWidget(page)

    def _build_day_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        top_bar = QHBoxLayout()
        self.btn_back = QPushButton("← Voltar")
        self.btn_back.clicked.connect(self.go_back)

        top_bar.addWidget(self.btn_back)
        top_bar.addStretch()

        layout.addLayout(top_bar)
        layout.addWidget(self.day_table)

        self.stack.addWidget(page)

    def open_day(self, qdate):
        logger.info(f"Abrindo dia {qdate.toString()}")
        self.day_table.build_day(qdate)
        self.stack.setCurrentIndex(self.PAGE_DAY)

    def go_back(self):
        self.stack.setCurrentIndex(self.PAGE_CALENDAR)
