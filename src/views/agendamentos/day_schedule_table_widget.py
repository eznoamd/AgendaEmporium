from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt, QDate
from model.TecnicaModel import TecnicaModel
from PySide6.QtWidgets import QHeaderView



class DayScheduleTableWidget(QTableWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.verticalHeader().setVisible(False)

        self.tecnicos = []



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


    def _build_headers(self):
        headers = ["Horário"]
        headers += [t["name"] for t in self.tecnicos]
        self.setHorizontalHeaderLabels(headers)

    def _build_time_column(self, times):
        for row, time in enumerate(times):
            item = QTableWidgetItem(time)
            item.setTextAlignment(Qt.AlignCenter)
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

    from PySide6.QtWidgets import QHeaderView

    def _configure_headers(self):
        header = self.horizontalHeader()

        # Primeiro: todas stretch
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Depois: coluna horário fixa
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        self.setColumnWidth(0, 80)

        header.setDefaultAlignment(Qt.AlignCenter)
        header.setMinimumHeight(40)
