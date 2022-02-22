class Map:
    # init the class
    def __init__(self, boat_locations, boat_orientations):
        # save the boat sizes. this needs to become a parameter!
        self.boat_sizes = [5, 4, 3, 3, 2]
        self.map_size = 10
        # create a map of map_size^2. this uses 10 different rows of 10 ~ (tilde) sign. 
        # other definitions might use 1 row of 10 ~ (tilde) signs 10 times (replicates), meaning any change
        # in 1 row would carry to all of them
        self.boat_map = [["~"]*self.map_size for i in range(self.map_size)]
        # save parameters to local vars
        self.boat_locations = boat_locations
        self.boat_orientations = boat_orientations
   
    # the way this class should print itself
    def __str__(self):
        # print boat locations to make sure the correct locations are set.
        print("DEBUG--MAP.py--REMOVE BEFORE LAUNCH")
        print(self.boat_locations)
        print(self.boat_orientations)
        print("DEBUG END--MAP.py--REMOVE BEFORE LAUNCH")
        
        # create a blank string map to fill soon
        self.map = "   1  2  3  4  5  6  7  8  9  10\n"
        self.number_to_letter={1: "A",2: "B", 3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J"}
        # run through boat locations and orientations and place them on the map (M)
        for i, loc_dict in enumerate(self.boat_locations): # using enumerate for easy access to indexation
            # save coordinates into variables
            x = loc_dict["X"] 
            y = loc_dict["Y"]
            # the current boat size is needed for calculations
            boat_size = self.boat_sizes[i]
            # if the boat is horizontal, go thru x point to x+boat size point in row y
            if self.boat_orientations[i] != 1: # horizontal
                for j in range(x-1, x-1 + boat_size):
                    self.boat_map[y-1][j] = "M"
            # else, go thru y point to y+boat size point in column x
            else:
                for j in range(y-1, y-1 + boat_size): # vertical
                    self.boat_map[j][x-1] = "M"

        # Now run thru the map and assign it's marker values (M or ~ [tilde]) into the string
        # this way the symbols of lists such as [] and of strings such as "",'' will not show in the final print
        count = 1
        for row in self.boat_map:
            self.map+=self.number_to_letter[count] + "  "
            for col in row:
                self.map += col + "  "
            self.map += "\n"
            count+=1
        return self.map

    # TODO: function to change the marker at spot X,Y
    # TODO: function to get the marker at spot X,Y
    # TODO: function to reset the markers at all spots

