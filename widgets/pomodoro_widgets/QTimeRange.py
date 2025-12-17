from PySide6.QtWidgets import QTimeEdit, QAbstractSpinBox
from PySide6.QtCore import QTime

class QTimeRange(QTimeEdit):
    def __init__(self, qtime: QTime):
        super().__init__()
        self.setDisplayFormat("mm:ss")
        self.setTime(qtime)
        self.setButtonSymbols(QAbstractSpinBox.NoButtons)