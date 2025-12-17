from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QFrame

class QTitleBar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_vars(parent)
        self.init_ui()
        self.setFixedHeight(25)
        self.setMouseTracking(True)
    
    def init_vars(self, parent):
        self.setObjectName("TitleBar")
        self.setProperty("theme", "pink")
        self.setAutoFillBackground(True)
        self.setFrameShape(QFrame.NoFrame)
        self.parent = parent

    def init_ui(self):
        # Create layouts
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        title_layout = QHBoxLayout()
        title_layout.setContentsMargins(0, 0, 0, 0)

        layout.addLayout(buttons_layout)
        layout.addLayout(title_layout)

        # Title label
        title = QLabel("Pomodoro Stopwatch")
        title.setObjectName("Title")
        title.setProperty("theme", "pink")
        title_layout.addWidget(title)

        # Close button
        btn_close = QPushButton("x")
        btn_close.setObjectName("ExitButton")
        btn_close.clicked.connect(self.parent.close)

        # Minimize button
        btn_min = QPushButton("-")
        btn_min.setObjectName("MinimizeButton")
        btn_min.clicked.connect(self.parent.showMinimized)

        # Maximize button
        btn_max = QPushButton("+")
        btn_max.setObjectName("MaximizeButton")
        btn_max.clicked.connect(self.toggle_max_restore)

        # Modify button
        for b in (btn_close, btn_min, btn_max): b.setFixedSize(14, 14)

        # Add buttons to layour
        buttons_layout.addWidget(btn_close)
        buttons_layout.addWidget(btn_min)
        buttons_layout.addWidget(btn_max)

        self.set_theme("pink")
    
    def set_theme(self, theme: str):
        # Set theme on this widget
        self.setProperty("theme", theme)

        # Re-polish self
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

        # Apply theme to children
        for child in self.findChildren(QWidget):
            child.setProperty("theme", theme)
            child.style().unpolish(child)
            child.style().polish(child)
            child.update()
    
    def toggle_max_restore(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()