from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QSlider, QWidget, QSizePolicy
)
from PySide6.QtCore import Qt, QSettings

class PreferenceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preference Settings")
        self.setFixedSize(600, 600)

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

        size_slider_layout = QHBoxLayout()
        label_size = QLabel("Window Size:")
        size_slider_layout.addWidget(label_size)
        self.size_slider = QSlider(Qt.Horizontal)
        self.size_slider.setMinimum(512)
        self.size_slider.setMaximum(1920)
        size_value = int(self.settings.value("window_size"))
        self.size_slider.setValue(size_value)
        self.size_slider.setTickInterval(12)
        self.size_slider.setTickPosition(QSlider.TicksBelow)
        self.size_slider.valueChanged.connect(self.slider_value_changed)
        size_slider_layout.addWidget(self.size_slider)
        self.slider_info_label = QLabel(f"{size_value}")
        self.slider_info_label.setAlignment(Qt.AlignCenter)
        size_slider_layout.addWidget(self.slider_info_label)
        main_layout.addLayout(size_slider_layout)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(spacer)

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

    def slider_value_changed(self):
        size_value = self.size_slider.value()
        self.slider_info_label.setText(f"{size_value}")
        self.resize(size_value, size_value)

    def save_settings(self):
        size_value = self.size_slider.value()
        self.settings.setValue("window_size", size_value)
        self.settings.sync()
