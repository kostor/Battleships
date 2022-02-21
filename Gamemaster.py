import random
from Player import Player
class Gamemaster:

    
    boat_sizes = [5, 4, 3, 3, 2] # boat sizes assuming usual game set
    fleet_size = len(boat_sizes) # this will make sure that we just 
                                 # need to change the boat configuration and the fleet size will automatically be updated
    def __init__(self):
        self.player1_locations = []
        self.player2_locations = []
        self.player1_orientations = []
        self.player2_orientations = []
        
        # randomize orientations for each ship in the fleet
        for index in range(Gamemaster.fleet_size):
            self.player1_orientations.append(random.randint(0,1))
            self.player2_orientations.append(random.randint(0,1))
        #for index in range(Gamemaster.fleet_size):
            
        
        # randomize locations based on orientations (to prevent index overflow when creating the map)
        for index in range(Gamemaster.fleet_size):
            if self.player1_orientations[index] != 1: # if ship is horizontal. This includes extreme cases where orientation is not 0 or 1
                self.player1_locations.append({"X": random.randint(1,10 - Gamemaster.boat_sizes[index]+1), "Y": random.randint(1,10)})
            else: # if ship is vertical
                self.player1_locations.append({"X": random.randint(1,10), "Y":random.randint(1,10-Gamemaster.boat_sizes[index]+1)})

            if self.player2_orientations[index] != 1:  # if ship is horizontal. This includes extreme cases where orientation is not 0 or 1
                self.player2_locations.append({"X": random.randint(1,10 - Gamemaster.boat_sizes[index]+1), "Y": random.randint(1,10)})
            else: # if ship is vertical
                self.player2_locations.append({"X": random.randint(1,10), "Y":random.randint(1,10-Gamemaster.boat_sizes[index]+1)})
        
        self.player1 = Player(self.player1_locations, self.player1_orientations)
        self.player2 = Player(self.player2_locations, self.player2_orientations)

    def get_player1(self):
        return self.player1
    def get_player2(self):
        return self.player2