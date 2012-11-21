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
        pass

    def addElement(self, element):
        pass

    def next(self):
        """
            Return the next Element in this Frame.
        """
        pass
