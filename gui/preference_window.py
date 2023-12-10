from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog
from PySide6.QtCore import QSettings
import os

class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preference Settings")
        self.setFixedSize(600, 400)

        self.settings = QSettings("setting/config.ini", QSettings.IniFormat)

        main_layout = QVBoxLayout()

        setting1 = QHBoxLayout()
        label_path = QLabel("Select Image Save Path")
        setting1.addWidget(label_path)

        save_path_button = QPushButton("Choose...")
        save_path_button.clicked.connect(self.set_image_save_path)
        save_path_button.setStyleSheet("background-color: #FCECDB; color: black;")
        setting1.addWidget(save_path_button)

        main_layout.addLayout(setting1)

        # Create a Delete Cache button
        delete_cache_button = QPushButton("Delete Cache")
        delete_cache_button.clicked.connect(self.delete_cache)
        delete_cache_button.setStyleSheet("background-color: #FCECDB; color: black;")
        main_layout.addWidget(delete_cache_button)

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

    def delete_cache(self):
        folder_path = self.settings.value("image_save_path")
        if folder_path:
            for file in os.listdir(folder_path):
                if file.endswith(".png") and file != "dummy.png":
                    os.remove(os.path.join(folder_path, file))

    def save_settings(self):
        self.settings.sync()
