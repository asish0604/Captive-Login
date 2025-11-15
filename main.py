import sys
import json
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QDialog,
    QLineEdit,
    QGraphicsDropShadowEffect,
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint
from PyQt6.QtGui import QFont, QColor
from wifi_login import login


def logger():
    with open("creds.json") as f:
        creds = json.load(f)
    username, password = creds["username"], creds["password"]
    login(username, password)


if "-l" in sys.argv or "--login" in sys.argv:
    logger()
    sys.exit(0)


def change(usr, passw):
    with open("creds.json", "r") as f:
        creds = json.load(f)
    creds["username"] = usr
    creds["password"] = passw
    with open("creds.json", "w") as f:
        json.dump(creds, f, indent=4)


def add_shadow(widget, blur=20, offset=5):
    """Add drop shadow effect to widget"""
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(blur)
    shadow.setXOffset(0)
    shadow.setYOffset(offset)
    shadow.setColor(QColor(0, 0, 0, 100))
    widget.setGraphicsEffect(shadow)


class ChangeCredentialsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Change Credentials")
        self.setFixedSize(400, 380)
        self.setModal(True)
        self.setup_ui()

    def setup_ui(self):
        # Set dialog background
        self.setStyleSheet(
            """
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #1a1a2e, stop:1 #16213e);
                border-radius: 15px;
            }
        """
        )

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 35, 30, 30)
        layout.setSpacing(15)

        # Title label with icon
        title_label = QLabel("🔐 Update Credentials")
        title_label.setFont(QFont("Segoe UI", 22, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #ffffff; margin-bottom: 10px;")
        layout.addWidget(title_label)

        # Subtitle
        subtitle = QLabel("Enter your new login information")
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #a0a0a0; margin-bottom: 20px;")
        layout.addWidget(subtitle)

        # Username entry
        username_label = QLabel("Username")
        username_label.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        username_label.setStyleSheet("color: #e0e0e0; margin-left: 5px;")
        layout.addWidget(username_label)

        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("Enter your username")
        self.username_entry.setFixedHeight(45)
        self.username_entry.setFont(QFont("Segoe UI", 12))
        self.username_entry.setStyleSheet(
            """
            QLineEdit {
                padding: 8px 15px;
                border: 2px solid #2a2d3a;
                border-radius: 10px;
                background-color: #1f2230;
                color: #ffffff;
                selection-background-color: #3b82f6;
            }
            QLineEdit:focus {
                border: 2px solid #3b82f6;
                background-color: #252836;
            }
            QLineEdit:hover {
                border: 2px solid #4a4d5a;
            }
        """
        )
        layout.addWidget(self.username_entry)

        layout.addSpacing(10)

        # Password entry
        password_label = QLabel("Password")
        password_label.setFont(QFont("Segoe UI", 10, QFont.Weight.DemiBold))
        password_label.setStyleSheet("color: #e0e0e0; margin-left: 5px;")
        layout.addWidget(password_label)

        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("Enter your password")
        self.password_entry.setFixedHeight(45)
        self.password_entry.setFont(QFont("Segoe UI", 12))
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_entry.setStyleSheet(
            """
            QLineEdit {
                padding: 8px 15px;
                border: 2px solid #2a2d3a;
                border-radius: 10px;
                background-color: #1f2230;
                color: #ffffff;
                selection-background-color: #3b82f6;
            }
            QLineEdit:focus {
                border: 2px solid #3b82f6;
                background-color: #252836;
            }
            QLineEdit:hover {
                border: 2px solid #4a4d5a;
            }
        """
        )
        layout.addWidget(self.password_entry)

        layout.addSpacing(20)

        # Change button
        change_button = QPushButton("Update Credentials")
        change_button.setFont(QFont("Segoe UI", 13, QFont.Weight.Bold))
        change_button.setFixedHeight(50)
        change_button.setCursor(Qt.CursorShape.PointingHandCursor)
        change_button.setStyleSheet(
            """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3b82f6, stop:1 #2563eb);
                color: white;
                border: none;
                border-radius: 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #2563eb, stop:1 #1d4ed8);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #1d4ed8, stop:1 #1e40af);
            }
        """
        )
        change_button.clicked.connect(self.handle_change)
        add_shadow(change_button, 15, 3)
        layout.addWidget(change_button)

        layout.addStretch()

        self.setLayout(layout)

    def handle_change(self):
        username = self.username_entry.text()
        password = self.password_entry.text()
        if username and password:
            change(username, password)
            self.accept()


class WifiLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WiFi Login Manager")
        self.setFixedSize(450, 420)
        self.setup_ui()

    def setup_ui(self):
        # Set dark gradient background
        self.setStyleSheet(
            """
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f0c29, stop:0.5 #302b63, stop:1 #24243e);
            }
        """
        )

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 40, 30, 30)
        layout.setSpacing(20)

        # Icon/Logo
        icon_label = QLabel("📶")
        icon_label.setFont(QFont("Segoe UI", 48))
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(icon_label)

        # Title label
        title_label = QLabel("WiFi Login Manager")
        title_label.setFont(QFont("Segoe UI", 26, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet(
            """
            color: #ffffff;
            margin-top: -10px;
            margin-bottom: 5px;
        """
        )
        layout.addWidget(title_label)

        # Subtitle
        subtitle = QLabel("Connect to your network instantly")
        subtitle.setFont(QFont("Segoe UI", 11))
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("color: #b0b0b0; margin-bottom: 15px;")
        layout.addWidget(subtitle)

        # Login button
        login_button = QPushButton("🚀 Login Now")
        login_button.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        login_button.setFixedHeight(60)
        login_button.setCursor(Qt.CursorShape.PointingHandCursor)
        login_button.setStyleSheet(
            """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
                border: none;
                border-radius: 15px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #764ba2, stop:1 #667eea);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #5a3d7a, stop:1 #4e63b8);
            }
        """
        )
        login_button.clicked.connect(self.handle_login)
        add_shadow(login_button, 20, 4)
        layout.addWidget(login_button)

        layout.addSpacing(5)

        # Change credentials button
        change_button = QPushButton("⚙️ Change Credentials")
        change_button.setFont(QFont("Segoe UI", 15, QFont.Weight.Bold))
        change_button.setFixedHeight(55)
        change_button.setCursor(Qt.CursorShape.PointingHandCursor)
        change_button.setStyleSheet(
            """
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #f093fb, stop:1 #f5576c);
                color: white;
                border: none;
                border-radius: 14px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #f5576c, stop:1 #f093fb);
            }
            QPushButton:pressed {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #d04557, stop:1 #c876d1);
            }
        """
        )
        change_button.clicked.connect(self.show_change_credentials_dialog)
        add_shadow(change_button, 20, 4)
        layout.addWidget(change_button)

        layout.addStretch()

        # Footer info
        footer = QLabel("Secure • Fast • Reliable")
        footer.setFont(QFont("Segoe UI", 9))
        footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer.setStyleSheet("color: #808080;")
        layout.addWidget(footer)

        central_widget.setLayout(layout)

    def handle_login(self):
        try:
            logger()
        except Exception as e:
            print(f"Login failed: {e}")

    def show_change_credentials_dialog(self):
        dialog = ChangeCredentialsDialog(self)
        dialog.exec()


def main():
    app = QApplication(sys.argv)

    # Set application-wide font
    app.setFont(QFont("Segoe UI", 10))

    window = WifiLoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
