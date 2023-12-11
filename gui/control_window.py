from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout,QWidget
from PySide6.QtCore import  QTimer, QSettings
from PySide6.QtGui import QIcon

from gui.preference_window import PreferenceDialog
from gui.information_window import InformationDialog

from utils.audio_streaming import stream_audio
from utils.audio_recognition import recognize_audio
from utils.emotion_classification import classify_emotion
from utils.subtitle_generation import generate_subtitle


class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Control Panel")
        self.setWindowIcon(QIcon("resources/icons/Echotion1.png"))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.audio_to_subtitle)
        self.settings = QSettings("setting/config.ini", QSettings.IniFormat)
        self.interval = int(self.settings.value("recording_interval", defaultValue=5))
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

    def audio_to_subtitle (self):
        self.microphone_button.setText("Listening...")
        self.microphone_button.setStyleSheet("background-color: #91CF1E; color: black;")
        audio_file_path = "stt_output.wav"
        stream_audio(audio_file_path, self.interval)
        self.microphone_button.setText("Loading...")
        self.microphone_button.setStyleSheet("background-color: #FDCF1E; color: black;")
        text = recognize_audio(audio_file_path)
        emotion_type = classify_emotion(text)
        generate_subtitle(emotion_type ,text)
        self.microphone_button.setText("Start")
        self.microphone_button.setStyleSheet("background-color: #FFB533; color: black;")
        
    def toggle_microphone(self):
        self.microphone_on = not self.microphone_on
        if self.microphone_on:
            self.audio_to_subtitle()
        else:
            self.microphone_button.setText("Start")
            self.microphone_button.setStyleSheet("background-color: #FFB533; color: black;")
    