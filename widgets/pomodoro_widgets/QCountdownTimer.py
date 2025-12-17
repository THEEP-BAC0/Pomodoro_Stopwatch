from PySide6.QtCore import QObject, QTimer, Signal, QTime

class QCountdownTimer(QObject):
    time_changed = Signal(str)
    finished = Signal()

    def __init__(self, qtime):
        super().__init__()
        self.running: bool = False
        self.time_left: QTime = qtime

        self.timer: QTimer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._tick)
    
    def toggle(self) -> None:
        self.running = not self.running
        if self.running: self.timer.start()
        else: self.timer.stop()

    def _tick(self) -> None:
        # Convert QTime to total seconds
        total_seconds = (
            self.time_left.hour() * 3600 +
            self.time_left.minute() * 60 +
            self.time_left.second()
        )

        # Stop if already zero
        if total_seconds <= 0:
            self.time_left = QTime(0, 0, 0)
            self.time_changed.emit(self.time_left.toString("mm:ss"))
            self.timer.stop()
            self.running = False
            self.finished.emit()
            return

        # Subtract 1 second
        total_seconds -= 1

        # Convert seconds to QTime
        h = total_seconds / 3600
        m = (total_seconds % 3600) / 60
        s = total_seconds % 60
        self.time_left = QTime(h, m, s)

        # Update UI
        self.time_changed.emit(self.time_left.toString("mm:ss"))

    def set_time(self, qtime: QTime) -> None:
        self.time_left = QTime(qtime.hour(), qtime.minute(), qtime.second())
        self.time_changed.emit(self.time_left.toString("mm:ss"))