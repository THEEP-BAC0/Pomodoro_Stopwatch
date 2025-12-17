from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, QTime
from .QCountdownTimer import QCountdownTimer
from .QTimeRange import QTimeRange

class QPomodoroScreen(QWidget):
    def __init__(self, qtime: QTime, QMainWindow, pomo_time: QTime = None, break_time: QTime = None):
        super().__init__()
        self.QMainWindow = QMainWindow
        self.init_vars(qtime, pomo_time, break_time)
        self.init_ui()
    
    # Initialize all needed variables
    def init_vars(self, qtime: QTime, pomo_time: QTime, break_time: QTime) -> None:
        self.on_break: bool = True
        self.set_breaktime: bool = False
        self.at_settings: bool = False
        if pomo_time: self.pomodoro_time: QTime = pomo_time
        else: self.pomodoro_time: QTime = qtime
        if break_time: self.break_time: QTime = break_time
        else: self.break_time: QTime = self.calculate_break_time()

        self.countdownTimer = QCountdownTimer(self.break_time)

    # Initializes the user interface
    def init_ui(self) -> None:
        # Create layout
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignCenter)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)

        # Create widget components
        self.settingsButton: QPushButton = QPushButton("☰")
        self.stateLabel: QLabel = QLabel(f"Break: ")
        self.pomodoroRange: QTimeRange = QTimeRange(self.pomodoro_time)
        self.breaktimeRange: QTimeRange = QTimeRange(self.break_time)
        self.countdownButton: QPushButton = QPushButton("Start")
        self.switchButton: QPushButton = QPushButton("Switch")

        # Create widget layout
        self.countdownLayout = QHBoxLayout()
        self.countdownLayout.setSpacing(0)
        self.countdownLayout.setContentsMargins(1, 1, 1, 1)
        self.layout.addLayout(self.countdownLayout)

        # Modify widgets before adding
        self.setObjectName("PomodoroScreen")
        self.settingsButton.setObjectName("SettingsButton")
        self.stateLabel.setObjectName("StateLabel")
        self.countdownButton.setObjectName("CountdownButton")
        self.switchButton.setObjectName("SwitchButton")
        self.pomodoroRange.setObjectName("PomodoroRange")
        self.breaktimeRange.setObjectName("BreaktimeRange")
        self.pomodoroRange.hide()

        # Modify buttons
        self.settingsButton.setFixedSize(30, 30)
        for b in (self.countdownButton, self.switchButton): b.setFixedHeight(30)
        
        # Add widgets to layout
        self.countdownLayout.addWidget(self.settingsButton)
        self.countdownLayout.addWidget(self.stateLabel)
        self.countdownLayout.addWidget(self.pomodoroRange)
        self.countdownLayout.addWidget(self.breaktimeRange)
        self.layout.addWidget(self.countdownButton)
        self.layout.addWidget(self.switchButton)

        # Connect signals
        self.settingsButton.clicked.connect(self.toggle_settings)

        self.pomodoroRange.userTimeChanged.connect(lambda n=self.pomodoroRange.time() : self.countdownTimer.set_time(n))
        self.breaktimeRange.userTimeChanged.connect(lambda n=self.breaktimeRange.time() : self.countdownTimer.set_time(n))
        
        self.countdownButton.clicked.connect(self.toggle_countdown)
        self.switchButton.clicked.connect(self.switch_state)
        
        self.countdownTimer.time_changed.connect(self.update_time_edit)
        self.countdownTimer.finished.connect(self.on_finished)

        self.set_theme()

    def toggle_settings(self):
        self.QMainWindow.screen_manager.switch_to_settings_screen(self.pomodoro_time, self.break_time)

    # Toggles countdown
    def toggle_countdown(self) -> None:
        self.countdownTimer.toggle()
        self.countdownButton.setText("Stop" if self.countdownTimer.running else "Start")
    
    # Switch between studying and break states
    def switch_state(self) -> None:
        self.on_finished()
        self.countdownButton.setText("Stop" if self.countdownTimer.running else "Start")
    
    # Update the QTimeRange respectively when the timer is running
    def update_time_edit(self, text: str) -> None:
        if self.on_break: self.breaktimeRange.setTime(QTime.fromString(text, "mm:ss"))
        else: self.pomodoroRange.setTime(QTime.fromString(text, "mm:ss"))
    
    # Update when the countdown finished
    def on_finished(self) -> None:
        # Set variables
        self.countdownButton.setText("Start")
        self.on_break = not self.on_break
        
        # Reset timer to new state
        if self.on_break:
            # Switch to break mode
            self.stateLabel.setText("Break: ")
            self.pomodoroRange.setTime(self.pomodoro_time)
            self.countdownTimer.set_time(self.break_time)
            self.pomodoroRange.hide()
            self.breaktimeRange.show()
        else:
            # Switch to study mode
            self.stateLabel.setText("Study: ")
            self.breaktimeRange.setTime(self.break_time)
            self.countdownTimer.set_time(self.pomodoro_time)
            self.breaktimeRange.hide()
            self.pomodoroRange.show()
        
        self.set_theme()
    
    # Function to get the break time
    def calculate_break_time(self) -> QTime:
        # Check if stopwatch time is less than 10 minutes
        if self.pomodoro_time.minute() < 10:
            # Set it to 5 minutes
            break_seconds = 300
        # Half the time if greater than 10 minutes
        else:
            # Convert pomodoro QTime to seconds
            pomo_secs = (
                self.pomodoro_time.hour() * 3600 +
                self.pomodoro_time.minute() * 60 +
                self.pomodoro_time.second()
            )

            break_seconds = int(pomo_secs / 1.5)
        
        # Convert to QTime
        h = break_seconds / 3600
        m = (break_seconds % 3600) / 60
        s = break_seconds % 60

        return QTime(h, m, s)

    def set_theme(self):
        theme = "cyan" if self.on_break else "pink"
        self.setProperty("theme", theme)
        self.QMainWindow.style_manager.apply_theme(theme, self)