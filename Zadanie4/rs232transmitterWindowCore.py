# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rs232transmitterWindowCore.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_RS232transmitter(object):
    def setupUi(self, RS232transmitter):
        if not RS232transmitter.objectName():
            RS232transmitter.setObjectName(u"RS232transmitter")
        RS232transmitter.resize(800, 480)
        self.centralwidget = QWidget(RS232transmitter)
        self.centralwidget.setObjectName(u"centralwidget")
        self.inputTextPlain = QTextEdit(self.centralwidget)
        self.inputTextPlain.setObjectName(u"inputTextPlain")
        self.inputTextPlain.setGeometry(QRect(40, 30, 300, 130))
        self.inputTextPlain.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.inputTextCoded = QTextBrowser(self.centralwidget)
        self.inputTextCoded.setObjectName(u"inputTextCoded")
        self.inputTextCoded.setGeometry(QRect(40, 280, 300, 130))
        self.inputTextCoded.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.receivedTextDecoded = QTextBrowser(self.centralwidget)
        self.receivedTextDecoded.setObjectName(u"receivedTextDecoded")
        self.receivedTextDecoded.setGeometry(QRect(460, 30, 300, 130))
        self.receivedTextDecoded.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.reveivedTextCoded = QTextBrowser(self.centralwidget)
        self.reveivedTextCoded.setObjectName(u"reveivedTextCoded")
        self.reveivedTextCoded.setGeometry(QRect(460, 280, 300, 130))
        self.reveivedTextCoded.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.codeButton = QPushButton(self.centralwidget)
        self.codeButton.setObjectName(u"codeButton")
        self.codeButton.setGeometry(QRect(120, 190, 121, 61))
        self.codeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.decodeButton = QPushButton(self.centralwidget)
        self.decodeButton.setObjectName(u"decodeButton")
        self.decodeButton.setGeometry(QRect(490, 190, 121, 61))
        self.decodeButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.censoreBox = QCheckBox(self.centralwidget)
        self.censoreBox.setObjectName(u"censoreBox")
        self.censoreBox.setGeometry(QRect(680, 170, 70, 17))
        self.censoreBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.censoreBox.setChecked(True)
        self.sendButton = QPushButton(self.centralwidget)
        self.sendButton.setObjectName(u"sendButton")
        self.sendButton.setGeometry(QRect(360, 320, 81, 31))
        self.sendButton.setCursor(QCursor(Qt.PointingHandCursor))
        RS232transmitter.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(RS232transmitter)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        RS232transmitter.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(RS232transmitter)
        self.statusbar.setObjectName(u"statusbar")
        RS232transmitter.setStatusBar(self.statusbar)

        self.retranslateUi(RS232transmitter)

        QMetaObject.connectSlotsByName(RS232transmitter)
    # setupUi

    def retranslateUi(self, RS232transmitter):
        RS232transmitter.setWindowTitle(QCoreApplication.translate("RS232transmitter", u"MainWindow", None))
        self.codeButton.setText(QCoreApplication.translate("RS232transmitter", u"Code", None))
        self.decodeButton.setText(QCoreApplication.translate("RS232transmitter", u"Decode", None))
        self.censoreBox.setText(QCoreApplication.translate("RS232transmitter", u"Censore", None))
        self.sendButton.setText(QCoreApplication.translate("RS232transmitter", u"send -->", None))
    # retranslateUi

