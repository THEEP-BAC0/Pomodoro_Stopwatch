from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PySide6.QtCore import Qt
from widgets.titlebar_widgets.QTitleBar import QTitleBar
from widgets.stopwatch_widgets.QStopwatchScreen import QStopwatchScreen
from .StyleManager import StyleManager
from .ScreenManager import ScreenManager
from .WindowDragger import WindowDragger

class QWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_meta()
        self.init_vars()
        self.init_ui()
    
    def init_meta(self) -> None:
        self.setWindowTitle("Pomodoro Stopwatch")
        self.setProperty("theme", "pink")
        self.setFixedSize(300, 200)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        with open("style.qss", "r") as f: self.setStyleSheet(f.read())

    def init_vars(self) -> None:
        self.style_manager = StyleManager(self)
        self.screen_manager = ScreenManager(self)
        self.dragger = WindowDragger(self)

    def init_ui(self) -> None:
        # Create main widget
        main_widget = QWidget()

        # Create wrapper
        self.wrapper = QVBoxLayout()
        self.wrapper.setContentsMargins(0, 0, 0, 0)
        main_widget.setLayout(self.wrapper)

        # Create round widget
        self.round_widget = QWidget(self)
        self.round_widget.setObjectName("RoundWidget")
        self.round_widget.setProperty("theme", "pink")
        self.round_widget.resize(300, 200)

        # Create title bar
        self.titleBar = QTitleBar(self)
        
        self.wrapper.addWidget(self.titleBar)
        self.screen_manager.current_screen = QStopwatchScreen(self)
        self.wrapper.addWidget(self.screen_manager.current_screen)
        
        self.setCentralWidget(main_widget)
    
    def mousePressEvent(self, event):
        self.dragger.start_drag(event)

    def mouseMoveEvent(self, event):
        self.dragger.drag(event)

    def mouseReleaseEvent(self, event):
        self.dragger.end_drag(event)