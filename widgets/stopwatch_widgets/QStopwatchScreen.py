from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QTime
from .QStopwatch import QStopwatch

class QStopwatchScreen(QWidget):
    def __init__(self, QMainWindow):
        super().__init__()
        self.QMainWindow = QMainWindow
        self.init_vars()
        self.init_ui()
    
    # Initialize all needed variables
    def init_vars(self) -> None:
        self.stopwatch = QStopwatch()

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Create widget components
        self.stopwatchLabel: QLabel = QLabel("00:00")
        self.stopwatchButton: QPushButton = QPushButton("Start")
        self.proceedButton: QPushButton = QPushButton("Proceed")
        
        # Modify widgets before adding
        self.stopwatchLabel.setObjectName("StopwatchLabel")
        self.stopwatchButton.setObjectName("StopwatchButton")
        self.proceedButton.setObjectName("ProceedButton")
        self.proceedButton.hide()
        
        # Add widgets to layout
        self.layout.addWidget(self.stopwatchLabel)
        self.layout.addWidget(self.stopwatchButton)
        self.layout.addWidget(self.proceedButton)

        # Connect signals
        self.stopwatchButton.clicked.connect(self.toggle_stopwatch)
        self.stopwatch.time_changed.connect(self.update_label)
        self.proceedButton.clicked.connect(self.switch_pomodoro)

        self.set_theme()

    # Toggles the stopwatch
    def toggle_stopwatch(self) -> None:
        self.stopwatch.toggle()
        self.stopwatchButton.setText("Stop" if self.stopwatch.running else "Start")

        if self.stopwatch.running == False: self.proceedButton.show()

    # Updates stopwatch label
    def update_label(self, text) -> None:
        self.stopwatchLabel.setText(text)
    
    # Initializes pomodoro screen
    def switch_pomodoro(self) -> None:
        # Get time from stopwatch
        qtime_value: QTime = self.stopwatch.return_time()

        # Switch to pomodoro screen
        self.QMainWindow.screen_manager.switch_to_pomodoro_screen(qtime_value)
    
    def set_theme(self):
        theme = "pink"
        self.setProperty("theme", theme)
        self.QMainWindow.style_manager.apply_theme(theme, self)