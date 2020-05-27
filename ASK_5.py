from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ctypes import Structure
import time
import keyboard

from PySide2.QtWidgets import QGraphicsPixmapItem
from numpy.random import randint as rand
import threading
from concurrent.futures import ThreadPoolExecutor

import resources

# Class containing all displayed subtitles
class TEXT(Structure):

    Invitation = "Hello, we are grateful that you wanted to take part in our psychomotor test." \
                 " There are 4 tasks ahead of you that will allow us to test your skills. Good luck!"
    window_title = "Psychomotor tests"
    start_button = "Press to start"

    tab_1 = "Test"
    tab_2 = "Results"

    first_task = "Press buttons as fast as possible"

    click_me = "Click me!"

    your_score = "Your score in this test is: "

    next = "Press to continue"

    end = "Thanks you for participation"


class PARAMS(Structure):
    test_1_duration = 1    # time in secs
    interval = 50000


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName(TEXT.window_title)
        self.resize(919, 789)
        self.centralwidget = QtWidgets.QWidget(self)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 921, 771))
        self.tab = QtWidgets.QWidget()
        self.graphicsScene = QtWidgets.QGraphicsScene(self.tab)
        self.graphicsView = QtWidgets.QGraphicsView(self.graphicsScene, self)
        self.graphicsView.setGeometry(0, 300, self.width(), self.height())
        self.startButton = QtWidgets.QPushButton(self.tab)
        self.startButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startButton.setFont(font)
        self.startButton.setText(TEXT.start_button)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setText(TEXT.Invitation)
        self.label.setGeometry(QtCore.QRect(160, 0, 600, 160))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.tabWidget.addTab(self.tab, TEXT.tab_1)
        self.tab_2 = QtWidgets.QWidget()
        self.tabWidget.addTab(self.tab_2, TEXT.tab_2)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.tabWidget.setTabEnabled(1, False)
        self.tabWidget.setCurrentIndex(0)
        # Continue button
        self.continueButton = QtWidgets.QPushButton(self.tab)
        self.continueButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.continueButton.setFont(font)
        self.continueButton.setText(TEXT.next)
        self.continueButton.setVisible(False)

        # First task button - reflex
        self.firstTaskButton = QtWidgets.QPushButton(self.tab)
        self.firstTaskButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.firstTaskButton.setFont(font)
        self.firstTaskButton.setText(TEXT.click_me)
        self.firstTaskButton.setVisible(False)
        self.pointCounter = 0
        self.testNumber = 0
        self.globalCursorPos = (-1, -1)


        # Second task button
        self.secondTaskButton = QtWidgets.QPushButton(self.tab)
        self.secondTaskButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.secondTaskButton.setFont(font)
        self.secondTaskButton.setText(TEXT.click_me)
        self.secondTaskButton.setVisible(False)

        self.graphicsView.setVisible(False)
        self.startButton.clicked.connect(self.startTest)
        self.firstTaskButton.clicked.connect(self.addPoint)
        self.continueButton.clicked.connect(self.tasksCounter)

    def mousePressEvent(self, event):
        self.globalCursorPos = (event.pos().x(), event.pos().y())
        time.sleep(0.5)
        self.globalCursorPos = (-1, -1)

    def startTest(self):
        start = time.time()
        x, y = self.newPosition()
        self.pointCounter = 0
        self.startButton.setVisible(False)
        self.label.setText(TEXT.first_task)
        self.firstTaskButton.setVisible(True)
        self.firstTaskButton.setGeometry(x, y, 200, 51)
        self.thread = threading.Thread(target=self.wait, args=(start, PARAMS.test_1_duration, ))
        self.thread.start()

    def tasksCounter(self):
        self.testNumber += 1
        self.continueButton.setVisible(False)
        if self.testNumber == 1:
            self.graphicsView.setVisible(True)
        if self.testNumber == 2:                 # TO TRZEBA ZMIENIĆ NIE KOŃCZYMY PO DWÓCH ZADANIACH
            self.endProgram()

    def keyPressEvent(self, event):
        key = event.key()
        if key == 32:
            pass



    def endProgram(self):
        self.label.setText(TEXT.end)
        self.update()
        self.close()

    # First test
    def wait(self, start, stop):
        while time.time() - start < stop:
            pass
        self.firstTaskButton.setVisible(False)
        self.label.setText(TEXT.your_score + str(self.pointCounter))
        self.continueButton.setVisible(True)

    def addPoint(self):
        self.pointCounter += 1
        x, y = self.newPosition()
        self.firstTaskButton.setGeometry(x, y, 200, 51)

    def newPosition(self):
        return rand(0, self.width() - 200), rand(0, self.height() - 102)

    # Second test






if __name__ == '__main__':
    myApp = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(myApp.exec_())