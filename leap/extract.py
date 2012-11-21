import numpy
from leap.frame import *

def extract(data):
    """
        Extract a frame from the raw data
    """
    frame = Frame()
    for hand in data.hands():
        frame += HandElement(hand.palm().position,hand.normal(),hand.velocity())
        for finger in hand.fingers():
            frame += FingerTipElement(finger.tip().position,finger.tip().direction,finger.velocity())
    return frame
