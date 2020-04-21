from habitat_collection.habitats import Habitats
from movements import ISwimming
class Sea(Habitats, ISwimming): 
    def __init__(self, name):
        Habitats.__init__(self, name)
        ISwimming.__init__(self)

    # Duck typing check
    def add_swimmer_pythonic(self, animal):
        try:
            if animal.swim_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_swimmer_type_check(self, animal):
        if isinstance(animal, ISwimming):
            self.animals.add(animal)
        else:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')