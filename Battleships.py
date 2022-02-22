from Gamemaster import Gamemaster 
from Map import Map

gamemaster = Gamemaster()

boats_map = Map(gamemaster.player1_locations,gamemaster.player1_orientations)
print(boats_map)

print("Ready? Set, Play!")