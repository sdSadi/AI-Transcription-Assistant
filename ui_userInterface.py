# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)
import resource_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 652)
        MainWindow.setMinimumSize(QSize(1008, 650))
        MainWindow.setMaximumSize(QSize(1008, 750))
        icon = QIcon()
        icon.addFile(":/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_sidebar = QFrame(self.centralwidget)
        self.frame_sidebar.setObjectName("frame_sidebar")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_sidebar.sizePolicy().hasHeightForWidth()
        )
        self.frame_sidebar.setSizePolicy(sizePolicy)
        self.frame_sidebar.setMaximumSize(QSize(200, 750))
        self.frame_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_sidebar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_leftTop = QFrame(self.frame_sidebar)
        self.frame_leftTop.setObjectName("frame_leftTop")
        self.frame_leftTop.setMinimumSize(QSize(0, 36))
        self.frame_leftTop.setMaximumSize(QSize(16777215, 36))
        self.frame_leftTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_leftTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_leftTop)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 2, 10, 6)
        self.label_files = QLabel(self.frame_leftTop)
        self.label_files.setObjectName("label_files")
        self.label_files.setMinimumSize(QSize(0, 28))
        font = QFont()
        font.setFamilies(["Arial Rounded MT"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_files.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_files)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_collapse = QPushButton(self.frame_leftTop)
        self.btn_collapse.setObjectName("btn_collapse")
        self.btn_collapse.setMinimumSize(QSize(28, 28))
        self.btn_collapse.setMaximumSize(QSize(32, 16777215))
        font1 = QFont()
        font1.setFamilies(["Arial Rounded MT"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_collapse.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn_collapse)

        self.verticalLayout.addWidget(self.frame_leftTop)

        self.tree_fileManager = QTreeWidget(self.frame_sidebar)
        font2 = QFont()
        font2.setFamilies(["Arial"])
        font2.setPointSize(18)
        font2.setBold(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font2)
        self.tree_fileManager.setHeaderItem(__qtreewidgetitem)
        self.tree_fileManager.setObjectName("tree_fileManager")
        self.tree_fileManager.header().setVisible(False)

        self.verticalLayout.addWidget(self.tree_fileManager)

        self.btn_userManual = QPushButton(self.frame_sidebar)
        self.btn_userManual.setObjectName("btn_userManual")

        self.verticalLayout.addWidget(self.btn_userManual)

        self.btn_settings = QPushButton(self.frame_sidebar)
        self.btn_settings.setObjectName("btn_settings")

        self.verticalLayout.addWidget(self.btn_settings)

        self.horizontalLayout.addWidget(self.frame_sidebar)

        self.frame_central = QFrame(self.centralwidget)
        self.frame_central.setObjectName("frame_central")
        self.frame_central.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_central)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_topButtons = QFrame(self.frame_central)
        self.frame_topButtons.setObjectName("frame_topButtons")
        self.frame_topButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_topButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_topButtons)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer1 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer1)

        self.btn_voiceRecord = QPushButton(self.frame_topButtons)
        self.btn_voiceRecord.setObjectName("btn_voiceRecord")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.btn_voiceRecord.sizePolicy().hasHeightForWidth()
        )
        self.btn_voiceRecord.setSizePolicy(sizePolicy1)
        self.btn_voiceRecord.setMinimumSize(QSize(200, 200))
        self.btn_voiceRecord.setMaximumSize(QSize(240, 240))
        self.btn_voiceRecord.setStyleSheet(
            "border-image: url(:/images/voice_recording.png);\n"
            "border-radius: 12px;\n"
            "padding-top: 140px;\n"
            'font: 700 9pt "Arial Rounded MT Bold";\n'
            "background-color: transparent;"
        )

        self.horizontalLayout_2.addWidget(self.btn_voiceRecord)

        self.horizontalSpacer2 = QSpacerItem(
            25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer2)

        self.btn_realTime = QPushButton(self.frame_topButtons)
        self.btn_realTime.setObjectName("btn_realTime")
        sizePolicy1.setHeightForWidth(
            self.btn_realTime.sizePolicy().hasHeightForWidth()
        )
        self.btn_realTime.setSizePolicy(sizePolicy1)
        self.btn_realTime.setMinimumSize(QSize(200, 200))
        self.btn_realTime.setMaximumSize(QSize(240, 240))
        self.btn_realTime.setStyleSheet(
            "border-image: url(:/images/real_time_speech.png);\n"
            "border-radius: 12px;\n"
            "padding-top: 140px;\n"
            'font: 700 9pt "Arial Rounded MT Bold";\n'
            "background-color: transparent;"
        )

        self.horizontalLayout_2.addWidget(self.btn_realTime)

        self.horizontalSpacer3 = QSpacerItem(
            25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer3)

        self.btn_audioUpload = QPushButton(self.frame_topButtons)
        self.btn_audioUpload.setObjectName("btn_audioUpload")
        sizePolicy1.setHeightForWidth(
            self.btn_audioUpload.sizePolicy().hasHeightForWidth()
        )
        self.btn_audioUpload.setSizePolicy(sizePolicy1)
        self.btn_audioUpload.setMinimumSize(QSize(200, 200))
        self.btn_audioUpload.setMaximumSize(QSize(240, 240))
        self.btn_audioUpload.setStyleSheet(
            "QPushButton {\n"
            "	border-image: url(:/images/audio_upload.png);\n"
            "	border-radius: 12px;\n"
            "	padding-top: 140px;\n"
            '	font: 700 9pt "Arial Rounded MT Bold";\n'
            "	background-color: transparent;\n"
            "}"
        )

        self.horizontalLayout_2.addWidget(self.btn_audioUpload)

        self.horizontalSpacer4 = QSpacerItem(
            40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer4)

        self.verticalLayout_2.addWidget(self.frame_topButtons)

        self.table_recentRecordings = QTableWidget(self.frame_central)
        if self.table_recentRecordings.columnCount() < 4:
            self.table_recentRecordings.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_recentRecordings.setObjectName("table_recentRecordings")
        self.table_recentRecordings.horizontalHeader().setVisible(True)
        self.table_recentRecordings.horizontalHeader().setStretchLastSection(True)
        self.table_recentRecordings.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.table_recentRecordings)

        self.horizontalLayout.addWidget(self.frame_central)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label_files.setText(
            QCoreApplication.translate("MainWindow", "Files", None)
        )
        self.btn_collapse.setText(
            QCoreApplication.translate("MainWindow", "\u2261", None)
        )
        ___qtreewidgetitem = self.tree_fileManager.headerItem()
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "Files", None)
        )
        self.btn_userManual.setText(
            QCoreApplication.translate("MainWindow", "Help and Guide", None)
        )
        self.btn_settings.setText(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
        self.btn_voiceRecord.setText(
            QCoreApplication.translate("MainWindow", "Voice Record", None)
        )
        self.btn_realTime.setText(
            QCoreApplication.translate("MainWindow", "Real Time", None)
        )
        self.btn_audioUpload.setText(
            QCoreApplication.translate("MainWindow", "Audio Upload", None)
        )
        ___qtablewidgetitem = self.table_recentRecordings.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate("MainWindow", "No.", None)
        )
        ___qtablewidgetitem1 = self.table_recentRecordings.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate("MainWindow", "Duration", None)
        )
        ___qtablewidgetitem2 = self.table_recentRecordings.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate("MainWindow", "Recordings", None)
        )
        ___qtablewidgetitem3 = self.table_recentRecordings.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate("MainWindow", "Date", None)
        )

    # retranslateUi
