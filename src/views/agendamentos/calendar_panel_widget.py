from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QCalendarWidget
)
from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtGui import QTextCharFormat, QColor


class CalendarPanelWidget(QWidget):
    day_selected = Signal(QDate)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("CalendarPanel")
        
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setVerticalHeaderFormat(
            QCalendarWidget.NoVerticalHeader
        )
        self.calendar.setNavigationBarVisible(False)
        self.calendar.clicked.connect(self.day_selected.emit)

        self._neutralize_weekends()

        self._build_ui()
        self._sync_month_label()
        self.calendar.currentPageChanged.connect(
            lambda y, m: self._sync_month_label()
        )


    # -------------------------
    # UI
    # -------------------------
    def _build_ui(self):
        main = QVBoxLayout(self)
        main.setContentsMargins(0, 0, 0, 0)
        main.setSpacing(12)
        main.setAlignment(Qt.AlignCenter)

        # Container branco (isolamento visual)
        container = QWidget()
        container.setObjectName("calendarContainer")
        container.setMaximumWidth(900)

        layout = QVBoxLayout(container)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(10)

        # Título
        title = QLabel("Agenda")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("calendarTitle")

        # Navegação
        nav = QHBoxLayout()
        nav.setSpacing(8)

        btn_prev = QPushButton("◀")
        btn_next = QPushButton("▶")

        btn_prev.setFixedSize(32, 32)
        btn_next.setFixedSize(32, 32)

        btn_prev.clicked.connect(self._prev_month)
        btn_next.clicked.connect(self._next_month)

        self.month_label = QLabel()
        self.month_label.setAlignment(Qt.AlignCenter)
        self.month_label.setObjectName("calendarMonth")

        nav.addWidget(btn_prev)
        nav.addStretch()
        nav.addWidget(self.month_label)
        nav.addStretch()
        nav.addWidget(btn_next)

        layout.addWidget(title)
        layout.addLayout(nav)
        layout.addWidget(self.calendar)

        main.addWidget(container)

        self._apply_style()

    # -------------------------
    # Navegação
    # -------------------------
    def _prev_month(self):
        self.calendar.showPreviousMonth()
        self._sync_month_label()

    def _next_month(self):
        self.calendar.showNextMonth()
        self._sync_month_label()

    def _sync_month_label(self):
        month = self.calendar.monthShown()
        year = self.calendar.yearShown()

        date = QDate(year, month, 1)
        self.month_label.setText(
            date.toString("MMMM yyyy").capitalize()
        )


    # -------------------------
    # Estilo isolado
    # -------------------------
    def _apply_style(self):
        self.setStyleSheet("""
            QWidget#calendarContainer {
                background-color: #FFFFFF;
                border-radius: 12px;
            }

            QLabel#calendarTitle {
                font-size: 22px;
                font-weight: bold;
                color: #222;
            }

            QLabel#calendarMonth {
                font-size: 17px;
                font-weight: 600;
                color: #444;
            }

            QPushButton {
                background-color: #F2F2F2;
                border: none;
                border-radius: 6px;
                font-size: 15px;
            }

            QPushButton:hover {
                background-color: #E0E0E0;
            }

            QCalendarWidget {
                background-color: white;
            }

            /* Dias do mês */
            QCalendarWidget QAbstractItemView {
                selection-background-color: #6C9EFF;
                selection-color: white;
                font-size: 20px;
                gridline-color: #D0D0D0;
            }

            /* Cabeçalho (Seg, Ter, Qua...) */
            QCalendarWidget QHeaderView::section {
                font-size: 20px;
                font-weight: bold;
                color: #FFFFFF;
                background-color: #F7F7F7;
                border: 1px solid #E0E0E0;
            }
        """)



    # -------------------------
    # API pública
    # -------------------------
    def mark_day(self, date: QDate, color="#A7C7E7"):
        fmt = QTextCharFormat()
        fmt.setBackground(QColor(color))
        self.calendar.setDateTextFormat(date, fmt)

    def _neutralize_weekends(self):
        fmt = QTextCharFormat()
        fmt.setForeground(QColor("#222"))  # mesma cor dos outros dias

        self.calendar.setWeekdayTextFormat(Qt.Saturday, fmt)
        self.calendar.setWeekdayTextFormat(Qt.Sunday, fmt)

