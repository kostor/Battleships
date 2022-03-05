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
                    # select a randomized point
                    self.player_boat_locations.append({"X": random.randint(0,9 - Gamemaster.boat_sizes[index]+1), "Y": random.randint(0,9)})
                    # if the elected point is new, the point will be added also to the map as a marker
                    if Gamemaster.boat_marker not in self.defence_map.get_marker([self.player_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index]+1)], [self.player_boat_locations[index]["Y"]]):
                        self.defence_map.set_marker([self.player_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index])], [self.player_boat_locations[index]["Y"]], Gamemaster.boat_marker)
                        break
                    # if the point isn't new, pop it and randomize a new one.
                    self.player_boat_locations.pop()
                
            else: # if ship is vertical. same logic applies here for all boat location saving purposes.
                while True:
                    self.player_boat_locations.append({"X": random.randint(0,9), "Y":random.randint(0,9-Gamemaster.boat_sizes[index]+1)})
                    
                    if Gamemaster.boat_marker not in self.defence_map.get_marker([self.player_boat_locations[index]["X"]], [self.player_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index]+1)]):
                        self.defence_map.set_marker([self.player_boat_locations[index]["X"]], [self.player_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index])], Gamemaster.boat_marker)
                        break
                    self.player_boat_locations.pop()

            if self.enemy_orientations[index] != 1:  # if ship is horizontal. This includes extreme cases where orientation is not 0 or 1
                while True: # same logic applies here for all boat location saving purposes.
                    self.enemy_boat_locations.append({"X": random.randint(0,9 - Gamemaster.boat_sizes[index]+1), "Y": random.randint(0,9)})
                    
                    if Gamemaster.boat_marker not in self.attack_map.get_marker([self.enemy_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index]+1)], [self.enemy_boat_locations[index]["Y"]]):
                        self.attack_map.set_marker([self.enemy_boat_locations[index]["X"]+i for i in range(Gamemaster.boat_sizes[index])], [self.enemy_boat_locations[index]["Y"]], Gamemaster.boat_marker)
                        break
                    self.enemy_boat_locations.pop()
            else: # if ship is vertical. same logic applies here for all boat location saving purposes.
                while True:
                    self.enemy_boat_locations.append({"X": random.randint(0,9), "Y":random.randint(0,9-Gamemaster.boat_sizes[index]+1)})
                    
                    if Gamemaster.boat_marker not in self.attack_map.get_marker([self.enemy_boat_locations[index]["X"]], [self.enemy_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index]+1)]):
                        self.attack_map.set_marker([self.enemy_boat_locations[index]["X"]], [self.enemy_boat_locations[index]["Y"]+i for i in range(Gamemaster.boat_sizes[index])], Gamemaster.boat_marker)
                        break
                    self.enemy_boat_locations.pop()
        
        # create player and enemy instances. 
        self.player = Player(self.player_boat_locations, self.player_orientations)
        self.enemy = Player(self.enemy_boat_locations, self.enemy_orientations)
        # print boat locations to make sure the correct locations are set.


    def game_loop(self):
        while self.winner == None: # this is the main game loop. will run untill a winner has risen.
            if self.turn: # if it's player's turn (true)
                while True: # this will run as long as the player doesn't chooses a new point to attacl
                    print("Where would you like to attack?\n\n".title())
                    print(self.attack_map.print_enemy_map() + "\n\n") # print attack map
                    x, y = self.parse_input(self.get_input()) # get input, parse it, and put it into x,y variables
                    if self.attack_map.get_marker([x],[y]) == "M": # hit
                        self.attack_map.set_marker([x],[y], "X")
                        self.turn = not self.turn # change turn. comment this out to allow successive hitting turns. 
                        print("You hit! congratulations!".title())
                        break
                    elif self.attack_map.get_marker([x],[y]) in ("X", "O"): # point was already attacked, try a new point
                        print("You've already attacked here! Choose a different spot!".title())
                        continue
                    elif self.attack_map.get_marker([x],[y]) == "~": # miss
                        self.attack_map.set_marker([x], [y], "O")
                        self.turn = not self.turn # change turn
                        print("You've missed!".title())
                        break
            else:
                print("The enemy is attacking! take positions!".title())
                # randomize x,y point to attack
                x = random.randint(0,9)
                y = random.randint(0,9)
                # this loop runs as long as the randomized point is not new. once a new unexplored point surfaces, the loop
                # will break. same as it was with player
                while True: 
                    if self.defence_map.get_marker([x],[y]) == "M": # hit
                        self.defence_map.set_marker([x],[y], "X")
                        self.turn = not self.turn # change turns
                        print("The enemy hit us! send word to HQ".title())
                        print(self.defence_map) # print the defence map, so player knows their status
                        break
                    elif self.defence_map.get_marker([x],[y]) in ("X", "O"): # point was already attacked, try a new point
                        x = random.randint(0,9)
                        y = random.randint(0,9)
                        continue
                    elif self.defence_map.get_marker([x],[y]) == "~": # miss
                        self.defence_map.set_marker([x], [y], "O")
                        self.turn = not self.turn # change turns
                        print(self.defence_map)
                        print("The enemy missed!".title())
                        break
            self.winner = self.check_winner() # check winner before turn changes
        return self.winner
    
    # this function recieves the user input and check its validity (point is on map)
    def get_input(self):
        while self.turn:
            input_ = input("it's your turn! where would you like to hit? please select row and a coloumn, for example: E5 or g10\n".title())
            input_ = input_.replace(" ","") # remove any spaces
            # check if input is valid
            if (len(input_) in range(1,4) and input_[0] in Gamemaster.abc and input_[1:] in Gamemaster.nums):           
                return input_
            print("Bad input. Please select a location on map using a letter and number; for example: E5\n")
    
    # this function parses the input (after it's made sure it's valid) and extracts an (x,y) point to attack
    def parse_input(self, input_):
        y = Gamemaster.letter_to_numer[input_[0]] # the map doesn't allow 2 letter rows
        x = int(input_[1:]) - 1 # get the x location (there are 2 digit locations) and substract 1
        return (x,y) # reutrn tupple of (x,y) locations

    # this function check if the player or enemy won by comparing the amount of Xs on each board to the amount of
    # boats markers in a fleet (17 "M" markers in standard game).
    # if no one won, returns none.
    def check_winner(self):
        if sum(row.count("X") for row in self.attack_map.get_marker(list(range(9)),list(range(9)))) == sum(Gamemaster.boat_sizes):
            return True
        elif sum(row.count("X") for row in self.defence_map.get_marker(list(range(9)),list(range(9)))) == sum(Gamemaster.boat_sizes):
            return False
        return None
        

