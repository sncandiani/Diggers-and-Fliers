from habitat_collection.habitats import Habitats
from movements import IWalking
class Cage(Habitats, IWalking): 
    def __init__(self, name):
        Habitats.__init__(self, name)
        IWalking.__init__(self)

    # Duck typing check
    def add_walker_pythonic(self, animal):
        try:
            if animal.walk_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_walker_type_check(self, animal):
        if isinstance(animal, IWalking):
            self.animals.add(animal)
        else:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')