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
    def __init__(self, type, *args, **kwargs):
        self.type = type

class FrameIterator(collections.Iterator):
    """
        Abstract class intended to be subclassed for each
        type of 3D input hardware. The FrameIterator is used 
        by a Recognizer to look at Frames in order.
    """

    def __init__(self):
        self.frames = []

    def __getitem__(self,index):
        return self.frames[index]

    def __add__(self,frame):
        self.addFrame(frame)
    def addFrame(self, frame):
        self.frames.append(frame)

    def next(self):
        """
            Returns the chronologically next Frame.
        """
        for f in self.frames:
            yield f
