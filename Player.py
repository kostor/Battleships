import Fleet
class Player:
    id = 0

    def __init__(self, id):        
        self.id = Player.id
        self.fleet = Fleet(self.id)
        Player.id += 1
    




