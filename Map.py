class Map:
    # init the class
    def __init__(self, boat_locations, boat_orientations, boat_sizes, map_size):
        
        self.boat_locations = boat_locations
        self.boat_orientations = boat_orientations
        self.boat_sizes = boat_sizes
        self.map_size = map_size
        
        self.boat_map = self.create_empty_map()

        self.number_to_letter={0: "A", 1: "B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J"} # for later use, prints map's headline
        #self.number_to_letter={1: "0",2: "1", 3: "2", 4:"3", 5:"4", 6:"5", 7:"6", 8:"7", 9:"8", 10:"9"} # for later use, prints map's headline
     
    # the way this class should print itself
    def __str__(self):       
        # create a blank string map to fill soon
        self.map = "   1  2  3  4  5  6  7  8  9  10\n"
        #self.map = "   0  1  2  3  4  5  6  7  8  9\n"
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
        count = 0
        for row in self.boat_map:
            self.map+=self.number_to_letter[count] + "  "
            for col in row:
                self.map += col + "  "
            self.map += "\n"
            count+=1
        return self.map

    def create_empty_map(self):
        # create a map of map_size^2. this uses 10 different rows of 10 ~ (tilde) sign. 
        # other definitions might use 1 row of 10 ~ (tilde) signs 10 times (replicates), meaning any change
        # in 1 row would carry to all of them
        return [["~"]*self.map_size for i in range(self.map_size)]


    # this function get list of (x,y) points and changes their marker to specified marker parameter
    def set_marker(self, x_list, y_list, marker):
        for x in x_list: # run thru Xs
            for y in y_list: # run thru Ys
                if marker != self.boat_map[y][x]: # change the marker if needed
                    self.boat_map[y][x] = marker
                else:
                    continue # skip if marker is the same
    
    # This function takes (x,y) list of interests of the boat_map points and returns them as a 1D or 2D area
    def get_marker(self, x_list, y_list):
        if len(y_list) == 1 and len(x_list) > 1: # map is asked to return a row of numbers
            return self.boat_map[y_list[0]][x_list[0]:x_list[-1]]
        elif len(y_list) > 1 and len(x_list) == 1: # map is asked to return a coloumn of numbers
            return [self.boat_map[y_list[0]:y_list[-1]][j][x_list[0]] for j in range(len(self.boat_map[y_list[0]:y_list[-1]] ))]
        elif len(y_list) > 1 and len(x_list) > 1: # map is asked to return a whole segment
            return self.boat_map[y_list[0]:][x_list[0]:]
        else: # map is asked to return a single point
            return self.boat_map[y_list[0]][x_list[0]]
    
    # TODO: function to reset the markers at all spots
    def reset_map(self):
        # set header
        self.map = "   1  2  3  4  5  6  7  8  9  10\n"
        count = 1 # counter to change row num to ABC equiv.
        for row in self.boat_map:
            self.map+=self.number_to_letter[count] + "  " 
            for col in row:
                self.map += "~  " # water marker
            self.map += "\n"
            count+=1
        self.boat_map = self.map
        return self.boat_map

    def print_enemy_map(self):
        map = "   1  2  3  4  5  6  7  8  9  10\n" # map header
        count = 0 # counter to change row num to ABC equiv.
        for row in self.boat_map: # go thru rows of the map
            map+=self.number_to_letter[count] + "  " # add the row header
            for col in row:
                if col == "M": # if the position in the row is a boat, conceal it.
                    map += "~  " # water marker
                else:
                    map += col + "  " # if it's a hit, miss or water, show it.
            map += "\n"
            count+=1
        return map
        