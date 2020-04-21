from animal_collection.animals import Animals 
from movements.flying import IFlying
class Parakeets(Animals, IFlying): 
    def __init__(self, name): 
        Animals.__init__(self, name)
        IFlying.__init__(self)
    