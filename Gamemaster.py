import random
from Player import Player
from Map import Map
class Gamemaster:

    boat_marker = "M"
    boat_sizes = [5, 4, 3, 3, 2] # boat sizes assuming usual game set
    fleet_size = len(boat_sizes) # this will make sure that we just 
                                 # need to change the boat configuration and the fleet size will automatically be updated
    map_size = 10
    
    def __init__(self):
        self.player_boat_locations = []
        self.enemy_boat_locations = []
        self.player_orientations = []
        self.enemy_orientations = []
        
        self.attack_map = Map([], [], Gamemaster.boat_sizes, Gamemaster.map_size)
        self.defence_map = Map([],[], Gamemaster.boat_sizes, Gamemaster.map_size)

        # randomize orientations for each ship in the fleet
        for index in range(Gamemaster.fleet_size):
            self.player_orientations.append(random.randint(0,1))   
            self.enemy_orientations.append(random.randint(0,1))
        #for index in range(Gamemaster.fleet_size):
            
        
        # randomize locations based on orientations (to prevent index overflow when creating the map)
        for index in range(Gamemaster.fleet_size):
            if self.player_orientations[index] != 1: # if ship is horizontal. This includes extreme cases where orientation is not 0 or 1
                while True:
                    self.player_boat_locations.append({"X": random.randint(0,9 - Gamemaster.boat_sizes[index]+1), "Y": random.randint(0,9)})
                    
                    if Gamemaster.boat_marker not in self.defence_map.get_marker([self.player_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index]+1)], [self.player_boat_locations[index]["Y"]]):
                        self.defence_map.set_marker([self.player_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index])], [self.player_boat_locations[index]["Y"]], Gamemaster.boat_marker)
                        break
                    self.player_boat_locations.pop()
                
            else: # if ship is vertical
                while True:
                    self.player_boat_locations.append({"X": random.randint(0,9), "Y":random.randint(0,9-Gamemaster.boat_sizes[index]+1)})
                    
                    if Gamemaster.boat_marker not in self.defence_map.get_marker([self.player_boat_locations[index]["X"]], [self.player_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index]+1)]):
                        self.defence_map.set_marker([self.player_boat_locations[index]["X"]], [self.player_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index])], Gamemaster.boat_marker)
                        break
                    self.player_boat_locations.pop()

            if self.enemy_orientations[index] != 1:  # if ship is horizontal. This includes extreme cases where orientation is not 0 or 1
                while True:
                    self.enemy_boat_locations.append({"X": random.randint(0,9 - Gamemaster.boat_sizes[index]+1), "Y": random.randint(0,9)})
                    
                    if Gamemaster.boat_marker not in self.attack_map.get_marker([self.enemy_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index]+1)], [self.enemy_boat_locations[index]["Y"]]):
                        self.attack_map.set_marker([self.enemy_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index])], [self.enemy_boat_locations[index]["Y"]], Gamemaster.boat_marker)
                        break
                    self.enemy_boat_locations.pop()
            else: # if ship is vertical
                while True:
                    self.enemy_boat_locations.append({"X": random.randint(0,9), "Y":random.randint(0,9-Gamemaster.boat_sizes[index]+1)})
                    
                    if Gamemaster.boat_marker not in self.attack_map.get_marker([self.enemy_boat_locations[index]["X"]], [self.enemy_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index]+1)]):
                        self.attack_map.set_marker([self.enemy_boat_locations[index]["X"]], [self.enemy_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index])], Gamemaster.boat_marker)
                        break
                    self.enemy_boat_locations.pop()
        
        self.player = Player(self.player_boat_locations, self.player_orientations)
        self.enemy = Player(self.enemy_boat_locations, self.enemy_orientations)
        # print boat locations to make sure the correct locations are set.
        print("DEBUG--Gamemaster.py--REMOVE BEFORE LAUNCH")
        print(self.player_boat_locations)
        print(self.player_orientations)
        print("DEBUG END--Gamemaster.py--REMOVE BEFORE LAUNCH")
        print(self.defence_map)

    def get_player1(self):
        return self.player1
    def get_player2(self):
        return self.player2