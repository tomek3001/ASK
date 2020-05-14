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
        self.coded_message = ''
        self.decoded_message = ''
        self.input_message = ''

    def codeclick(self):
        self.input_message = self.ui.inputTextPlain.toPlainText()
        binary_string = string2binary(self.input_message, False)
        self.coded_message = binary_string
        self.ui.inputTextCoded.setText(self.coded_message)

    def sendclick(self):
        self.ui.reveivedTextCoded.setText(self.coded_message)

    def decodeclick(self):
        self.decoded_message = binary2string(self.coded_message)
        self.ui.receivedTextDecoded.setText(self.decoded_message)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            quit()
