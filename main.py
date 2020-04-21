from animal_collection import Ants, BettaFish, CopperheadSnake, Earthworms, Finches, Gerbils, Mice, Parakeets, Terrapins, TimberRattlesnake
from habitat_collection import Sea, Sky, Ground, Cage
# Instances of animals
mr_ant = Ants("Mr.Ant")
mr_beta = BettaFish("Mr.Beta")
mrs_copper = CopperheadSnake("Mrs.Copper")
mr_earth = Earthworms("Mr.Earth")
mr_finch = Finches("Mr.Finches")
mrs_mouse= Mice("Mrs.Copper")
mrs_keet = Parakeets("Mrs.Copper")
germy = Gerbils("Germy Gerbil")
terry = Terrapins("Terry pin")
timmy = TimberRattlesnake("Timmy Snake")
# Instances of habitats 
seaworld = Sea("Seaworld")
hawaiiansky = Sky("Hawaii")
groundlevel = Ground("Ground Level")
home = Cage("Comfy Cage")

seaworld.add_swimmer_type_check(mr_beta)
hawaiiansky.add_flight_animal_type_check(mr_finch)
# will not work because mrs copper does not belong to the proper class
groundlevel.add_digger_pythonic(mrs_copper)
groundlevel.add_digger_pythonic(mr_earth)
home.add_walker_pythonic(mr_ant)