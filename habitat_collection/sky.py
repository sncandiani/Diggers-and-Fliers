from habitat_collection.habitats import Habitats
from movements import IFlying
class Sky(Habitats, IFlying): 
    def __init__(self, name):
        Habitats.__init__(self, name)
        IFlying.__init__(self)
    

    # Duck typing check
    def add_flight_animal_pythonic(self, animal):
        try:
            if animal.flight_speed > -1:
                self.animals.add(animal)
        except AttributeError as ex:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')

    # Actual typing check
    def add_flight_animal_type_check(self, animal):
        if isinstance(animal, IFlying):
            self.animals.add(animal)
        else:
            print(f'{animal.name} can\'t swim, so please do not try to put it in the {self.name} habitat')