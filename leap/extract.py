import numpy
from leap.frame import *
from gesture.frame import *

def extract(data):
    """
        Extract a frame from the raw data
    """
    frame = Frame()
    for hand in data.hands:
        frame += HandElement(hand.palm_position,hand.palm_normal,hand.palm_velocity)
        for finger in hand.fingers:
            frame += FingerTipElement(finger.tip_position,finger.direction,finger.tip_velocity)
    return frame
