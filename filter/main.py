import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from filter.plots import UnfilteredSignalPlot, FilteredSignalPlot


class MainApplication(QtWidgets.QMainWindow):

    # The type of filter.
    FILTER_TYPES = ["lowpass", "highpass", "bandpass", "bandstop"]

    INFO = (
        "Student Project with:\n"
        "Digital Processing of Signal\n"
        "Cardinal Stefan Wyszynski University in Warsaw\n\n"
        "Author: Konrad Tarnowski\n"
        "MIT License © 2020"
    )

    def __init__(self):
        super().__init__()
        # setup parameters
        self.top = 50
        self.left = 50
        self.width = 800
        self.height = 600
        self.title = "Simple Butterworth Filter"
        self.iconName = "icons//logo_uksw.ico"
        # setup UI
        self.initUI()
        self.createWidgets()
        self.setupLayout()

    def initUI(self):
        """Setting general configurations of the application"""
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

    def createWidgets(self):
        """Creating the widgets of the application."""
        # create the Menubar
        self.addMenuBar()
        # create buttons
        self.addButtons()
        # create input unfiltered signal plot
        self.inputPlotCanvas = UnfilteredSignalPlot(self)
        # create output filtered signal
        self.outputPlotCanvas = FilteredSignalPlot(self)
        # create the status bar
        self.addStatusBar()

    def addMenuBar(self):
        """Creating the buttons on the top bar."""
        # create the Menu Bar from QMainWindow
        menuBar = self.menuBar()

        # create Root Menus
        fileMenu = menuBar.addMenu("&File")
        helpMenu = menuBar.addMenu("&Help")

        quitAction = QtWidgets.QAction('&Quit', self)
        quitAction.setShortcut("Ctrl+Q")

        aboutAction = QtWidgets.QAction("&About", self)
        versionAction = QtWidgets.QAction("&Version", self)

        # add actions to Menus
        fileMenu.addAction(quitAction)
        helpMenu.addAction(aboutAction)
        helpMenu.addAction(versionAction)

        # events
        quitAction.triggered.connect(self.closeApplication)
        aboutAction.triggered.connect(self.showAbout)
        versionAction.triggered.connect(self.showVersion)

    def addButtons(self):
        pass
        # self.combo = QtWidgets.QComboBox(self)
        # self.combo.addItems(self.FILTER_TYPES)
        # self.combo.move(150, 100)

        # self.button = QtWidgets.QPushButton("&Save", self)
        # self.button.clicked.connect(self.saveFunc)
        # self.button.move(150, 150)

    def addStatusBar(self):
        # create a label
        self.status = QtWidgets.QLabel()
        self.status.setText("Ready")
        # set label as StatusBar, and the label will be only changing
        self.statusBar().addWidget(self.status)

    # ======== Menu Bar function ========
    def closeApplication(self):
        """Close the application."""
        QtWidgets.qApp.quit()

    def showAbout(self):
        """Show information about project and author."""
        aboutMessage = QtWidgets.QMessageBox()
        aboutMessage.setWindowTitle(self.title)
        aboutMessage.setWindowIcon(QtGui.QIcon(self.iconName))
        aboutMessage.setText(self.INFO)
        aboutMessage.setIcon(QtWidgets.QMessageBox.Information)
        aboutMessage.exec_()

    def showVersion(self):
        versionMessage = QtWidgets.QMessageBox()
        versionMessage.setWindowTitle("Version")
        versionMessage.setText("Python 3.7.5 with PyQt5\nfor Windows")
        versionMessage.setWindowIcon(QtGui.QIcon(self.iconName))
        versionMessage.setIcon(QtWidgets.QMessageBox.Information)
        versionMessage.exec_()

    # ======== Buttons function ========
    def saveFunc(self):
        comboTXT = self.combo.currentText()
        print(comboTXT)

    # ======== Setup Layout ========
    def setupLayout(self):
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by defaul
        centralWidget = QtWidgets.QWidget()
        # vertical container will be a main layout
        mainLayout = QtWidgets.QVBoxLayout(centralWidget)
        # setup horizontal container for buttons
        horizontalBox = QtWidgets.QHBoxLayout()
        horizontalBox.setDirection(QtWidgets.QVBoxLayout.LeftToRight)
        mainLayout.addLayout(horizontalBox)
        mainLayout.addWidget(self.inputPlotCanvas)
        mainLayout.addWidget(self.outputPlotCanvas)
        self.setCentralWidget(centralWidget)


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
