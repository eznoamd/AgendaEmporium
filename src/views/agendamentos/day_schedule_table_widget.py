from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QDate
from model.TecnicaModel import TecnicaModel
from PySide6.QtWidgets import QHeaderView

class DayScheduleTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.verticalHeader().setVisible(False)
        self.verticalHeader().setDefaultSectionSize(60)
        self.setSelectionMode(QTableWidget.SingleSelection)
        self.setSelectionBehavior(QTableWidget.SelectItems)


        self.tecnicos = []


    def _apply_style(self):
        self.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                gridline-color: #e6e6e6;
                font-size: 12px;
            }

            QHeaderView::section {
                background-color: #f8f9fa;
                border: 1px solid #e6e6e6;
                padding: 6px;
                font-weight: bold;
            }

            QTableWidget::item {
                border: 1px solid #f0f0f0;
            }

            QTableWidget::item:selected {
                background-color: #d0ebff;
            }
        """)



    def build_day(self, qdate: QDate):
        self.clear()

        self.verticalHeader().setVisible(False)  # ← reaplica após clear()

        self.tecnicos = self._load_tecnicos()
        times = self._generate_times()

        self.setRowCount(len(times))
        self.setColumnCount(len(self.tecnicos) + 1)

        self._configure_headers()
        self._build_headers()
        self._build_time_column(times)
        self._build_empty_cells()
        self._apply_style()
        self.setShowGrid(True)
        self.setAlternatingRowColors(False)



    def _build_headers(self):
        headers = ["Horário"]
        headers += [t["name"] for t in self.tecnicos]
        self.setHorizontalHeaderLabels(headers)

    def _build_time_column(self, times):
        for row, time in enumerate(times):
            item = QTableWidgetItem(time)
            item.setTextAlignment(Qt.AlignTop | Qt.AlignHCenter)
            item.setForeground(Qt.gray)
            item.setFlags(Qt.ItemIsEnabled)
            self.setItem(row, 0, item)


    def _load_tecnicos(self):
        model = TecnicaModel()
        tecnicos = model.get_all()

        # filtra apenas ativos
        return [t for t in tecnicos if t["active"] == 1]

    def _generate_times(self):
        times = []
        hour = 8
        minute = 0

        while hour < 18:
            times.append(f"{hour:02d}:{minute:02d}")
            minute += 30
            if minute == 60:
                minute = 0
                hour += 1

        return times

    def _configure_headers(self):
        header = self.horizontalHeader()

        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.Fixed)

        self.setColumnWidth(0, 70)

        header.setDefaultAlignment(Qt.AlignCenter)
        header.setFixedHeight(48)

    def _build_empty_cells(self):
        for row in range(self.rowCount()):
            for col in range(1, self.columnCount()):
                item = QTableWidgetItem("")
                item.setFlags(
                    Qt.ItemIsSelectable |
                    Qt.ItemIsEnabled
                )
                self.setItem(row, col, item)
