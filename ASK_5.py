from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ctypes import Structure
import time
import keyboard
from numpy.random import randint as rand
import numpy as np
from random import random
import threading
import pygame
import shapes.resources
import timeit
import os


# Class containing all displayed subtitles
class TEXT(Structure):
    Invitation = "Hello, we are grateful that you wanted to take part in our psychomotor test." \
                 " There are 4 tasks ahead of you that will allow us to test your skills. Good luck!" \
                 "\nFirst you have to click button as fast as possible"
    window_title = "Psychomotor tests"
    start_button = "Press to start"

    test_button = "Let's some exercises"

    tab_1 = "Test"
    tab_2 = "Results"

    first_task = "Press buttons as fast as possible"
    second_task = "Your next task is to capture the sound as fast as possible wait for sound three times." \
                  "Press space if you heard sound"
    third_task = "Your third task is to check all the squares."
    click_me = "Click me!"

    your_score = "Your score in this test is: "

    next = "Press to continue"

    end = "Thanks you for participation"

    file_name = "smashing.wav"

    exercise_tool = "\nPress C to continue"


    hexagon = ":/hexagon"
    circle = ":/circle"
    square = ":/square"
    octagon = ":/octagon"

    shapes = [hexagon, circle, square, octagon]


class PARAMS(Structure):
    test_1_duration = 2  # time in secs
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
        self.graphicsView.setGeometry(0, 300, self.width(), self.height() - 300)
        self.createSquares()
        # Start Button
        self.startButton = QtWidgets.QPushButton(self.tab)
        self.startButton.setGeometry(QtCore.QRect(360, 350, 200, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.startButton.setFont(font)
        self.startButton.setText(TEXT.start_button)
        # Test button
        self.testButton = QtWidgets.QPushButton(self.tab)
        self.testButton.setGeometry(QtCore.QRect(360, 415, 200, 51))
        self.testButton.setFont(font)
        self.testButton.setText(TEXT.test_button)

        #Labels
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
        self.stop = 0
        self.reaction_time = 0
        self.mouse_press_pos = 0

        self.exercises = False
        self.graphicsView.setVisible(False)

        self.startButton.clicked.connect(self.startTest)
        self.firstTaskButton.clicked.connect(self.addPoint)
        self.continueButton.clicked.connect(self.tasksCounter)
        self.testButton.clicked.connect(self.exercisesTool)

    def createSquares(self):
        graphics_view_dimensions = self.width() - 2, self.height() - 302
        self.graphicsView.setSceneRect(0, 0, graphics_view_dimensions[0], graphics_view_dimensions[1])
        # self.graphicsView.set

        self.items = []
        self.all_squares = 0
        self.marked_squares = 0
        for item in range(10):
            self.items.append(QtWidgets.QGraphicsPixmapItem())
            # self.items[-1].setRotation(rand(0, 45))
            if item == 0:
                chosen_fig = TEXT.shapes[2]
                self.items[-1].shape_name = chosen_fig[2:]
                pixmap = QtGui.QPixmap(chosen_fig)
            else:
                chosen_fig = TEXT.shapes[rand(0, 4)]
                self.items[-1].shape_name = chosen_fig[2:]
                pixmap = QtGui.QPixmap(chosen_fig)
            if self.items[-1].shape_name == "square":
                self.all_squares += 1
            pixmap = pixmap.scaledToHeight(int(pixmap.height() / 15), QtCore.Qt.SmoothTransformation)
            self.items[-1].setPixmap(pixmap)
            self.items[-1].checked = False
            overlays = True
            while overlays:
                current_figure = self.items[-1].boundingRect().getRect()
                # set new position, from 10 to gw dimension minus figure dim (width/height)
                self.items[-1].setPos(rand(10, graphics_view_dimensions[0] - current_figure[2]),
                                      rand(10, graphics_view_dimensions[1] - current_figure[3]))
                self.items[-1].pos()
                current_figure_x = self.items[-1].pos().x()
                current_figure_y = self.items[-1].pos().y()
                current_figure_bbox = QtCore.QRectF(current_figure_x - int(current_figure_x / 2),
                                                    current_figure_y - int(current_figure_y / 2),
                                                    current_figure[2],
                                                    current_figure[3])
                if len(self.items) > 1:
                    for figure in self.items[:-1]:
                        tested_figure = figure.boundingRect().getRect()
                        tested_figure_x = figure.pos().x()
                        tested_figure_y = figure.pos().y()
                        tested_figure_bbox = QtCore.QRectF(tested_figure_x - int(tested_figure_x / 2),
                                                           tested_figure_y - int(tested_figure_y / 2),
                                                           tested_figure[2],
                                                           tested_figure[3])
                        if current_figure_bbox.intersects(tested_figure_bbox):
                            overlays = True
                            break
                        else:
                            overlays = False
                else:
                    break

            self.items[-1].setVisible(True)
            self.graphicsScene.addItem(self.items[-1])

    def exercisesTool(self):
        self.exercises = True
        self.startTest()

    def startTest(self):
        start = time.time()
        x, y = self.newPosition()
        self.pointCounter = 0
        self.startButton.setVisible(False)
        self.testButton.setVisible(False)
        if self.exercises:
            self.label.setText(TEXT.first_task + TEXT.exercise_tool)
        else:
            self.label.setText(TEXT.first_task)
        self.firstTaskButton.setVisible(True)
        self.firstTaskButton.setGeometry(x, y, 200, 51)
        self.thread = threading.Thread(target=self.wait, args=(start, PARAMS.test_1_duration,))
        self.thread.start()

    def tasksCounter(self):
        self.testNumber += 1
        self.continueButton.setVisible(False)
        if self.testNumber == 1:
            self.continueButton.setVisible(True)
            self.label.setText(TEXT.second_task)
        if self.testNumber == 2:
            self.thread = threading.Thread(target=self.makeSound)
            self.thread.start()
        if self.testNumber == 3:
            self.label.setText(TEXT.third_task)
            self.continueButton.setVisible(True)
        if self.testNumber == 4:
            self.graphicsView.setVisible(True)
            self.start = time.time()
        if self.testNumber == 5:
            if self.exercises:
                self.reset()
            else:
                self.endProgram()

    # Powrót do ustawień początkowych
    def reset(self):
        self.continueButton.setVisible(False)
        self.firstTaskButton.setVisible(False)
        self.pointCounter = 0
        self.testNumber = 0
        self.stop = 0
        self.reaction_time = 0
        self.mouse_press_pos = 0
        self.exercises = False
        self.graphicsView.setVisible(False)
        self.start = 0
        self.testButton.setVisible(True)
        self.startButton.setVisible(True)
        self.label.setText(TEXT.Invitation)

    def keyPressEvent(self, event):
        key = event.key()
        if key == 32:
            self.stop = time.time()
        if key == 67 and self.exercises:
            self.continueButton.setVisible(True)
            self.graphicsView.setVisible(False)

    def endProgram(self):
        self.label.setText(TEXT.end)
        self.update()
        self.close()

    # First test
    def wait(self, start, stop):
        if self.exercises:
            while not self.continueButton.isVisible():
                self.label.setText(TEXT.your_score + str(self.pointCounter))
        else:
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
    def makeSound(self):
        if self.exercises:
            while not self.continueButton.isVisible():
                time.sleep(rand(2, 6))
                pygame.mixer.init()
                pygame.mixer_music.load(TEXT.file_name)
                if not self.continueButton.isVisible():
                    pygame.mixer_music.play()
                start = time.time()  # zamieniłem kolejność, bo tak to czas reakcji był liczony
                # razem z czasem wczytania pliku
                while self.stop - start < 0:
                    pass
                self.reaction_time = time.time() - start
                self.label.setText(TEXT.your_score + str(self.reaction_time) + " s")
        else:
            for i in range(1):
                time.sleep(rand(2, 6))
                pygame.mixer.init()
                pygame.mixer_music.load(TEXT.file_name)
                pygame.mixer_music.play()
                start = time.time()  # zamieniłem kolejność, bo tak to czas reakcji był liczony
                # razem z czasem wczytania pliku
                while self.stop - start < 0:
                    pass
                self.reaction_time = time.time() - start
            self.label.setText(TEXT.your_score + str(self.reaction_time) + " s")
            self.continueButton.setVisible(True)

    def mousePressEvent(self, event):
        self.mouse_press_pos = event.pos().toTuple()
        if self.testNumber == 4:
            self.check_pressed_figure()

    def check_pressed_figure(self):
        if self.exercises:
            hit = False
            for figure in self.items:
                tested_figure = figure.boundingRect().getRect()
                tested_figure_x = figure.pos().x()
                tested_figure_y = figure.pos().y()
                tested_figure_xend = tested_figure_x + tested_figure[2]
                tested_figure_yend = tested_figure_y + tested_figure[3]
                if ((tested_figure_x < self.mouse_press_pos[0] < tested_figure_xend) and
                        (tested_figure_y < self.mouse_press_pos[1] - 300 < tested_figure_yend)):
                    if figure.shape_name == "square":
                        if figure.checked is False:
                            figure.checked = True
                            self.marked_squares += 1
                    hit = True
            if self.marked_squares == self.all_squares:
                self.label.setText(TEXT.your_score + str((time.time() - self.start) / self.marked_squares) + " s")
                self.start = time.time()
                self.graphicsScene.clear()
                self.createSquares()
        else:
            hit = False
            for figure in self.items:
                tested_figure = figure.boundingRect().getRect()
                tested_figure_x = figure.pos().x()
                tested_figure_y = figure.pos().y()
                tested_figure_xend = tested_figure_x + tested_figure[2]
                tested_figure_yend = tested_figure_y + tested_figure[3]
                if ((tested_figure_x < self.mouse_press_pos[0] < tested_figure_xend) and
                        (tested_figure_y < self.mouse_press_pos[1] - 300 < tested_figure_yend)):
                    if figure.shape_name == "square":
                        if figure.checked is False:
                            figure.checked = True
                            self.marked_squares += 1
                    hit = True
            if self.marked_squares == self.all_squares:
                self.label.setText(TEXT.your_score + str((time.time() - self.start)/self.marked_squares) + " s")
                self.continueButton.setVisible(True)
                self.graphicsView.setVisible(False)



if __name__ == '__main__':
    myApp = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(myApp.exec_())
