from gesture.learn import GestureLearner
from gesture import features
import leap.frame

class LeapLearner(GestureLearner):
    class Meta:
        feature_generators = [
            #position
            features.position_histogram(leap.frame.FINGER),
            features.position_histogram(leap.frame.HAND),
            #velocity
            features.velocity_histogram(leap.frame.FINGER),
            features.velocity_histogram(leap.frame.HAND),
            #direction
            features.direction_histogram(leap.frame.FINGER),
            features.direction_histogram(leap.frame.HAND),
            #average number of things
            features.num_type_histogram(leap.frame.FINGER),
            features.num_type_histogram(leap.frame.HAND),
        ]
