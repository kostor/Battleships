import Fleet
class Player:
    
    # class id for each instantation
    id = 0

    def __init__(self, locations_list, orientations_list):        
        # get the current id (should always amount to 1 max)
        self.id = Player.id
        # add 1 to class's id
        Player.id += 1
        # set a fleet for this player id
        self.fleet = Fleet(self.id)
        
        # set locations and orientations for each boat as dictated by gamemaster obj. First check they're the same lengths
        if len(locations_list) == len(orientations_list):
            # running on same length lists, locations and orientations are sorted by biggest to smallest ship.
            for index in range(len(locations_list)):
                # address the self fleet object. in it, address the fleet dict containing the dict of all active boats. go one by one
                # using the index to find the keys by order, and set loc and orient
                self.fleet.fleet_dict[list(fleet.fleet_dict.keys())[index]].set_location(locations_list[index])
                self.fleet.fleet_dict[list(fleet.fleet_dict.keys())[index]].set_orientation(locations_list[index])
            
    




