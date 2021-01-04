class Score:
    """ Simple class to represent a score in a game """

    def __init__(self, name, score):
        """ Initializes private attributes

        Args:
            name (str): name of the player (cannot be empty)
            score (int): score of the player (cannot be negative)
        
        Raises:
            ValueError: name is empty or not string, score is not integer or negative
        """

        if type(name) is not str or not name:
            raise ValueError("Invalid name.")
        if type(score) is not int or score < 0:
            raise ValueError("Invalid score.")

        self._name = name
        self._score = score

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def __str__(self):
        """ Return a string of the player's score
            format -- Score: player_name (player.score)
        """
        return f"Score: {self.name} ({self.score})"

    def __lt__(self, other):
        if type(self) is not type(other):
            raise TypeError("Can't compare different object types!")

        return self.score < other.score

    def to_dict(self):
        """ Return a dictionary of current score """
        return {"name": self.name, "score": self.score}
