from animal_collection.animals import Animals 
from movements.swimming import ISwimming
class Terrapins(Animals, ISwimming): 
    def __init__(self, name): 
        Animals.__init__(self, name)
        ISwimming.__init__(self)
    