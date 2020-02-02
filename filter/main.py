import sys
from PyQt5 import QtWidgets, QtCore, QtGui

from filter.plots import UnfilteredSignalPlot, FilteredSignalPlot


class MainApplication(QtWidgets.QMainWindow):

    # filter parameters
    FILTER_TYPES = ["lowpass", "highpass", "bandpass", "bandstop"]
    FILTER_ORDERS = ["1", "2", "3", "8", "8", "16"]

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
        self.width = 1200
        self.height = 700
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
        # create inputs & buttons
        self.createTopBar()
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

    def createTopBar(self):

        # input signal parameters y = Asin(2π * f * x) + Asin(2π * f * x)
        self.firstSinLabel = QtWidgets.QLabel("y1 = A * sin(2π * fs * x)")
        self.firstAmplitudeLineEdit = QtWidgets.QLineEdit()
        self.firstAmplitudeLineEdit.setPlaceholderText("1th Amplitude")

        self.firstFrequencyLineEdit = QtWidgets.QLineEdit()
        self.firstFrequencyLineEdit.setPlaceholderText("1th Frequency")

        self.secondSinLabel = QtWidgets.QLabel("y2 = A * sin(2π * fs * x)")
        self.secondAmplitudeLineEdit = QtWidgets.QLineEdit()
        self.secondAmplitudeLineEdit.setPlaceholderText("2nd Amplitude")

        self.secondFrequencyLineEdit = QtWidgets.QLineEdit()
        self.secondFrequencyLineEdit.setPlaceholderText("2nd Frequency")

        # filter parameters
        self.filterTypeLabel = QtWidgets.QLabel("Filter Type")
        self.filterTypeCombo = QtWidgets.QComboBox()
        self.filterTypeCombo.addItems(self.FILTER_TYPES)

        self.filterOrderLabel = QtWidgets.QLabel("Filter Order")
        self.filterOrderCombo = QtWidgets.QComboBox()
        self.filterOrderCombo.addItems(self.FILTER_ORDERS)

        self.cutoffLabel = QtWidgets.QLabel("Cuttof Frequency")

        self.passbandLineEdit = QtWidgets.QLineEdit()
        self.passbandLineEdit.setPlaceholderText("Passband Frequency")

        self.stopbandLineEdit = QtWidgets.QLineEdit()
        self.stopbandLineEdit.setPlaceholderText("Stopband Frequency")

        # plots parameters
        self.axSamplesLineEdit = QtWidgets.QLineEdit()
        self.axSamplesLineEdit.setPlaceholderText("Set count of samples X")

        self.grabSamplesLineEdit = QtWidgets.QLineEdit()
        self.grabSamplesLineEdit.setPlaceholderText(
            "Lets grab first x samples")

        # plot button
        self.plotButton = QtWidgets.QPushButton("&Plot")
        self.plotButton.setMinimumHeight(40)
        self.plotButton.setFont(QtGui.QFont("Arial", 10))
        self.plotButton.setStyleSheet("background-color: red; font: bold")

        # clear button
        self.clearButton = QtWidgets.QPushButton("&Clear")
        self.clearButton.setMinimumHeight(40)

        # events
        # self.button.clicked.connect(self.saveFunc)

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

    # ======== Top Bar function ========
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

        # create input signal group box
        inputSignalGroupBox = QtWidgets.QGroupBox(
            "&Sum of Sinusoidal Input Signals y = y1 + y2")
        layout1 = QtWidgets.QFormLayout()
        layout1.addRow(self.firstSinLabel)
        layout1.addRow(self.firstAmplitudeLineEdit,
                       self.firstFrequencyLineEdit)
        layout1.addRow(self.secondSinLabel)
        layout1.addRow(self.secondAmplitudeLineEdit,
                       self.secondFrequencyLineEdit)
        inputSignalGroupBox.setLayout(layout1)

        # create filter left parameters
        filterGroupBox = QtWidgets.QGroupBox("&Filter Parameters")
        layout2 = QtWidgets.QFormLayout()
        layout2.addRow(self.filterTypeLabel, self.filterOrderLabel)
        layout2.addRow(self.filterTypeCombo, self.filterOrderCombo)
        # layout2.addRow(QtWidgets.) add QLine if I find it in web
        layout2.addRow(self.cutoffLabel)
        layout2.addRow(self.stopbandLineEdit, self.passbandLineEdit)
        filterGroupBox.setLayout(layout2)

        plotsGroupBox = QtWidgets.QGroupBox("&Plots Parameters")
        layout3 = QtWidgets.QFormLayout()
        layout3.addRow(self.axSamplesLineEdit)
        layout3.addRow(self.grabSamplesLineEdit)
        plotsGroupBox.setLayout(layout3)

        # setup horizontal container for top bar
        horizontalBox = QtWidgets.QHBoxLayout()
        horizontalBox.setDirection(QtWidgets.QVBoxLayout.LeftToRight)
        horizontalBox.setSpacing(20)
        horizontalBox.addWidget(inputSignalGroupBox)
        horizontalBox.addWidget(filterGroupBox)
        horizontalBox.addWidget(plotsGroupBox)
        horizontalBox.addWidget(self.plotButton)
        horizontalBox.addWidget(self.clearButton)

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
