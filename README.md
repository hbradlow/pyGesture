pyGesture
=========

Try it
------

To try it out, run
    python collect.py

To load pretrained gestures, run
    [Command] load
    [Command] recognize

To train new gestures, run
    [Command] learn

Files
-----

* [`collect.py`](https://github.com/hbradlow/pyGesture/blob/master/collect.py) - Script to handle collection of training/testing data
* [`features.py`](https://github.com/hbradlow/pyGesture/blob/master/features.py) - Functions that extract features from the raw data
* [`learn.py`](https://github.com/hbradlow/pyGesture/blob/master/learn.py) - Uses the scikit-learn svm to classify gestures based on a training set

Dependencies
------------

* ['scikit-learn'](http://scikit-learn.org/)
* ['scipy'](http://www.scipy.org/)
* ['numpy'](http://numpy.scipy.org/)
