class Boat:
    
    # init the object with boat_type, size, location and orientation (always set to default untill gamemaster changes that)
    def __init__(self, boat_type, size, location = {"X": 0, "Y": 0}, orientation = 0):
        self.type = boat_type
        self.size = size
        self.location = location
        self.orientation = orientation
    # simple getter - setter fucntions for the class.
    def get_size(self):
        return self.size
    def get_type(self):
        return self.type
    def set_location(self, location):
        self.location = location
    def set_orientation(self, orientation):
        self.orientation = orientation




