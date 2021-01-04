class Item():
    """This class instantiates an Item with its name and its family (to make game more interactive)"""
    def __init__(self, name, family):
        self.name = name
        self.family = family
    
    def __str__(self):
        return f"({self.name} of family {self.family})"


