from PySide6.QtWidgets import QMainWindow  # Import the base window class from QtWidgets
from ui_userInterface import (
    Ui_MainWindow,
)  # Import the UI class generated from Qt Designer
from PySide6.QtCore import (
    Qt,
    QEvent,
    QPropertyAnimation,
    QEasingCurve,
    QSize,
)  # Import Qt features


# A custom main window that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):  # Create main window objects

        super().__init__()  # Initialize the parent class QMainWindow

        # Create an instance of the generated UI class and set it up
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Let MainWindow detect events happening in the audio upload button
        self.ui.btn_audioUpload.installEventFilter(self)

    def eventFilter(self, watched, event):

        # Checks whether the event belongs to the Audio Upload button
        if watched is self.ui.btn_audioUpload:

            # Mouse enters the button
            if event.type() == QEvent.Type.Enter:
                print("Mouse entered!")
                self.expand_button(watched)

            # Mouse leaves the button
            elif event.type() == QEvent.Type.Leave:
                print("Mouse left!")
                self.shrink_button(watched)

        # Allow Qt to continue processing the event normally
        return super().eventFilter(watched, event)

    def expand_button(self, button):

        # Create an animation for the button's size property
        animation = QPropertyAnimation(button, b"size")

        animation.setDuration(500)  # Set animation duration to 500ms

        # Define the initial and financial button dimensions
        animation.setStartValue(QSize(200, 200))
        animation.setEndValue(QSize(204, 204))

        # Make the animation slow down in the end for smooth effect
        animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        # Keep the animation alive so it does  not stop when the function ends
        self.animation = animation
        animation.start()  # Start the animation

    def shrink_button(
        self, button
    ):  # reverse the expand animation when cursor leaves the button
        animation = QPropertyAnimation(button, b"size")

        animation.setDuration(500)

        animation.setStartValue(QSize(204, 204))
        animation.setEndValue(QSize(200, 200))

        animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.animation = animation
        animation.start()
