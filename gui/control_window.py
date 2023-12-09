from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout, QHBoxLayout,QWidget
from PySide6.QtCore import  Qt
from PySide6.QtGui import QIcon, QAction

from gui.preference_window import PreferenceDialog
from gui.information_window import InformationDialog

from utils.audio_streaming import stream_audio
from utils.audio_recognition import recognize_audio
from utils.emotion_classification import classify_emotion
from utils.subtitle import generate_subtitle


class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Echotion")
        self.setWindowIcon(QIcon("resources/icons/Echotion1.png"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        
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

        self.microphone_on = False
        self.microphone_button = QPushButton("Start", self)
        self.microphone_button.setStyleSheet("background-color: #FFB533; color: black;")
        self.microphone_button.clicked.connect(self.toggle_microphone)
        self.microphone_button.setFixedSize(80, 30)

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.microphone_button)
        button_layout.addStretch()

        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def show_information(self):
        dialog = InformationDialog(self)
        dialog.exec_()

    def show_preference(self):
        dialog = PreferenceDialog(self)
        dialog.exec_()

    def toggle_microphone(self):
        self.microphone_on = not self.microphone_on
        if self.microphone_on:
            self.microphone_button.setText("Stop")
            self.microphone_button.setStyleSheet("background-color: #FCECDB; color: black;")
        else:
            self.microphone_button.setText("Start")
            self.microphone_button.setStyleSheet("background-color: #FFB533; color: black;")
            #stop
    
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

    def audio_to_subtitle ():
        stream_audio()
        text = recognize_audio()
        emotion_type = classify_emotion(text)
        generate_subtitle(emotion_type ,text)