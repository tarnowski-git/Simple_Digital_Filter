from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from math import pi, sin


class UnfilteredSignalPlot(FigureCanvasQTAgg):
    """Sum of Sinusoidal Input Signals y = y1 + y2.

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
        # create the axes
        self.axes = fig.add_subplot(111)
        self.configureAxes()
        self.draw()

    def plot(self, Am1 = 1, Fs1 = 1, Am2 = 1, Fs2 = 1, samples = 48000, section=4800):
        """Draw unfiltered signal."""
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        # create empty array
        y = [0] * samples
        # fill array with xxxHz signal
        for i in range(samples):
            y[i] = Am1 * sin(2 * pi * Fs1 * i/samples) + Am2 * sin(2 * pi * Fs2 * i/samples)
        # set range
        self.axes.set_xlim(0, section)
        self.axes.set_ylim(min(y), max(y))
        # create a plot
        self.axes.plot(y)
        self.draw()

    def configureAxes(self):
        self.axes.set_title("Unfiltered Signal", size=13)
        self.axes.set_ylabel("Magnitude")
        self.axes.set_xlabel("Frequency [Hz]")  # Samples
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(-1, 1)
        self.axes.grid(True)

    def cleanAxes(self):
        # clear current plot
        self.axes.clear()
        self.configureAxes()
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
        self.draw()

    def configureAxes(self):
        self.axes.set_title("Filtered Signal", size=13)
        self.axes.set_ylabel("Magnitude")
        self.axes.set_xlabel("Frequency [Hz]")  # Samples
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(-1, 1)
        self.axes.grid(True)

    def cleanAxes(self):
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        self.draw()
