from rs232transmitterCustomWindow import *


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = TransmitterWindow()
    win.show()
    sys.exit(app.exec_())
