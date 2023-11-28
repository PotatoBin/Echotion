from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap

class InformationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Echotion")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout(self)

        logo_label = QLabel()
        pixmap = QPixmap("resources/icons/logo.svg").scaled(100, 100)
        logo_label.setPixmap(pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        title_label = QLabel("<b>Echotion</b>")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        version_label = QLabel("Version 1.0")
        version_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(version_label)

        license_label = QLabel("MIT License")
        license_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(license_label)

        layout.addStretch()
