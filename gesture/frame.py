import collections 

class Frame(collections.Iterator):
    """
        A snapshot of a point in time from the 3D detection hardware.
        Intended to be subclassed for each type of hardware.
        A Frame consists of a collection of elements each 
        having certain parameters, for example coordinates, velocity,
        or acceleration. A Frame also contains metadata, for example
        the time the data was collected, ambient conditions, etc.
    """

    def __init__(self, *args, **kwargs):
        self.elements = []

    def __getitem__(self,type):
        """
            Return all the frame elements of this type
        """
        return [e for e in self.elements if e.type == type]

    def __add__(self,element):
        self.addElement(element)
        return self
    def addElement(self, element):
        self.elements.append(element)

    def next(self):
        """
            Return the next Element in this Frame.
        """
        for e in self.elements:
            yield e

class FrameElement:
    """
        A single data point from the 3D detection hardware.
        A FrameElement has, at the very least, coordinates
        x, y, and z. It may also have other properties,
        like acceleration or velocity.
    """
    def __init__(self, t, *args, **kwargs):
        self.type = t
