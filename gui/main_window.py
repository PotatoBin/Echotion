from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QWidget
from PySide6.QtGui import QIcon, QAction, QPixmap
from PySide6.QtCore import QTimer
from gui.preference_window import PreferenceDialog
from gui.information_window import InformationDialog
from utils.subtitle import generate_subtitle

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Echotion")
        self.setWindowIcon(QIcon("resources/icons/Echotion1.png"))

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

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("resources/dummy.png"))

        self.microphone_on = False
        self.microphone_button = QPushButton("Start", self)
        self.microphone_button.clicked.connect(self.toggle_microphone)
        self.microphone_button.setFixedSize(80, 30)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        button_layout = QHBoxLayout()
        button_layout.addStretch()  # 왼쪽 공간
        button_layout.addWidget(self.microphone_button)
        button_layout.addStretch()  # 오른쪽 공간

        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_test)
        self.counter = 0 

    def toggle_microphone(self):
        self.microphone_on = not self.microphone_on
        if self.microphone_on:
            self.microphone_button.setText("Stop")
            self.microphone_button.setStyleSheet("background-color: #FCECDB; color: black;")
            self.start_test()
        else:
            self.microphone_button.setText("Start")
            self.microphone_button.setStyleSheet("background-color: #FFB533; color: black;")
            self.stop_test()

    def start_test(self):
        self.timer.start(1000) 

    def stop_test(self):
        self.timer.stop()
        self.counter = 0 

    def update_test(self):
        if self.counter <= 6:
            self.run_test(self.counter)
            self.counter += 1
        else:
            self.stop_test()

    def run_test(self, i):
        emotions = ["공포", "분노", "슬픔", "중립", "놀람", "행복", "혐오"]
        pixmap = generate_subtitle(i, emotions[i])
        self.update_image(pixmap)

    def show_information(self):
        dialog = InformationDialog(self)
        dialog.exec_()

    def show_preference(self):
        dialog = PreferenceDialog(self)
        dialog.exec_()

    def update_image(self, pixmap) :
        if not self.label:
            return
        self.label.setPixmap(pixmap)
