import sys
from PySide6.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.control_window import ControlWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    control = ControlWindow()
    window.show()
    control.show()
    sys.exit(app.exec())