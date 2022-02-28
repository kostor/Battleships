from Gamemaster import Gamemaster 
from Map import Map

gamemaster = Gamemaster()

boats_map = Map(gamemaster.player1_locations,gamemaster.player1_orientations)
print(boats_map)
print('----------------')
print(boats_map.get_marker([1,2,3,4,5],[1,3]))
print('----------------')
print(boats_map.reset_map())
print("Ready? Set, Play!")