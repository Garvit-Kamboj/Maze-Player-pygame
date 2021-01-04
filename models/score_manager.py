import json
from models.score import Score


class ScoreManager:
    """ Class to manage a collection of scores
    
    Attributes:
        scores (list): the list of scores managed by the instance
    """

    def __init__(self):
        """ Initializes private attribute """
        self._scores = list()


    @property
    def scores(self):
        """ Returns a list of dictionaries (state of Score objects) """
        return [score.to_dict() for score in self._scores]


    def add_score(self, score):
        """ Append the new score into the scores list 
            Sort the list in desending order 
        """
        if type(score) is not Score:
            raise TypeError("Invalid score.")
        
        self._scores.append(score)
        self._scores = sorted(self._scores, reverse=True)


    def remove_user_score(self, user):
        """ Remove all score instances of the user passed in """
        self._scores = [score for score in self._scores if score.name != user]
        #another way to do it:
        # self._scores = list(filter(lambda o: o.name != name, self._scores))
        

    def __len__(self):
        """ returns the length of score list"""
        return len(self._scores)


    def serialize(self):
        """ Returns a list of dictionaries (state of Score objects) """
        return self.scores
        
    
    def to_json(self, filename):
        """ Write the scores to a json file."""
        with open(filename, 'w') as file:
            file.write(json.dumps({"scores": self.serialize()}))

    
    def from_json(self, filename):
        """ Read data from a json file and add it to the score manager instance"""
        if filename.split('.')[1] != 'json':
            raise TypeError("Only json files accepted")
        with open(filename, 'r') as file:
            data = json.load(file)
            for each in data["scores"]:
                self.add_score(Score(each["name"], each["score"]))

