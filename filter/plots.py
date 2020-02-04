import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from scipy.signal import butter, filtfilt, lfilter

from math import pi, sin
import matplotlib.pyplot as plt

class UnfilteredSignalPlot(FigureCanvasQTAgg):
    """Sum of Sinusoidal Input Signals y = y1 + y2.

    Parameters
    ----------
    `parent` : master widget
        Represents a widget to act as the parent of the current object.
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

    def plot(self, Am1 = 1, Fs1 = 1, Am2 = 1, Fs2 = 1, samples = 48000, section=4800, duration=10):
        """Draw unfiltered signal.
        Return y"""
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        # compute sines
        sine1 = self.sineGenerator(30, Fs1, duration)
        sine2 = self.sineGenerator(30, Fs2, duration)
        # create sum of sine
        sine = sine1 + sine2
        # set range
        self.axes.set_xlim(0, duration)
        self.axes.set_ylim(min(sine.data)*1.1, max(sine.data)*1.1)
        # create a plot
        self.axes.plot(sine.index, sine.data)
        self.draw()
        return sine

    def sineGenerator(self, sampleFrequency, sineFrequency, duration):
        # number of samples [1/sec * sec]
        nsamples = sampleFrequency * duration
        # angular frequency - how many degrees the particle travels per second
        w = 2.0 * np.pi * sineFrequency
        # set timeline
        t_sine = np.linspace(0, duration, nsamples, endpoint=False)
        # count y(t)
        y_sine = np.sin(w * t_sine)
        # pack func into pandas DataFrame
        result = pd.DataFrame({'data': y_sine}, index=t_sine)
        return result


    def configureAxes(self):
        self.axes.set_title("Generated Signal", size=13)
        self.axes.set_ylabel("Amplitude")
        self.axes.set_xlabel("Time [sec]")
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(-1, 1)
        self.axes.grid(True)

    def cleanAxes(self):
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        self.draw()


class FilteredSignalPlot(FigureCanvasQTAgg):
    """Canvas clas whitch compute and draws filtred signals. 

    Parameters
    ----------
    `parent` : master widget
        Represents a widget to act as the parent of the current object.
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

    def plot(self, order=10, lowcut=0.05, highcut=10, filterType="lowpass", samplingRate=1000, section=1000, unfilteredSig=None, duration=10):
        """Draw filtered signal."""
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        # choose appropriate type
        if filterType == "highpass":
            filtered_sine = self.butter_highpass_filter(data=unfilteredSig.data, cutoff=10, fs=30, order=10)
        elif filterType == "lowpass":
            filtered_sine = self.butter_lowpass_filter(data=unfilteredSig.data, cutoff=lowcut, fs=samplingRate, order=order)
        elif filterType == "bandpass":
            filtered_sine = self.butter_bandpass_filter(data=unfilteredSig.data, lowcut=lowcut, highcut=highcut, fs=samplingRate, order=order)
        elif filterType == "bandstop":
            filtered_sine = self.butter_bandstop_filter(data=unfilteredSig.data, lowcut=lowcut, highcut=highcut, fs=samplingRate, order=order)
        else:
            raise ValueError("Filter type in FilteredSignalPlot is not find!")
        # set range
        self.axes.set_xlim(0, duration)
        self.axes.set_ylim(min(filtered_sine)*1.1, max(filtered_sine)*1.1)
        # create a plot
        self.axes.plot(unfilteredSig.index, filtered_sine)
        self.draw()

    def butter_highpass(self, cutoff, fs, order=5):
        # Nyquist frequency | f = f / (fs/2) 
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='high', analog=False)
        return b, a

    def butter_highpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_highpass(cutoff, fs, order=order)
        y = filtfilt(b, a, data)
        return y

    def butter_lowpass(self, cutoff, fs, order=5):
        # Nyquist frequency | f = f / (fs/2)
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def butter_lowpass_filter(self, data, cutoff, fs, order=5):
        b, a = self.butter_lowpass(cutoff, fs, order=order)
        y = lfilter(b, a, data)
        return y

    def butter_bandpass(self, lowcut, highcut, fs, order=5):
        # Nyquist frequency | f = f / (fs/2)
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a

    def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=5):
        b, a = self.butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y

    def butter_bandstop_filter(self, data, lowcut, highcut, fs, order=5):
        # Nyquist frequency | f = f / (fs/2)
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        i, u = butter(order, [low, high], btype='bandstop')
        y = lfilter(i, u, data)
        return y

    def configureAxes(self):
        self.axes.set_title("Filtered Signal", size=13)
        self.axes.set_ylabel("Amplitude")
        self.axes.set_xlabel("Time [sec]")
        self.axes.set_xlim(0, 1)
        self.axes.set_ylim(-1, 1)
        self.axes.grid(True)

    def cleanAxes(self):
        # clear current plot
        self.axes.clear()
        self.configureAxes()
        self.draw()
