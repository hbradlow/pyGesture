import sys
from lib import Leap
import Frame, FrameElement, FrameIterator

def Listner(Leap.Listener):
    def __init__(self, callback_class):
        super(Listener, self).__init__()
        self.callback_class = callback_class
    def onInit(self, controller):
        pass
    def onFrame(self, controller):
        self.callback_class.addFrame(controller.frame())

def LeapFrame(Frame.Frame):
    def __init__(self):
        pass
    def addElement(self):
        pass
    def next(self):

def LeapFrameElement(FrameElement.FrameElement):
    def __init__(self, x, y, z):
        pass

def LeapInterface(FrameIterator.FrameIterator):
    def __init__(self, callback=None):
        self.listner = Lisnter(self)
        self.frames = []
        self.callback = callback
    def addFrame(self, frame):
        if self.callback:
            self.callback(frame)
        else:
            self.frames.append(frame)
    def next(self):
        return self.frames.pop()

