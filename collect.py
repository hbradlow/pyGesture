import sys
from lib import Leap 

import leap.learn
import leap.recorder
import leap.extract

class Listener:
    def __init__(self): 
        self.recording = False
        self.data = []

        #this part is variable
        self.leap_listener = leap.recorder.LeapListener(self.onFrame)
        self.controller = Leap.Controller(self.leap_listener)

    def onFrame(self, datum):
        if self.recording: 
            self.data.append(data)

    def start_recording(self): 
        self.recording = True

    def stop_recording(self): 
        self.recording = False 
        frames = [leap.extract.extract(datum) for datum in self.data]
        self.data = [] 
        return frames

def listen(gesture_list): 
    listener = Listener() 

    print "- Press Enter to toggle recording" 
    print "- Press 'q' + Enter to quit"
    print "[Record]",
    while True: 
        letter = sys.stdin.readline()
        if letter[0]  == 'q': 
            print "Done learning gesture"
            break
        if listener.recording: 
            print "Stoping record" 
            print "[Record] ",
            gesture_list.append(listener.stop_recording())
        else: 
            print " ** Recording ** "
            print "[Stop] ",
            listener.start_recording()

def guess(gLearner): 
    gesture_list = []
    listener = Listener() 
    while True: 
        letter = sys.stdin.readline()
        if letter[0]  == 'q': 
            print "Done recognizing"
            break
        if listener.recording: 
            print "Recognized ", gLearner.predict(listener.stop_recording())
            print "[Recognize] ",
        else: 
            print "Recording..."
            print "[Stop] ",
            listener.start_recording()


print """Usage:
        load        : Load a saved set of trained gestures
        learn       : Learn a new gesture 
        recognize   : Let the program guess what you are trying to input 
        q           : Quit""" 
print "[Command] ",
gLearner = leap.learn.LeapLearner() 
while True: 
    command = sys.stdin.readline()
    if "learn" in command: 
        print "Enter the name of the gesture: ", 

        gesture_name = sys.stdin.readline()
        gesture_list = []
        listen(gesture_list)

        gLearner.register_data(gesture_list, [gesture_name for i in gesture_list])
        gLearner.save_data()
    elif "recognize" in command: 
        gLearner.learn()
        guess(gLearner)     
        print "[Command] ", 
    elif command[0] == "q": 
        print "Goodbye"
        break
    elif "load" in command: 
        gLearner.load_data() 
        print "[Command] ",
    else: 
        print """Unrecognized command, usage:
        load        : Load a saved set of trained gestures
        learn       : Learn a new gesture 
        recognize   : Let the program guess what you are trying to input 
        q           : Quit""" 
        print "[Command] ",
