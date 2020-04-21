from animal_collection.animals import Animals 
from movements.walking import IWalking
class Ants(Animals, IWalking): 
    def __init__(self, name): 
        Animals.__init__(self, name)
        IWalking.__init__(self)
    