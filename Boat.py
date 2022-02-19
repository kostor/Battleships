class Boat:
    def __init__(self, type, size, location = {"X": 0, "Y": 0}, orientation = 0):
        self.type = type
        self.size = size
        self.location = location
        self.orientation = orientation
    def get_size(self):
        return self.size
    def get_type(self):
        return self.type




