# import boat base class to create objects for a fleet
from Boat import Boat

class Fleet:
    # init fleet object with player id. Then create all the boats objects
    def __init__(self, player_id):
        self.player_id = player_id
        self.carrier = Boat("Carrier", 5)
        self.battleship = Boat("Battleship", 4)
        self.destroyer = Boat("Destroyer", 3)
        self.submarine = Boat("Submarine", 3)
        self.patrol_boat = Boat("Patrol Boat", 5)
        # this is a dict of the active boats the player possess
        self.fleet_dict = {"Carrier": self.carrier, "Battleship": self.battleship, "Destroyer": self.destroyer, "Submarine": self.submarine, "Patrol Boat": self.patrol_boat}

    # method to remove a boat once it's ruined
    def destroy_boat(self, type):
        # check if the boat is in the dict still. if yes, return the removed boat for later use
        if type in self.fleet_dict.keys():
            return self.fleet_dict.popitem(type)
        # if not, return false.
        else:
            print("Error: Boat not found in player's fleet!")
            return False