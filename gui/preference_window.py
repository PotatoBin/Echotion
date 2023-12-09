from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QWidget, QColorDialog
)
from PySide6.QtCore import QSettings

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

        setting2 = QHBoxLayout()
        color_label = QLabel("Select Color: ")
        setting2.addWidget(color_label)

        color_button = QPushButton("Pick Color")
        color_button.setStyleSheet("background-color: #FFFFFF")  # Set default color
        color_button.clicked.connect(self.set_color)
        setting2.addWidget(color_button)

        main_layout.addLayout(setting2)
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

    def set_color(self):
        color_dialog = QColorDialog(self)
        color = color_dialog.getColor()
        if color.isValid():
            sender_button = self.sender()
            sender_button.setStyleSheet(f"background-color: {color.name()};")
            self.settings.setValue("selected_color", color.name())

    def save_settings(self):
        self.settings.sync()
