import math
import numpy
import collections

def collapse(vec):
    return abs(vec.x)+abs(vec.y)+abs(vec.z)

def ave_v(vectors):
    l = range(len(vectors[0]))
    for v in vectors:
        for index,value in enumerate(v):
            l[index] += value
    for index,value in enumerate(l):
        l[index] /= len(vectors)

    return numpy.array(l)

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, basestring):
            for sub in flatten(el):
                yield sub
        else:
            yield el
