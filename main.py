from PySide6.QtWidgets import QApplication
from widgets.window.QWindow import QWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = QWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()