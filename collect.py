import sys
from lib import Leap 
from learn import GestureLearner

class Listener(Leap.Listener): 
    def __init__(self): 
        self.recording = False
        super(Listener, self).__init__()

    def onInit(self, controller): 
        self.frames = []

    def onFrame(self, controller): 
        if self.recording: 
            self.frames.append(controller.frame())

    def start_recording(self): 
        self.recording = True

    def stop_recording(self): 
        self.recording = False 
        return_list = [frame for frame in self.frames]
        self.frames = [] 
        return return_list

def listen(gesture_list): 
    listener = Listener() 
    controller = Leap.Controller(listener) 

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
    controller = Leap.Controller(listener)
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
gLearner = GestureLearner() 
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
