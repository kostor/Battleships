import Boat

class Fleet:
    def __init__(self, player_id):
        self.player_id = player_id
        self.carrier = Boat("Carrier", 5)
        self.battleship = Boat("Battleship", 4)
        self.destroyer = Boat("Destroyer", 3)
        self.submarine = Boat("Submarine", 3)
        self.patrol_boat = Boat("Patrol Boat", 5)
        self.fleet = {"Carrier": self.carrier, "Battleship": self.battleship, "Destroyer": self.destroyer, "Submarine": self.submarine, "Patrol Boat": self.patrol_boat}

    def destroy_boat(self, type):
        if type in self.fleet.keys():
            return self.fleet.popitem(type)
        else:
            print("Error: Boat not found in player's fleet!")
            return False