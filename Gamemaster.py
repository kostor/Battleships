import random
import Player
class Gamemaster:

    
    boat_sizes = [5, 4, 3, 3, 2] # boat sizes assuming usual 
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
        for index in range(Gamemaster.fleet_size):
            self.player2_orientations.append(random.randint(0,1))

        for index in range(Gamemaster.fleet_size):
            if self.player1_orientations[index] == 0: # if ship is horizontal
                self.player1_locations.append([random.randint(1,10), random.randint(1,10-Gamemaster.boat_sizes[index]+1)])
            elif self.player1_orientations[index] == 1: # if ship is vertical
                self.[player1_locations.append([random.randint(1,10-Gamemaster.boat_sizes[index]+1)])
            else:
                



        self.player1 = Player()





