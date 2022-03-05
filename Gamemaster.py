import random

from Player import Player
from Map import Map

class Gamemaster:

    boat_marker = "M"
    boat_sizes = [5, 4, 3, 3, 2] # boat sizes assuming usual game set
    fleet_size = len(boat_sizes) # this will make sure that we just 
                                 # need to change the boat configuration and the fleet size will automatically be updated
    map_size = 10
    
    nums = "0 1 2 3 4 5 6 7 8 9 10" # used for user input later
    letter_to_numer = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, 
                       "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9}
    #abc = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" # used for user input later
    abc = " ".join(letter_to_numer.keys())
    
    
    def __init__(self):
        # player/enemy boat positioning
        self.player_boat_locations = []
        self.enemy_boat_locations = []
        self.player_orientations = []
        self.enemy_orientations = []
        
        # game loop variables
        self.turn = True # true = player's turn
        self.winner = None # true = player won
        
        # map variables
        self.attack_map = Map([], [], Gamemaster.boat_sizes, Gamemaster.map_size)
        self.defence_map = Map([],[], Gamemaster.boat_sizes, Gamemaster.map_size)

        # randomize orientations for each ship in each fleet
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


    def game_loop(self):
        while self.winner == None:
            if self.turn:
                while True:
                    print("Where would you like to attack?\n\n".title())
                    print(self.attack_map.print_enemy_map() + "\n\n")
                    x, y = self.parse_input(self.get_input())
                    if self.attack_map.get_marker([x],[y]) == "M":
                        self.attack_map.set_marker([x],[y], "X")
                        self.turn = not self.turn
                        print("You hit! congratulations!".title())
                        break
                    elif self.attack_map.get_marker([x],[y]) in ("X", "O"):
                        print("You've already attacked here! Choose a different spot!".title())
                        continue
                    elif self.attack_map.get_marker([x],[y]) == "~":
                        self.attack_map.set_marker([x], [y], "O")
                        self.turn = not self.turn
                        print("You've missed!".title())
                        break
            else:
                print("The enemy is attacking! take positions!".title())
                
                x = random.randint(0,9)
                y = random.randint(0,9)
                while True:
                    if self.defence_map.get_marker([x],[y]) == "M":
                        self.defence_map.set_marker([x],[y], "X")
                        self.turn = not self.turn
                        print("The enemy hit us! send word to HQ".title())
                        print(self.defence_map)
                        break
                    elif self.defence_map.get_marker([x],[y]) in ("X", "O"):
                        x = random.randint(0,9)
                        y = random.randint(0,9)
                        continue
                    elif self.defence_map.get_marker([x],[y]) == "~":
                        self.defence_map.set_marker([x], [y], "O")
                        self.turn = not self.turn
                        print(self.defence_map)
                        print("The enemy missed!".title())
                        break
            self.winner = self.check_winner()
        return self.winner
    
    # this function recieves the user input and check its validity (point is on map)
    def get_input(self):
        while self.turn:
            input_ = input("it's your turn! where would you like to hit? please select row and a coloumn, for example: E5 or g10\n".title())
            input_ = input_.replace(" ","") # remove any spaces
            if (len(input_) in range(1,4) and input_[0] in Gamemaster.abc and input_[1:] in Gamemaster.nums):           
                return input_
            print("Bad input. Please select a location on map using a letter and number; for example: E5\n")
    def parse_input(self, input_):
        y = Gamemaster.letter_to_numer[input_[0]]
        x = int(input_[1:]) - 1
        return (x,y)

    def check_winner(self):
        if sum(row.count("X") for row in self.attack_map.get_marker(list(range(9)),list(range(9)))) == sum(Gamemaster.boat_sizes):
            return True
        elif sum(row.count("X") for row in self.defence_map.get_marker(list(range(9)),list(range(9)))) == sum(Gamemaster.boat_sizes):
            return False
        return None
        

