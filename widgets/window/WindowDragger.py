from PySide6.QtCore import Qt, QPoint

class WindowDragger:
    def __init__(self, window):
        self.window = window
        self.offset = QPoint()
        self.dragging = False

    def start_drag(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            # Store the offset between mouse position and top-left of the window
            self.offset = event.globalPosition().toPoint() - self.window.frameGeometry().topLeft()
            event.accept()

    def drag(self, event):
        if self.dragging:
            # Move window relative to mouse
            self.window.move(event.globalPosition().toPoint() - self.offset)
            event.accept()

    def end_drag(self, event):
        self.dragging = False
        event.accept()