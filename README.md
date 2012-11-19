pyGesture
=========

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
* [`utils.py`](https://github.com/hbradlow/pyGesture/blob/master/utils.py) - Some hacked together utility functions. These functions should probably be removed, and this project should switch to using numpy.array's instead of Leap.Vecor's.

Dependencies
------------

* [scikit-learn](http://scikit-learn.org/)
* [scipy](http://www.scipy.org/)
* [numpy](http://numpy.scipy.org/)
