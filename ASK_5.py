from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ctypes import Structure
import time
from numpy.random import randint as rand
import threading
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

class PARAMS(Structure):
    test_1_duration = 10    # time in secs


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName(TEXT.window_title)
        self.resize(919, 789)
        self.centralwidget = QtWidgets.QWidget(self)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 921, 771))
        self.tab = QtWidgets.QWidget()
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 920, 750))
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setText(TEXT.start_button)
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

        self.firstTaskButton = QtWidgets.QPushButton(self.tab)
        self.firstTaskButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.firstTaskButton.setFont(font)
        self.firstTaskButton.setText(TEXT.click_me)
        self.firstTaskButton.setVisible(False)
        self.pointCounter = 0

        self.pushButton.clicked.connect(self.startTest)
        self.firstTaskButton.clicked.connect(self.addPoint)

    def startTest(self):
        start = time.time()
        x, y = self.newPosition()
        self.pointCounter = 0
        self.pushButton.setVisible(False)
        self.label.setText(TEXT.first_task)
        self.firstTaskButton.setVisible(True)
        self.firstTaskButton.setGeometry(x, y, 200, 51)
        self.thread = threading.Thread(target=self.wait, args=(start, ))
        self.thread.start()

    def wait(self, start):
        while time.time() - start < PARAMS.test_1_duration:
            pass
        self.firstTaskButton.setVisible(False)
        print("Your points: ", self.pointCounter)
    def addPoint(self):
        self.pointCounter += 1
        x, y = self.newPosition()
        self.firstTaskButton.setGeometry(x, y, 200, 51)

    def newPosition(self):
        return rand(0, self.width() - 200), rand(0, self.height()-51)

if __name__ == '__main__':
    myApp = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(myApp.exec_())