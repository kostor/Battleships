import random
class Gamemaster:
    def __init__(self):
        self.player1_locations = []
        self.player2_locations = []
        self.player1_orientations = []
        self.player2_orientations = []
        for index in range(5):
            self.player1_orientations.append(random.randint(0,1))
        for index in range(5):
            self.player2_orientations.append(random.randint(0,1))

        self.plaeyer1 = Player()





