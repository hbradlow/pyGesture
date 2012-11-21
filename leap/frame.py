import interfaces.frame
import numpy
from lib import Leap

#types
FINGER = "leap_finger"
HAND = "leap_hand"

class FingerTipElement(interfaces.frame.FrameElement):
    def __init__(self,position,direction,velocity,*args,**kwargs):
        super(FingerTipElement,self).__init__(FINGER,*args,**kwargs)
        self.position = position
        self.direction = direction
        self.velocity = velocity

        if isinstance(position,Leap.Vector):
            self.position = numpy.array(position.x,position.y,position.z)
        if isinstance(direction,Leap.Vector):
            self.direction = numpy.array(direction.x,direction.x,direction.x)
        if isinstance(velocity,Leap.Vector):
            self.velocity = numpy.array(velocity.x,velocity.y,velocity.z)

class HandElement(interfaces.frame.FrameElement):
    def __init__(self,position,direction,velocity,*args,**kwargs):
        super(HandElement,self).__init__(HAND,*args,**kwargs)
        self.position = position
        self.direction = direction
        self.velocity = velocity

        if isinstance(position,Leap.Vector):
            self.position = numpy.array(position.x,position.y,position.z)
        if isinstance(direction,Leap.Vector):
            self.direction = numpy.array(direction.x,direction.x,direction.x)
        if isinstance(velocity,Leap.Vector):
            self.velocity = numpy.array(velocity.x,velocity.y,velocity.z)
