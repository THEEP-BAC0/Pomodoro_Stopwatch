from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QTime
from ..pomodoro_widgets.QTimeRange import QTimeRange

class QSettingsScreen(QWidget):
    def __init__(self, pomodoro_time: QTime, break_time: QTime, QMainWindow):
        super().__init__()
        self.QMainWindow = QMainWindow
        self.QMainWindow.setProperty("theme", "cyan")
        self.init_vars(pomodoro_time, break_time)
        self.init_ui()
    
    # Initialize all needed variables
    def init_vars(self, pomodoro_time: int, break_time: QTime) -> None:
        self.at_settings: bool = False
        self.pomodoro_time: QTime = pomodoro_time
        self.break_time: QTime = break_time

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)

        # Create widget components
        self.backButton = QPushButton("<")
        self.breakLabel = QLabel(f"Break Time: ")
        self.breaktimeRange = QTimeRange(self.break_time)
        self.pomodoroLabel = QLabel(f"Pomodoro Time: ")
        self.pomodoroRange = QTimeRange(self.pomodoro_time)

        # Create widget layout
        self.breakLayout = QHBoxLayout()
        self.pomodoroLayout = QHBoxLayout()
        self.layout.addLayout(self.breakLayout)
        self.layout.addLayout(self.pomodoroLayout)

        # Modify widgets before adding
        self.setObjectName("SettingsScreen")
        self.breakLabel.setObjectName("BreakLabel")
        self.breaktimeRange.setObjectName("BreaktimeRange")
        self.pomodoroLabel.setObjectName("PomodoroLabel")
        self.pomodoroRange.setObjectName("PomodoroRange")
        
        # Add widgets to layout
        self.layout.addWidget(self.backButton)
        self.breakLayout.addWidget(self.breakLabel)
        self.breakLayout.addWidget(self.breaktimeRange)
        self.pomodoroLayout.addWidget(self.pomodoroLabel)
        self.pomodoroLayout.addWidget(self.pomodoroRange)

        # Connect signals
        self.backButton.clicked.connect(self.pomodoro_switch)

        self.set_theme()

    def pomodoro_switch(self):
        new_pomo_time = self.pomodoroRange.time()
        new_break_time = self.breaktimeRange.time()
        self.QMainWindow.screen_manager.switch_to_pomodoro_screen(QTime(0, 0 , 0), pomo_time=new_pomo_time, break_time=new_break_time)

    def set_theme(self):
        theme = "purple"
        self.setProperty("theme", theme)
        self.QMainWindow.style_manager.apply_theme(theme, self)