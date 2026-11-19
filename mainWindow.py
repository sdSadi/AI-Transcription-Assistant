from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QEvent, QPropertyAnimation, QEasingCurve, QSize
from ui_userInterface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setMouseTracking(True)

        self.ui.centralwidget.setMouseTracking(True)
        self.ui.frame_central.setMouseTracking(True)
        self.ui.frame_sidebar.setMouseTracking(True)

        self.ui.btn_audioUpload.installEventFilter(self)
        self.ui.btn_realTime.installEventFilter(self)
        self.ui.btn_voiceRecord.installEventFilter(self)

    def handle_audio(self):
        print("Audio Uploaded")

    # def mousePressEvent(self, event):
    #     print("Mouse pressed!")
    #     print("Position:", event.position())

    #     super().mousePressEvent(event)

    # def mouseMoveEvent(self, event):

    #     if event.buttons() & Qt.MouseButton.LeftButton:
    #         print("Dragging with left mouse button")

    #     super().mouseMoveEvent(event)

    def eventFilter(self, watched, event):

        if watched is self.ui.btn_audioUpload:
            if event.type() == QEvent.Type.Enter:
                print("Mouse entered!")
                self.expand_button(watched)

            elif event.type() == QEvent.Type.Leave:
                print("Mouse left!")
                self.shrink_button(watched)

        return super().eventFilter(watched, event)

    # def eventFilter(self, watched, event):

    #     if event.type() == QEvent.Type.Enter:
    #         print("ENTER detected:", watched.objectName())

    #     if watched is self.ui.btn_audioUpload:

    #         if event.type() == QEvent.Type.Enter:
    #             print("Mouse entered!")
    #             self.expand_button(watched)

    #         elif event.type() == QEvent.Type.Leave:
    #             print("Mouse left!")
    #             self.shrink_button(watched)

    #     return super().eventFilter(watched, event)

    def expand_button(self, button):
        animation = QPropertyAnimation(button, b"size")

        animation.setDuration(500)

        animation.setStartValue(QSize(200, 200))
        animation.setEndValue(QSize(204, 204))

        animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.animation = animation
        animation.start()

    def shrink_button(self, button):
        animation = QPropertyAnimation(button, b"size")

        animation.setDuration(500)

        animation.setStartValue(QSize(204, 204))
        animation.setEndValue(QSize(200, 200))

        animation.setEasingCurve(QEasingCurve.Type.OutCubic)

        self.animation = animation
        animation.start()
