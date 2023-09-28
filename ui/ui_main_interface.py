# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPlainTextEdit, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(455, 396)
        MainWindow.setMouseTracking(False)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.confirm_button = QPushButton(self.centralwidget)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setGeometry(QRect(190, 290, 61, 41))
        self.interval_la = QLabel(self.centralwidget)
        self.interval_la.setObjectName(u"interval_la")
        self.interval_la.setGeometry(QRect(110, 40, 101, 20))
        self.notigy_la = QLabel(self.centralwidget)
        self.notigy_la.setObjectName(u"notigy_la")
        self.notigy_la.setGeometry(QRect(110, 90, 91, 16))
        self.close_button = QPushButton(self.centralwidget)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(70, 290, 61, 41))
        self.close_button.setText(u"\u5173\u95ed\u63d0\u9192")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(220, 40, 121, 22))
        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(220, 90, 121, 22))
        self.cd_la = QLabel(self.centralwidget)
        self.cd_la.setObjectName(u"cd_la")
        self.cd_la.setGeometry(QRect(110, 140, 91, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QRect(220, 140, 121, 20))
        self.remake_button = QPushButton(self.centralwidget)
        self.remake_button.setObjectName(u"remake_button")
        self.remake_button.setGeometry(QRect(320, 290, 61, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 190, 71, 16))
        self.radioBu_open = QRadioButton(self.centralwidget)
        self.radioBu_open.setObjectName(u"radioBu_open")
        self.radioBu_open.setGeometry(QRect(220, 190, 41, 19))
        self.radioBu_open.setChecked(True)
        self.radioBu_close = QRadioButton(self.centralwidget)
        self.radioBu_close.setObjectName(u"radioBu_close")
        self.radioBu_close.setGeometry(QRect(300, 190, 41, 19))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 240, 61, 16))
        self.hint_pt = QPlainTextEdit(self.centralwidget)
        self.hint_pt.setObjectName(u"hint_pt")
        self.hint_pt.setGeometry(QRect(190, 220, 171, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 455, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.confirm_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d77\u6765\u7ad9\u7ad9", None))
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.interval_la.setText(QCoreApplication.translate("MainWindow", u"\u95f4 \u9694 \u65f6 \u95f4(m)", None))
        self.notigy_la.setText(QCoreApplication.translate("MainWindow", u"\u63d0 \u9192 \u6b21 \u6570(s)", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"80", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"60", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"45", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"30", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"20", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"1", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.cd_la.setText(QCoreApplication.translate("MainWindow", u"\u5012 \u8ba1 \u65f6 (s)", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.remake_button.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u65b0\u8ba1\u65f6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5faa \u73af \u5f00 \u5173", None))
        self.radioBu_open.setText(QCoreApplication.translate("MainWindow", u"\u5f00", None))
        self.radioBu_close.setText(QCoreApplication.translate("MainWindow", u"\u5173", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u63d0  \u793a  \u8bed", None))
    # retranslateUi

