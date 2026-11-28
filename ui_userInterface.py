# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userInterface.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1008, 652)
        MainWindow.setMinimumSize(QSize(1008, 650))
        MainWindow.setMaximumSize(QSize(1008, 750))
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_sidebar = QFrame(self.centralwidget)
        self.frame_sidebar.setObjectName(u"frame_sidebar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_sidebar.sizePolicy().hasHeightForWidth())
        self.frame_sidebar.setSizePolicy(sizePolicy)
        self.frame_sidebar.setMinimumSize(QSize(30, 0))
        self.frame_sidebar.setMaximumSize(QSize(187, 750))
        self.frame_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_sidebar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, -1, 4, -1)
        self.frame_leftTop = QFrame(self.frame_sidebar)
        self.frame_leftTop.setObjectName(u"frame_leftTop")
        self.frame_leftTop.setMinimumSize(QSize(0, 36))
        self.frame_leftTop.setMaximumSize(QSize(16777215, 36))
        self.frame_leftTop.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.frame_leftTop.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_leftTop.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_leftTop)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 2, 4, 6)
        self.label_files = QLabel(self.frame_leftTop)
        self.label_files.setObjectName(u"label_files")
        self.label_files.setMinimumSize(QSize(0, 28))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_files.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_files)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_collapse = QPushButton(self.frame_leftTop)
        self.btn_collapse.setObjectName(u"btn_collapse")
        self.btn_collapse.setMinimumSize(QSize(28, 28))
        self.btn_collapse.setMaximumSize(QSize(32, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial Rounded MT"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.btn_collapse.setFont(font1)

        self.horizontalLayout_3.addWidget(self.btn_collapse)


        self.verticalLayout.addWidget(self.frame_leftTop)

        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.tree_fileManager = QTreeWidget(self.frame_sidebar)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(18)
        font2.setBold(False)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font2)
        self.tree_fileManager.setHeaderItem(__qtreewidgetitem)
        self.tree_fileManager.setObjectName(u"tree_fileManager")
        self.tree_fileManager.header().setVisible(False)

        self.verticalLayout.addWidget(self.tree_fileManager)

        self.frame_userManual = QFrame(self.frame_sidebar)
        self.frame_userManual.setObjectName(u"frame_userManual")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_userManual.sizePolicy().hasHeightForWidth())
        self.frame_userManual.setSizePolicy(sizePolicy1)
        self.frame_userManual.setMinimumSize(QSize(28, 36))
        self.frame_userManual.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.frame_userManual.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_userManual.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_userManual)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 2, 4, 2)
        self.btn_userManual = QPushButton(self.frame_userManual)
        self.btn_userManual.setObjectName(u"btn_userManual")
        sizePolicy1.setHeightForWidth(self.btn_userManual.sizePolicy().hasHeightForWidth())
        self.btn_userManual.setSizePolicy(sizePolicy1)
        self.btn_userManual.setMinimumSize(QSize(0, 32))
        self.btn_userManual.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	font: 700 9pt \"Arial Rounded MT Bold\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_userManual)

        self.btn_userManual_icon = QPushButton(self.frame_userManual)
        self.btn_userManual_icon.setObjectName(u"btn_userManual_icon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_userManual_icon.sizePolicy().hasHeightForWidth())
        self.btn_userManual_icon.setSizePolicy(sizePolicy2)
        self.btn_userManual_icon.setMinimumSize(QSize(32, 32))
        self.btn_userManual_icon.setMaximumSize(QSize(32, 32))
        self.btn_userManual_icon.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/images/userManual.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_userManual_icon.setIcon(icon1)
        self.btn_userManual_icon.setIconSize(QSize(34, 34))

        self.horizontalLayout_4.addWidget(self.btn_userManual_icon)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_userManual)

        self.frame = QFrame(self.frame_sidebar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 36))
        self.frame.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 2, 4, 2)
        self.btn_settings = QPushButton(self.frame)
        self.btn_settings.setObjectName(u"btn_settings")
        sizePolicy1.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy1)
        self.btn_settings.setMinimumSize(QSize(0, 32))
        self.btn_settings.setStyleSheet(u"QPushButton {\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	font: 700 9pt \"Arial Rounded MT Bold\";\n"
"}")

        self.horizontalLayout_5.addWidget(self.btn_settings)

        self.btn_settings_icon = QPushButton(self.frame)
        self.btn_settings_icon.setObjectName(u"btn_settings_icon")
        sizePolicy2.setHeightForWidth(self.btn_settings_icon.sizePolicy().hasHeightForWidth())
        self.btn_settings_icon.setSizePolicy(sizePolicy2)
        self.btn_settings_icon.setMinimumSize(QSize(32, 32))
        self.btn_settings_icon.setMaximumSize(QSize(32, 32))
        self.btn_settings_icon.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"    padding: 0px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/images/settings_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_settings_icon.setIcon(icon2)
        self.btn_settings_icon.setIconSize(QSize(34, 34))

        self.horizontalLayout_5.addWidget(self.btn_settings_icon)

        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout.setStretch(2, 1)

        self.horizontalLayout.addWidget(self.frame_sidebar)

        self.frame_central = QFrame(self.centralwidget)
        self.frame_central.setObjectName(u"frame_central")
        self.frame_central.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_central.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_central)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_topButtons = QFrame(self.frame_central)
        self.frame_topButtons.setObjectName(u"frame_topButtons")
        self.frame_topButtons.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.frame_topButtons.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_topButtons.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_topButtons)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer1)

        self.btn_voiceRecord = QPushButton(self.frame_topButtons)
        self.btn_voiceRecord.setObjectName(u"btn_voiceRecord")
        sizePolicy2.setHeightForWidth(self.btn_voiceRecord.sizePolicy().hasHeightForWidth())
        self.btn_voiceRecord.setSizePolicy(sizePolicy2)
        self.btn_voiceRecord.setMinimumSize(QSize(200, 200))
        self.btn_voiceRecord.setMaximumSize(QSize(240, 240))
        self.btn_voiceRecord.setStyleSheet(u"border-image: url(:/images/voice_recording.png);\n"
"border-radius: 12px;\n"
"padding-top: 140px;\n"
"font: 700 9pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.btn_voiceRecord)

        self.horizontalSpacer2 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer2)

        self.btn_realTime = QPushButton(self.frame_topButtons)
        self.btn_realTime.setObjectName(u"btn_realTime")
        sizePolicy2.setHeightForWidth(self.btn_realTime.sizePolicy().hasHeightForWidth())
        self.btn_realTime.setSizePolicy(sizePolicy2)
        self.btn_realTime.setMinimumSize(QSize(200, 200))
        self.btn_realTime.setMaximumSize(QSize(240, 240))
        self.btn_realTime.setStyleSheet(u"border-image: url(:/images/real_time_speech.png);\n"
"border-radius: 12px;\n"
"padding-top: 140px;\n"
"font: 700 9pt \"Arial Rounded MT Bold\";\n"
"background-color: transparent;")

        self.horizontalLayout_2.addWidget(self.btn_realTime)

        self.horizontalSpacer3 = QSpacerItem(25, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer3)

        self.btn_audioUpload = QPushButton(self.frame_topButtons)
        self.btn_audioUpload.setObjectName(u"btn_audioUpload")
        sizePolicy2.setHeightForWidth(self.btn_audioUpload.sizePolicy().hasHeightForWidth())
        self.btn_audioUpload.setSizePolicy(sizePolicy2)
        self.btn_audioUpload.setMinimumSize(QSize(200, 200))
        self.btn_audioUpload.setMaximumSize(QSize(240, 240))
        self.btn_audioUpload.setStyleSheet(u"QPushButton {\n"
"	border-image: url(:/images/audio_upload.png);\n"
"	border-radius: 12px;\n"
"	padding-top: 140px;\n"
"	font: 700 9pt \"Arial Rounded MT Bold\";\n"
"	background-color: transparent;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_audioUpload)

        self.horizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer4)


        self.verticalLayout_2.addWidget(self.frame_topButtons)

        self.table_recentRecordings = QTableWidget(self.frame_central)
        if (self.table_recentRecordings.columnCount() < 4):
            self.table_recentRecordings.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_recentRecordings.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_recentRecordings.setObjectName(u"table_recentRecordings")
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_files.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.btn_collapse.setText(QCoreApplication.translate("MainWindow", u"\u2261", None))
        ___qtreewidgetitem = self.tree_fileManager.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Files", None))
        self.btn_userManual.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_userManual_icon.setText("")
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_settings_icon.setText("")
        self.btn_voiceRecord.setText(QCoreApplication.translate("MainWindow", u"Voice Record", None))
        self.btn_realTime.setText(QCoreApplication.translate("MainWindow", u"Real Time", None))
        self.btn_audioUpload.setText(QCoreApplication.translate("MainWindow", u"Audio Upload", None))
        ___qtablewidgetitem = self.table_recentRecordings.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"No.", None))
        ___qtablewidgetitem1 = self.table_recentRecordings.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Duration", None))
        ___qtablewidgetitem2 = self.table_recentRecordings.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Recordings", None))
        ___qtablewidgetitem3 = self.table_recentRecordings.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None))
    # retranslateUi

