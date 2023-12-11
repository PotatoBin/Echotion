import os
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import QTimer, QSettings
from gui.preference_window import PreferenceDialog
from gui.information_window import InformationDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Echotion")
        self.setWindowIcon(QIcon("resources/icons/Echotion1.png"))
        self.settings = QSettings("setting/config.ini", QSettings.IniFormat)
        background_color = self.settings.value("background_color", defaultValue="#00ff31")
        self.setStyleSheet(f"background-color: {background_color};")

        menubar = self.menuBar()
        echotion_menu = menubar.addMenu("Echotion")

        action_info = QAction("About Echotion", self)
        action_info.triggered.connect(self.show_information)
        echotion_menu.addAction(action_info)
        action_pref = QAction("Preference", self)
        action_pref.triggered.connect(self.show_preference)
        echotion_menu.addAction(action_pref)
        echotion_menu.addSeparator()
        action_exit = QAction("Quit", self)
        action_exit.triggered.connect(QApplication.instance().quit)
        echotion_menu.addAction(action_exit)
        self.menuBar().setVisible(True)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("resources/dummy.png"))

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image_periodically)
        self.timer.start(500)

    def update_image_periodically(self):
        self.settings = QSettings("setting/config.ini", QSettings.IniFormat)
        directory_path = self.settings.value("image_save_path", defaultValue="subtitle_history")
        files = os.listdir(directory_path)

        if files:
            image_files = [file for file in files if file.lower().endswith(('.png'))]

            if image_files:
                most_recent_file = max(image_files, key=lambda f: os.path.getmtime(os.path.join(directory_path, f)))

                image_path = os.path.join(directory_path, most_recent_file)

                pixmap = QPixmap(image_path)
                self.update_image(pixmap)
            
    def show_information(self):
        dialog = InformationDialog(self)
        dialog.exec_()

    def show_preference(self):
        dialog = PreferenceDialog(self)
        dialog.exec_()

    def update_image(self, pixmap) :
        if self.label:
            self.label.setPixmap(pixmap)