from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class UnfilteredSignalPlot(FigureCanvasQTAgg):
    """

    Parameters
    ----------
    `parent` : master widget
        Represents a widget to act as the parent of the current object
    """

    def __init__(self, parent=None, width=5, height=2, dpi=70):
        # create the Figure
        fig = Figure(figsize=(width, height), dpi=dpi)   # figsize - in inch
        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)
        self.configureAxes()
        self.axes.plot([1, 2, 3], [1, 2, 3])

    def configureAxes(self):
        self.axes.set_title("Unfiltered Signal", size=13)
        self.axes.set_ylabel("Magnitude")
        self.axes.set_xlabel("Frequency [Hz]")  # Samples
        self.axes.grid(True)

    def cleanAxes(self):
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        self.axes.plot([1, 2, 3], [1, 2, 3])
        self.draw()


class FilteredSignalPlot(FigureCanvasQTAgg):
    """

    Parameters
    ----------
    `parent` : master widget
        Represents a widget to act as the parent of the current object
    """

    def __init__(self, parent=None, width=5, height=2, dpi=70):
        # create the Figure
        fig = Figure(figsize=(width, height), dpi=dpi)   # figsize - in inch
        FigureCanvasQTAgg.__init__(self, fig)
        self.setParent(parent)

        self.axes = fig.add_subplot(111)
        self.configureAxes()
        self.axes.plot([1, 2, 3], [1, 2, 3])

    def configureAxes(self):
        self.axes.set_title("Filtered Signal", size=13)
        self.axes.set_ylabel("Magnitude")
        self.axes.set_xlabel("Frequency [Hz]")  # Samples
        self.axes.grid(True)

    def cleanAxes(self):
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        self.axes.plot([1, 2, 3], [1, 2, 3])
        self.draw()
