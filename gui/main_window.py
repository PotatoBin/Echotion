import os
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import  Qt, QTimer, QSettings
from gui.preference_window import PreferenceDialog
from gui.information_window import InformationDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Echotion")
        self.setWindowIcon(QIcon("resources/icons/Echotion1.png"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.old_pos = None

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
        self.timer.start(1000)

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
    
    def mousePressEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None