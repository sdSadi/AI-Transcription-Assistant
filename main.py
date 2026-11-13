# Main program file to run to open the app
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_userInterface import Ui_MainWindow
import resource_rc  # Load all the resource assets

# Create instance of Qt application
app = QApplication(sys.argv)

# Create the base window container and populate it with ui layout
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

# load the window and start the application event loop
window.show()
sys.exit(app.exec())
