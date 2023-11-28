from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QWidget, QSizePolicy
)
from PySide6.QtCore import QSettings

class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preference Settings")
        self.setFixedSize(600, 400)

        self.settings = QSettings("setting/config.ini", QSettings.IniFormat)

        main_layout = QVBoxLayout()

        path_layout = QHBoxLayout()
        label_path = QLabel("Select Image Save Path")
        path_layout.addWidget(label_path)

        save_path_button = QPushButton("Choose...")
        save_path_button.clicked.connect(self.set_image_save_path)
        save_path_button.setStyleSheet("background-color: #FCECDB; color: black;")
        path_layout.addWidget(save_path_button)

        main_layout.addLayout(path_layout)
        main_layout.addWidget(QWidget(), 1)

        button_layout = QHBoxLayout()
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        close_button.setStyleSheet("background-color: #FCECDB; color: black;")
        button_layout.addWidget(close_button)

        save_button = QPushButton("Save")
        save_button.clicked.connect(self.save_settings)
        save_button.setStyleSheet("background-color: #FFB533; color: black;")
        button_layout.addWidget(save_button)

        main_layout.addLayout(button_layout)
        main_layout.setSpacing(5)

        self.setLayout(main_layout)

    def set_image_save_path(self):
        options = QFileDialog.Options()
        directory = QFileDialog.getExistingDirectory(self, "Select Directory", options=options)
        if directory:
            self.settings.setValue("image_save_path", directory)

    def save_settings(self):
        self.settings.sync()