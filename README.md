# Simple Butterworth Filter Graph Plotting Application

Desktop GUI applications to show Butterworth filtration graph of the sum of sinusoidal signals with bandwidth and bandpass frequencies using Python 3.7 with PyQT5 graphical modul. The appliction allowing to choose type of filtration and filter appropriate parameters.

The [Butterworth filter](https://en.wikipedia.org/wiki/Butterworth_filter) is a type of signal processing filter designed to have a frequency response as flat as possible in the passband. It is also referred to as a maximally flat magnitude filter.

## Demo

![demo](https://user-images.githubusercontent.com/34337622/73711664-dc06d580-4707-11ea-8080-941172ae8512.gif)

## Technologies

-   Python 3.7
-   PyQT5 graphic module
-   NumPy module
-   SciPy module
-   Matplotlib module
-   pandas modul

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/Simple_Digital_Filter.git
```

-   Setup your [local environment](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python simple_filter.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --onefile --windowed simple_filter.py
```

## [License](https://github.com/tarnowski-git/Simple_Digital_Filter/blob/master/LICENSE)

MIT © [Konrad Tarnowski](https://github.com/tarnowski-git)
