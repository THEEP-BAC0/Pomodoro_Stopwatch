from PySide6.QtWidgets import QWidget

class StyleManager:
    def __init__(self, window):
        self.window = window
    
    def apply_theme(self, theme: str, screen: QWidget) -> None:
        # Update window
        self.window.setProperty("theme", theme)
        self.window.round_widget.setProperty("theme", theme)
        self.window.titleBar.set_theme(theme)
        self.window.style().unpolish(self.window)
        self.window.style().polish(self.window)
        self.window.round_widget.style().unpolish(self.window.round_widget)
        self.window.round_widget.style().polish(self.window.round_widget)
        self.window.round_widget.update()

        # Update screen children
        for child in screen.findChildren(QWidget):
            child.setProperty("theme", theme)
            child.style().unpolish(child)
            child.style().polish(child)
            child.update()