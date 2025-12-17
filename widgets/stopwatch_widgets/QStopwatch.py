from PySide6.QtCore import QObject, QTime, QTimer, Signal

class QStopwatch(QObject):
    time_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.running = False
        self.minutes = 0
        self.seconds = 0

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)
    
    def toggle(self) -> None:
        self.running = not self.running
        if self.running:
            self.timer.start()
        else:
            self.timer.stop()

    def tick(self) -> None:
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1

        self.time_changed.emit(self.construct_time())

    def construct_time(self) -> str:
        return f"{self.minutes:02d}:{self.seconds:02d}"
    
    def return_time(self) -> QTime:
        total_seconds = self.minutes * 60 + self.seconds
        h = total_seconds / 3600
        m = (total_seconds % 3600) / 60
        s = total_seconds % 60
        return QTime(h, m, s)