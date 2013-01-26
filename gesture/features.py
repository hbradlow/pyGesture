"""
    A set of functions to compute features for gestures.

    Each feature is a function that takes a list of frames and returns a scalar or possibly multidimensional list.
"""
from lib import Leap
from gesture import utils
import numpy

def list_3d(size):
    """
        Returns an zero-filled 3d list of capacity size*size*size
    """
    return [[[0 for i in range(size)] for j in range(size)] for k in range(size)]

def velocity_histogram(type,bins=8,limit=(-1.,1.)):
    """
        Feature based on a 3d histogram of the normalized velocity vectors
    """

    def feature(frames):
        length = limit[1]-limit[0]
        bin_size = length/bins

        def hround(v):
            return min(bins-1,int((v-limit[0])/bin_size))

        l = list_3d(bins)
        for frame in frames:
            for element in frame[type]:
                v = element.velocity
                x = v[0]/numpy.linalg.norm(v)
                y = v[1]/numpy.linalg.norm(v)
                z = v[2]/numpy.linalg.norm(v)
                l[hround(x)][hround(y)][hround(z)] += 1
        return l

    return feature

def direction_histogram(type,bins=8,limit=(-1.,1.)):
    """
        Feature based on a 3d histogram of the normalized direction vectors
    """

    def feature(frames):
        length = limit[1]-limit[0]
        bin_size = length/bins

        def hround(v):
            return min(bins-1,int((v-limit[0])/bin_size))

        l = list_3d(bins)
        for frame in frames:
            for element in frame[type]:
                v = element.direction
                x = v[0]/numpy.linalg.norm(v)
                y = v[1]/numpy.linalg.norm(v)
                z = v[2]/numpy.linalg.norm(v)
                l[hround(x)][hround(y)][hround(z)] += 1
        return l

    return feature

def position_histogram(type,bins = 8,limit=(-1.,1.)):
    """
        Feature based on a 3d histogram of the normalized positions
    """
    def feature(frames):
        length = limit[1]-limit[0]
        bin_size = length/bins

        def hround(v):
            return min(bins-1,int((v-limit[0])/bin_size))

        l = list_3d(bins)
        positions = []
        for frame in frames:
            for element in frame[type]:
                p = element.position
                positions.append(p)
        if len(positions)>0:
            average_p = utils.ave_v(positions)
            for index,position in enumerate(positions):
                v = numpy.subtract(position,average_p)
                x = v[0]/numpy.linalg.norm(v)
                y = v[1]/numpy.linalg.norm(v)
                z = v[2]/numpy.linalg.norm(v)
                l[hround(x)][hround(y)][hround(z)] += 1
        return l

    return feature

def num_type_histogram(type,bins=10,limit=(0,10)):
    """
        Feature based on the histogram of the number of a certain type of element
    """
    def feature(frames):
        length = limit[1]-limit[0]
        bin_size = length/bins

        def hround(v):
            return min(bins-1,int((v-limit[0])/bin_size))

        l = [0 for i in range(bins)]
        for frame in frames:
            bin = hround(len(frame[type]))
            l[bin] += bin ** 10 #raise to a high power to magnify the difference

        return l

    return feature
