from background import *
import rs232transmitterWindowCore
from rs232transmitterWindowCore import *
import PySide2.QtGui


class TransmitterWindow(QMainWindow):
    def __init__(self):
        super(TransmitterWindow, self).__init__()
        self.ui = rs232transmitterWindowCore.Ui_RS232transmitter()
        self.ui.setupUi(self)
        self.setWindowTitle("RS232 Transmission Simulator")
        self.ui.codeButton.clicked.connect(self.codeclick)
        self.ui.sendButton.clicked.connect(self.sendclick)
        self.ui.decodeButton.clicked.connect(self.decodeclick)
        self.ui.censoreBox.toggled.connect(self.checkboxcheck)
        self.coded_message = ''
        self.decoded_message = ''
        self.decoded_message_censored = ''
        self.input_message = ''
        self.message_sent = False

        f = open('dicts/dict.txt', 'r')
        self.dictionary = []
        for line in f:
            word = line.split('\n')[0]
            self.dictionary.append(word)

    def codeclick(self):
        self.input_message = self.ui.inputTextPlain.toPlainText()
        binary_string = string2binary(self.input_message, False)
        self.coded_message = binary_string
        self.ui.inputTextCoded.setText(self.coded_message)
        self.message_sent = False

    def sendclick(self):
        self.ui.reveivedTextCoded.setText(self.coded_message)
        self.message_sent = True

    def decodeclick(self):
        self.decoded_message = binary2string(self.coded_message)
        self.decoded_message = binary2string(self.coded_message)
        self.decoded_message_censored = censore_message(self.decoded_message, self.dictionary)
        if self.message_sent:
            if self.ui.censoreBox.isChecked():
                self.ui.receivedTextDecoded.setText(self.decoded_message_censored)
            else:
                self.ui.receivedTextDecoded.setText(self.decoded_message)

    def checkboxcheck(self):
        if self.ui.censoreBox.isChecked():
            self.ui.receivedTextDecoded.setText(self.decoded_message_censored)
        else:
            self.ui.receivedTextDecoded.setText(self.decoded_message)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            quit()
