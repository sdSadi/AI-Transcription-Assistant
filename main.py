# Main program file to run to open the app
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from mainWindow import MainWindow
import resource_rc  # Load all the resource assets

# Create instance of Qt application
app = QApplication(sys.argv)

# load the window and start the application event loop
window = MainWindow()
window.show()

sys.exit(app.exec())

# pyside6-uic userInterface.ui -o ui_userInterface.py
# pyside6-rcc resources.qrc -o resource_rc.py
