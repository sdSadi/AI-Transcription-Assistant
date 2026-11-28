# Import sys for command-line arguments and program exit
import sys

from PySide6.QtWidgets import QApplication  # Manages the application and its event loop
from mainWindow import MainWindow  # Import custom main window class
import resource_rc  # Load compiled Qt resources

# Create instance of Qt application
app = QApplication(sys.argv)

# Create and display the main window
window = MainWindow()
window.show()

# Start the event loop and exit when the application closes
sys.exit(app.exec())

# pyside6-uic userInterface.ui -o ui_userInterface.py
# pyside6-rcc resource.qrc -o resource_rc.py
