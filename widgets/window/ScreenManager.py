from PySide6.QtCore import QTime
from widgets.stopwatch_widgets.QStopwatchScreen import QStopwatchScreen
from widgets.pomodoro_widgets.QPomodoroScreen import QPomodoroScreen
from widgets.settings_widgets.QSettingsScreen import QSettingsScreen

class ScreenManager():
    def __init__(self, window):
        self.window = window
        self.current_screen = None

    def switch_to_stopwatch_screen(self) -> None:
        self.deleteScreen()
        self.current_screen = QStopwatchScreen(self.window)
        self.window.wrapper.addWidget(self.current_screen)

    def switch_to_pomodoro_screen(self, qtime_value: QTime, pomo_time: QTime = None, break_time: QTime = None) -> None:
        self.deleteScreen()
        self.current_screen = QPomodoroScreen(qtime_value, self.window, pomo_time=pomo_time, break_time=break_time)
        self.window.wrapper.addWidget(self.current_screen)

    def switch_to_settings_screen(self, pomodoro_time: QTime, break_time: QTime) -> None:
        self.deleteScreen()
        self.current_screen = QSettingsScreen(pomodoro_time, break_time, self.window)
        self.window.wrapper.addWidget(self.current_screen)
    
    def deleteScreen(self):
        self.window.wrapper.removeWidget(self.current_screen)
        self.current_screen.deleteLater()