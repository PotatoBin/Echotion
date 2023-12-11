from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, 
    QFileDialog, QColorDialog, QSlider, QLineEdit
)
from PySide6.QtCore import QSettings, Qt
import os

class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preference Settings")
        self.setFixedSize(600, 400)
        self.settings = QSettings("setting/config.ini", QSettings.IniFormat)

        main_layout = QVBoxLayout()

        # API Key Input
        api_key_layout = QHBoxLayout()
        label_api_key = QLabel("Enter API Key:")
        api_key_layout.addWidget(label_api_key)

        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Enter your API key")
        api_key_layout.addWidget(self.api_key_input)

        main_layout.addLayout(api_key_layout)

        # PT File Path Selection
        pt_file_layout = QHBoxLayout()
        label_pt_file = QLabel("Select .pt File:")
        pt_file_layout.addWidget(label_pt_file)

        select_pt_file_button = QPushButton("Choose...")
        select_pt_file_button.clicked.connect(self.set_pt_file_path)
        select_pt_file_button.setStyleSheet("background-color: #FCECDB; color: black;")
        pt_file_layout.addWidget(select_pt_file_button)
        main_layout.addLayout(pt_file_layout)

        # Image Save Path
        setting1 = QHBoxLayout()
        label_path = QLabel("Select Image Save Path")
        setting1.addWidget(label_path)

        save_path_button = QPushButton("Choose...")
        save_path_button.clicked.connect(self.set_image_save_path)
        save_path_button.setStyleSheet("background-color: #FCECDB; color: black;")
        setting1.addWidget(save_path_button)
        main_layout.addLayout(setting1)

        # Background Color Picker
        color_picker_layout = QHBoxLayout()
        label_color = QLabel("Select Background Color")
        color_picker_layout.addWidget(label_color)

        color_picker_button = QPushButton("Choose Color")
        color_picker_button.clicked.connect(self.set_background_color)
        background_color = self.settings.value("background_color", defaultValue="#FFFFFF")
        color_picker_button.setStyleSheet(f"background-color: {background_color}; color: black;")
        color_picker_layout.addWidget(color_picker_button)
        main_layout.addLayout(color_picker_layout)

        # Recording Interval Slider
        self.interval_slider = QSlider(Qt.Horizontal)
        self.interval_slider.setMinimum(3)
        self.interval_slider.setMaximum(7)
        recording_interval = self.settings.value("recording_interval", defaultValue=5)
        self.interval_slider.setValue(int(recording_interval))

        recording_interval_layout = QHBoxLayout()
        label_interval = QLabel("Recording Interval:")
        recording_interval_layout.addWidget(label_interval)

        self.slider_value_label = QLabel()  # Label to display slider value
        self.slider_value_label.setAlignment(Qt.AlignCenter)  # Align center
        self.update_slider_label(self.interval_slider.value())  # Set initial value
        recording_interval_layout.addWidget(self.slider_value_label)
        
        recording_interval_layout.addWidget(self.interval_slider)
        self.interval_slider.valueChanged.connect(self.slider_value_changed)

        main_layout.addLayout(setting1)
        main_layout.addLayout(recording_interval_layout)

        # Delete Cache Button
        delete_cache_button = QPushButton("Delete Cache")
        delete_cache_button.clicked.connect(self.delete_cache)
        delete_cache_button.setStyleSheet("background-color: #FCECDB; color: black;")
        main_layout.addWidget(delete_cache_button)

        # Close and Save Buttons
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

    def set_pt_file_path(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Select .pt File", "", "PT Files (*.pt)", options=options)
        if file_path:
            self.settings.setValue("pt_file_path", file_path)
            
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

    def set_background_color(self):
        color = QColorDialog.getColor(Qt.white, self, "Select Background Color")
        if color.isValid():
            hex_color = color.name()
            self.settings.setValue("background_color", hex_color)

    def update_slider_label(self, value):
        self.slider_value_label.setText(f" {value}")

    def slider_value_changed(self, value):
        self.update_slider_label(value)
        self.settings.setValue("recording_interval", value)

    def save_settings(self):
        api_key = self.api_key_input.text()
        self.settings.setValue("api_key", api_key)
        self.settings.sync()