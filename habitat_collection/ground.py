from habitat_collection.habitats import Habitats
from movements import IDigging
class Ground(Habitats, IDigging): 
    def __init__(self, name):
        Habitats.__init__(self, name)
        IDigging.__init__(self)

    # Duck typing check
    def add_digger_pythonic(self, animal):
        try:
            if animal.dig_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_digger_type_check(self, animal):
        if isinstance(animal, IDigging):
            self.animals.add(animal)
        else:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')