from background import *
import rs232transmitterWindowCore
from rs232transmitterWindowCore import *


class TransmitterWindow(QMainWindow):
    def __init__(self):
        super(TransmitterWindow, self).__init__()
        self.ui = rs232transmitterWindowCore.Ui_RS232transmitter()
        self.ui.setupUi(self)
        self.setWindowTitle("RS232 Transmission Simulator")
        self.ui.codeButton.clicked.connect(self.codeclick)
        self.ui.sendButton.clicked.connect(self.sendclick)
        self.ui.decodeButton.clicked.connect(self.decodeclick)

    def codeclick(self):

        pass

    def sendclick(self):
        pass

    def decodeclick(self):
        pass
