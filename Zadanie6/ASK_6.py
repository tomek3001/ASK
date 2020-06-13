from PyQt5.uic.uiparser import QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
import sys
from ctypes import Structure
import timeit
from numpy.random import randint
import numpy as np
from random import random
import threading
import matplotlib.pyplot as plt
import os


class Texts(Structure):
    # Texts
    windowTitle_text = "Nasza aplikacja"
    login_text = "Zaloguj"
    loginLabel_text = "Użytkownik: "
    passwordLabel_text = "Hasło: "
    control_text = "OBECNY"
    temperature_text = "Temperatura urządzeń: "
    speed_text = "Prędkość pracy: "
    speedChange_text = "Zmiana prędkości taśmy."

    # Fonts
    login_font = QtGui.QFont()
    login_font.setPointSize(30)
    login_font.setStrikeOut(False)
    login_font.setKerning(True)
    login_font.setStyleStrategy(QtGui.QFont.PreferDefault)

    type_font = QtGui.QFont()
    type_font.setPointSize(20)
    type_font.setStrikeOut(False)
    type_font.setKerning(True)
    type_font.setStyleStrategy(QtGui.QFont.PreferDefault)


class Parameters(Structure):
    overheat_probability = 0.5
    block_probability = 0.5
    control_time = 20
    reaction_time = 5


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Core window config
        self.setWindowTitle(Texts.windowTitle_text)
        self.setFixedSize(800, 600)

        # Login window elements
        self.loginButton = QtWidgets.QPushButton(self)
        self.loginButton.setGeometry(self.generate_rect(50, 65, 150, 100))
        self.loginButton.setFont(Texts.login_font)
        self.loginButton.setText(Texts.login_text)
        self.loginButton.pressed.connect(self.login)

        self.loginLoginText = QtWidgets.QTextEdit(self)
        self.loginLoginText.setGeometry(self.generate_rect(60, 30, 300, 50))
        self.loginLoginText.setFont(Texts.type_font)

        self.loginPasswordText = QtWidgets.QLineEdit(self)
        self.loginPasswordText.setGeometry(self.generate_rect(60, 45, 300, 50))
        self.loginPasswordText.setFont(Texts.type_font)
        self.loginPasswordText.setEchoMode(QtWidgets.QLineEdit.Password)

        self.loginLoginLabel = QtWidgets.QLabel(self)
        self.loginLoginLabel.setText(Texts.loginLabel_text)
        self.loginLoginLabel.setFont(Texts.login_font)
        self.loginLoginLabel.setGeometry(self.generate_rect(26.7, 29, 210, 50))

        self.loginPasswordLabel = QtWidgets.QLabel(self)
        self.loginPasswordLabel.setText(Texts.passwordLabel_text)
        self.loginPasswordLabel.setFont(Texts.login_font)
        self.loginPasswordLabel.setGeometry(self.generate_rect(33, 44, 110, 50))

        # Program variables
        self.username = "admin"
        self.password = "admin"
        # self.username = ""
        # self.password = ""
        self.high_load = False
        self.time_since_control_popup = 0
        self.overheat_probability = Parameters.overheat_probability
        self.block_probability = Parameters.block_probability
        self.last_control_time = 0
        self.last_temperature_time = 0
        self.user_logged_in = False
        self.production_speed = 2
        self.devices_temperature = 50
        self.upper_temperature_rand = 4
        self.lower_temperature_rand = 3
        self.proper_work = True
        self.last_speed_change = -10

        # self.login_screen_visible(False)

        # Main screen elements
        self.controlButton = QtWidgets.QPushButton(self)
        self.controlButton.setGeometry(self.generate_rect(80, 80, 200, 200))
        self.controlButton.setFont(Texts.login_font)
        self.controlButton.setText(Texts.control_text)
        self.controlButton.pressed.connect(self.control)
        self.controlButton.setVisible(False)

        self.temperatureLabel = QtWidgets.QLabel(self)
        self.temperatureLabel.setGeometry(self.generate_rect(30, 30, 400, 200))
        self.temperatureLabel.setFont(Texts.type_font)
        self.temperatureLabel.setText(Texts.temperature_text + str(self.devices_temperature))

        self.speedLabel = QtWidgets.QLabel(self)
        self.speedLabel.setGeometry(self.generate_rect(30, 40, 400, 200))
        self.speedLabel.setFont(Texts.type_font)
        self.speedLabel.setText(Texts.speed_text + str(self.production_speed))

        self.speedChangeLabel = QtWidgets.QLabel(self)
        self.speedChangeLabel.setGeometry(self.generate_rect(50, 10, 500, 200))
        self.speedChangeLabel.setFont(Texts.login_font)
        self.speedChangeLabel.setText(Texts.speedChange_text)
        self.speedChangeLabel.setVisible(False)

        self.accidentLabel = QtWidgets.QLabel(self)

        # Hide main program
        self.main_screen_visible(False)

    def paintEvent(self, event):
        if self.user_logged_in:
            if timeit.default_timer() - self.last_control_time > Parameters.control_time:
                if not self.controlButton.isVisible():
                    self.controlButton.setVisible(True)
                    self.time_since_control_popup = timeit.default_timer()
                elif timeit.default_timer() - self.time_since_control_popup > Parameters.reaction_time:
                    self.logout()
                self.controlButton.setText(Texts.control_text
                                           + f"\n{round(Parameters.reaction_time + self.time_since_control_popup - timeit.default_timer() )}")

            if timeit.default_timer() - self.last_temperature_time > 1 and self.proper_work:
                self.generate_new_temperature()
                self.last_temperature_time = timeit.default_timer()

            if (0 < (timeit.default_timer() - self.last_speed_change) < 5) \
                    and round((timeit.default_timer() - self.last_speed_change))%2 == 0:
                self.speedChangeLabel.setVisible(True)
            elif self.speedChangeLabel.isVisible():
                self.speedChangeLabel.setVisible(False)
        self.update()

    def login(self):
        is_user_legit = self.check_user()
        self.loginLoginText.clear()
        self.loginPasswordText.clear()
        if is_user_legit:
            self.login_screen_visible(False)
            self.main_screen_visible(True)
            self.last_control_time = timeit.default_timer()
            self.user_logged_in = True

    def logout(self):
        self.login_screen_visible(True)
        self.main_screen_visible(False)
        self.controlButton.setVisible(False)
        self.user_logged_in = False
        self.speedChangeLabel.setVisible(False)

    def control(self):
        self.last_control_time = timeit.default_timer()
        self.controlButton.setVisible(False)

    def login_screen_visible(self, action):
        self.loginLoginLabel.setVisible(action)
        self.loginPasswordLabel.setVisible(action)
        self.loginButton.setVisible(action)
        self.loginLoginText.setVisible(action)
        self.loginPasswordText.setVisible(action)

    def main_screen_visible(self, action):
        self.temperatureLabel.setVisible(action)
        self.speedLabel.setVisible(action)
        self.accidentLabel.setVisible(action)

    def check_user(self):
        if self.loginLoginText.toPlainText() == self.username \
                and self.loginPasswordText.text() == self.password:
            return True
        else:
            return False

    def generate_new_temperature(self):
        if self.devices_temperature < 50:
            self.upper_temperature_rand = 4
            self.lower_temperature_rand = 1
        elif self.devices_temperature > 65:
            self.upper_temperature_rand = 2
            self.lower_temperature_rand = 3
        self.devices_temperature += randint(-self.lower_temperature_rand, self.upper_temperature_rand)
        self.temperatureLabel.setText(Texts.temperature_text + str(self.devices_temperature))
        self.generate_new_speed()

    def generate_new_speed(self):
        last_speed = self.production_speed
        if self.devices_temperature <= 60:
            self.production_speed = 2
        else:
            self.production_speed = 1
        if last_speed - self.production_speed != 0:
            self.last_speed_change = timeit.default_timer()
        self.speedLabel.setText(Texts.speed_text + str(self.production_speed))

    def generate_rect(self, x, y, width, height):
        """Button generator

        :param x: horizontal coordinate, (0, 100>% of window width
        :param y: vertical coordinate, (0, 100>% of window height
        :param width: button width
        :param height: button height
        :return:
        """
        new_x = x * self.width() / 100 - width / 2
        new_y = y * self.height() / 100 - height / 2
        return QtCore.QRect(new_x, new_y, width, height)


if __name__ == '__main__':
    myApp = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(myApp.exec_())
