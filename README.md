pyGesture
=========

Install
------

    git clone git://github.com/hbradlow/pyGesture.git
    cd pyGesture
    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

Try it
------

To try it out, run

    python collect.py

To train new gestures, run

    [Command] learn

To load pretrained gestures, run

    [Command] load
    [Command] recognize

Files
-----

* [`collect.py`](https://github.com/hbradlow/pyGesture/blob/master/collect.py) - Script to handle collection of training/testing data
* [`features.py`](https://github.com/hbradlow/pyGesture/blob/master/features.py) - Functions that extract features from the raw data
* [`learn.py`](https://github.com/hbradlow/pyGesture/blob/master/learn.py) - Uses the scikit-learn svm to classify gestures based on a training set
* [`utils.py`](https://github.com/hbradlow/pyGesture/blob/master/utils.py) - Some hacked together utility functions. These functions should probably be removed, and this project should switch to using numpy.array's instead of Leap.Vectors.
* [`recognizer.py`](https://github.com/hbradlow/pyGesture/blob/master/recognizer.py) - Implements Leap.Listener and uses a sliding window to detect gestures from the frame stream.

Dependencies
------------

* [scikit-learn](http://scikit-learn.org/)
* [scipy](http://www.scipy.org/)
* [numpy](http://numpy.scipy.org/)
