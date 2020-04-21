from animal_collection.animals import Animals 
from movements.digging import IDigging
class Earthworms(Animals, IDigging): 
    def __init__(self, name): 
        Animals.__init__(self, name)
        IDigging.__init__(self)
    