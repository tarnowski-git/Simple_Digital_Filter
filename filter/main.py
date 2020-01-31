import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class MainApplication(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Music Note Recognizer"
        self.top = 50
        self.left = 50
        self.width = 500
        self.height = 500
        self.iconName = "icons//logo_uksw.ico"
        self.initUI()

    def initUI(self):
        """Setting general configurations of the application"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.iconName))


def main():
    # You need one (and only one) QApplication instance per application.
    # Pass in sys.argv to allow command line arguments for your app.
    app = QtWidgets.QApplication(sys.argv)
    window = MainApplication()
    # IMPORTANT!!!!! Windows are hidden by default.
    window.show()
    # Start the event loop.
    app.exec()

    # Your application won't reach here until you exit and the event
    # loop has stopped.
