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
    QRect,
)  # Import Qt features


# A custom main window that inherits from QMainWindow
class MainWindow(QMainWindow):
    def __init__(self):  # Create main window objects

        super().__init__()  # Initialize the parent class QMainWindow

        # Create an instance of the generated UI class and set it up
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # List of buttons which will have hover animation
        self.animated_buttons = [
            self.ui.btn_audioUpload,
            self.ui.btn_voiceRecord,
            self.ui.btn_realTime,
        ]

        # Install an Event Filter on each button
        for button in self.animated_buttons:
            button.installEventFilter(self)

        # Store a seperate animation and button
        self.animations = {}
        self.original_geometry = {}

        self.is_enabled = True

        self.ui.btn_collapse.clicked.connect(self.toggle_state)

        # List of all sidebar contents to hide when closing the sidebar
        self.sidebar_contents = [
            self.ui.btn_userManual,
            self.ui.btn_settings,
            self.ui.label_files,
            self.ui.tree_fileManager,
        ]

    def toggle_state(self):

        # Log the action based on current state before switched
        if self.is_enabled:
            self.change_width(self.ui.frame_sidebar, 50, False)
        else:
            self.change_width(self.ui.frame_sidebar, 187, True)

        # Flip the state upon a click
        self.is_enabled = not self.is_enabled

    def change_width(self, sidebar, target_width, visibility):

        self.sidebar_animation = QPropertyAnimation(sidebar, b"maximumWidth")

        self.sidebar_animation.setDuration(300)

        self.sidebar_animation.setStartValue(sidebar.width())  # Retrieve current width
        self.sidebar_animation.setEndValue(target_width)

        self.sidebar_animation.setEasingCurve(QEasingCurve.Type.InOutCubic)

        # Hide all the contents inside the sidebar
        for content in self.sidebar_contents:
            content.setVisible(visibility)

        self.sidebar_animation.start()
        self.original_geometry.clear()  # Ensure new original position set everytime to avoid bugs

    def eventFilter(self, watched, event):

        # Checks whether the event belongs to any of the input button
        if watched in self.animated_buttons:

            # Mouse enters the button
            if event.type() == QEvent.Type.Enter:
                if watched not in self.original_geometry:
                    self.original_geometry[watched] = watched.geometry()
                self.expand_button(watched)

            # Mouse leaves the button
            elif event.type() == QEvent.Type.Leave:
                self.shrink_button(watched)

        # Allow Qt to continue processing the event normally
        return super().eventFilter(watched, event)

    def expand_button(self, button):

        rect = button.geometry()
        original = self.original_geometry[button]
        expand_rect = QRect(
            original.x() - 5,
            original.y() - 5,
            original.width() + 10,
            original.height() + 10,
        )

        # Create an animation for the button's size property
        self.animations[button] = QPropertyAnimation(button, b"geometry")
        animation = self.animations[button]

        animation.setDuration(250)  # Set animation duration to 500ms

        # Define the initial and financial button dimensions
        animation.setStartValue(rect)
        animation.setEndValue(expand_rect)

        # Make the animation slow down in the end for smooth effect
        animation.setEasingCurve(QEasingCurve.Type.OutQuad)

        animation.start()  # Start the animation

    def shrink_button(
        self, button
    ):  # reverse the expand animation when cursor leaves the button
        self.animations[button] = QPropertyAnimation(button, b"geometry")
        animation = self.animations[button]
        original = self.original_geometry[button]

        animation.setDuration(250)

        animation.setStartValue(button.geometry())
        animation.setEndValue(original)

        animation.setEasingCurve(QEasingCurve.Type.OutQuad)

        animation.start()
