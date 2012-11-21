import collections
import frame

class FrameIterator(collections.Iterator):
    """
        Abstract class intended to be subclassed for each
        type of 3D input hardware. The FrameIterator is used 
        by a Recognizer to look at Frames in order.
    """

    def __init__(self):
        pass

    def addFrame(self, frame):
        pass

    def next(self):
        """
            Returns the chronologically next Frame.
        """
        pass
