from sklearn import svm
import features
import pickle
import utils

feature_generators = [
    #finger stuff
    features.average_velocity,
    features.fingerVariance,
    features.avgFingers,

    #finger histograms
    features.position_histogram,
    features.velocity_histogram,

    #hand histograms
    features.hand_velocity_histogram,
    features.palm_normal_histogram,
    features.palm_position_histogram,
    #features.palm_position_variance,
]

class GestureLearner:
    def __init__(self):
        self.classifier = svm.LinearSVC()
        self.feature_vectors = []
        self.classifications = []
        self.keys = {}
        self.index = 0
        self.max_length = 0

    def get_feature_vector(self,gesture):
        """
            Calculate a vector of features for the given gesture
        """
        vector = []
        for generator in feature_generators:
            vector.append(generator(gesture))

        return [i for i in utils.flatten(vector)]

    def register_data(self,gestures,classifications):
        """
            Generate a list of feature vectors and train the classifier on them
        """
        feature_vectors = []

        for gesture in gestures:
            vector = self.get_feature_vector(gesture)
            feature_vectors.append(vector)

        for key in classifications: 
            if key not in self.keys:
                self.keys[key] = self.index
                self.index += 1
                
        self.feature_vectors += feature_vectors
        self.classifications += [self.keys[a] for a in classifications]

    def learn(self):
        self.classifier.fit(self.feature_vectors,self.classifications)

    def predict(self,gesture):
        """
            Predict a classification for the given feature
        """
        if len(gesture) > self.max_length:
            self.max_length = len(gesture)
        vector = self.get_feature_vector(gesture)
        num = self.classifier.predict([vector])[0]
        for key,value in self.keys.items():
            if value == num:
                return key

    def load_classifier(self, filename="classifier.pickle"):
        """
            Load the classifier
        """
        with open(filename,"r") as f:
            self.classifier = pickle.load(f)

    def save_classifier(self,filename="classifier.pickle"):
        """
            Save the classifier to a file
        """
        with open(filename,"w") as f:
            pickle.dump(self.classifier,f)

    def load_data(self,filename="data.pickle"):
        """
            Load the classifier from a file
        """
        with open(filename,"r") as f:
            self.feature_vectors,self.classifications,self.keys,self.index = pickle.load(f)

    def save_data(self,filename="data.pickle"):
        """
            Save the classifier to a file
        """
        with open(filename,"w") as f:
            pickle.dump([self.feature_vectors,self.classifications, self.keys,self.index],f)
