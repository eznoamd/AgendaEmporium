from PySide6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
from PySide6.QtCore import Qt

from model.TipoModel import TipoModel


class ProcedimentoView(QWidget):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self._model = TipoModel()

        layout = QVBoxLayout(self)

        self._table = QTableWidget(self)
        self._table.setColumnCount(3)
        self._table.setHorizontalHeaderLabels(["ID", "Nome", "Duração"])
        self._table.setRowCount(0)
        self._table.setEditTriggers(QTableWidget.NoEditTriggers)
        self._table.setSelectionBehavior(QTableWidget.SelectRows)
        self._table.setSelectionMode(QTableWidget.SingleSelection)
        self._table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self._table)

        self._carregar_dados()

    def _carregar_dados(self) -> None:
        dados = self._model.get_all() or []

        self._table.setRowCount(len(dados))

        for row, item in enumerate(dados):
            # item pode ser um dict ou um objeto com atributos id, name, duration
            if isinstance(item, dict):
                id_val = item.get("id")
                name_val = item.get("name")
                duration_val = item.get("duration")
            else:
                id_val = getattr(item, "id", None)
                name_val = getattr(item, "name", None)
                duration_val = getattr(item, "duration", None)

            id_item = QTableWidgetItem(str(id_val) if id_val is not None else "")
            name_item = QTableWidgetItem(str(name_val) if name_val is not None else "")
            duration_item = QTableWidgetItem(str(duration_val) if duration_val is not None else "")

            id_item.setTextAlignment(Qt.AlignCenter)
            duration_item.setTextAlignment(Qt.AlignCenter)

            self._table.setItem(row, 0, id_item)
            self._table.setItem(row, 1, name_item)
            self._table.setItem(row, 2, duration_item)