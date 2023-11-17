
import random
"""make a new file like student files with rooms an like students take 3 of those"""


def check_if_string(input):
    try:
        int(input)
        return False
    except:
        return True

def try_string():
    x = input("N,W,E,S?   : ")
    while not check_if_string(x):
        print("not N,W,E,S")
        x = input("N,W,E,S?   : ")
    return x

  



"""make a function to check if the input to the Player is the right thing or not"""
class arrow():

    def __init__(self):
        self.player_coordinate = {"x": 0, "y": 0}
        self.alive = True

    def start_coordinate(self, start_coordinate):
        start_coordinate_x = start_coordinate[0]
        start_coordinate_y = start_coordinate[1]
        self.player_coordinate["x"] = start_coordinate_x
        self.player_coordinate["y"] = start_coordinate_y

    def is_alive(self):
        return self.alive
    
    def get(self):
        return self.player_coordinate

    def dead(self):
        self.alive = False
        
    def move(self, direction):

        if direction == "N":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 0
            new_coordinate_y = coordinate_y + 1
            if new_coordinate_y > 4:
                new_coordinate_y = 0
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            print(self.player_coordinate)

        if direction == "S":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 0
            new_coordinate_y = coordinate_y - 1
            if new_coordinate_y < 0:
                new_coordinate_y = 4
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            print(self.player_coordinate)

        if direction == "E":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 1
            new_coordinate_y = coordinate_y + 0
            if new_coordinate_x > 3:
                new_coordinate_x = 0
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            print(self.player_coordinate)

        if direction == "W":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x - 1
            new_coordinate_y = coordinate_y + 0
            if new_coordinate_x < 0:
                new_coordinate_x = 3
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            print(self.player_coordinate)



class danger_room():
    def __init__(self, coordinate):
        self.danger_room_coordiantes = (coordinate)

    def get(self):
        return self.danger_room_coordiantes

class safe_rooms():
    def __init__(self, coordinate):
        self.safe_room_coordiantes = (coordinate)

    def get(self):
        return self.safe_room_coordiantes

class wumpus_room():

    def __init__(self, coordinate):
        self.wumpus_room_coordiantes = (coordinate)
        self.alive = True

    def __str__(self):
        return f"{self.wumpus_room_coordiantes[0]}"

    def add(self, coordinate):
        self.wumpus_room_coordiantes.pop[0]
        self.wumpus_room_coordiantes.append(coordinate)

    def get(self):
        return self.wumpus_room_coordiantes

    def is_boss_alive(self):
        return self.alive
    
    def boss_dead(self):
        self.alive = False

class teleport_rooms():
    def __init__(self, coordinate):
        self.teleport_room_coordiantes = (coordinate)

    def get(self):
        return self.teleport_room_coordiantes
    
    #def get_teleport_to(self, teleport_coordination_list):
        self.teleport_room_coordiantes[0] = teleport_coordination_list[0]
        self.teleport_room_coordiantes[1] = teleport_coordination_list[1]
        self.teleport_room_coordiantes[2] = teleport_coordination_list[2]
        self.teleport_room_coordiantes[3] = teleport_coordination_list[3]



    
      
class player():
    """change the thing to dictionary to understand"""
    def __init__(self):
        self.player_coordinate = {"x": 0, "y": 0}
        self.alive = True

    def start_coordinate(self, start_coordinate):
        start_coordinate_x = start_coordinate[0]
        start_coordinate_y = start_coordinate[1]
        self.player_coordinate["x"] = start_coordinate_x
        self.player_coordinate["y"] = start_coordinate_y

    def is_alive(self):
        return self.alive
    
    def get(self):
        x_coordinate = self.player_coordinate.get("x")
        y_coordinate = self.player_coordinate.get("y")
        
        return x_coordinate, y_coordinate

    def dead(self):
        self.alive = False

    def north_south_west_east(self):
        
        north_coordinate_y = self.player_coordinate.get("y")        
        north_coordinate_y = north_coordinate_y + 1 
        if north_coordinate_y > 4:
            north_coordinate_y = 0
        possible_north = (self.player_coordinate.get("x"), north_coordinate_y)
        
    
        south_coordinate_y = self.player_coordinate.get("y")        
        south_coordinate_y = south_coordinate_y - 1
        if south_coordinate_y < 0:
            south_coordinate_y = 4
        possible_south = (self.player_coordinate.get("x"), south_coordinate_y)
        

        west_coordinate_x = self.player_coordinate.get("x")        
        west_coordinate_x = west_coordinate_x + 1 
        if west_coordinate_x > 3:
            west_coordinate_x = 0
        possible_west = (west_coordinate_x, self.player_coordinate.get("y"))
        

        east_coordinate_x = self.player_coordinate.get("x")        
        east_coordinate_x = east_coordinate_x - 1
        if east_coordinate_x < 0:
            east_coordinate_x = 3
        possible_east = (east_coordinate_x, self.player_coordinate.get("y"))
        

        
        return possible_north, possible_south, possible_west, possible_east
        
    def move(self, direction):

        if direction == "N":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 0
            new_coordinate_y = coordinate_y + 1
            if new_coordinate_y > 4:
                new_coordinate_y = 0
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            #print(self.player_coordinate)

        if direction == "S":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 0
            new_coordinate_y = coordinate_y - 1
            if new_coordinate_y < 0:
                new_coordinate_y = 4
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            #print(self.player_coordinate)

        if direction == "E":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 1
            new_coordinate_y = coordinate_y + 0
            if new_coordinate_x > 3:
                new_coordinate_x = 0
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            #print(self.player_coordinate)

        if direction == "W":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x - 1
            new_coordinate_y = coordinate_y + 0
            if new_coordinate_x < 0:
                new_coordinate_x = 3
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            #print(self.player_coordinate)
            

class rooms():

    def __init__(self):   
        self.rooms_dictionary = {"danger_rooms" : [], "teleport_rooms" : [], "safe_rooms" : [], "wumpus_room" : []}
        
    def get(self):
        return self.rooms_dictionary
            


    def add(self, room_type, room_coordinate):
        self.rooms_dictionary[room_type].append(room_coordinate)

    def get_specific_rooms(self, type_of_room):
        if type_of_room == "danger_rooms":
            x = self.rooms_dictionary.get(type_of_room)
            return x
        elif type_of_room == "teleport_rooms":
            x = self.rooms_dictionary.get(type_of_room)
            return x
        elif type_of_room == "safe_rooms":
            x = self.rooms_dictionary.get(type_of_room)
            return x
        elif type_of_room == "wumpus_room":
            x = self.rooms_dictionary.get(type_of_room)
            return x
  
def has_intersection(lst1, lst2):
    for i in lst2:
        if i in lst1:
            return True
    return False

def has_overlapp(lst1, x):
    for i in lst1:
        if i == x:
            return True
    return False



def main():
    """input some kind of location to player"""
    """adding certain amount of dangerrooms to the list of all rooms in class room because it is similar to the labb 6"""    

    room_one = rooms()
    player_one = player()
    arrow_one = arrow()

    score = 0

    teleport_coordiantes_to = []

    list_of_all_rooms = [(y, x) for x in range(5) for y in range(4)]
    random.shuffle(list_of_all_rooms)

    for i in range(0, 5, 1):
        danger_rooms_coordinates = list_of_all_rooms[i]
        danger_room_one = danger_room(danger_rooms_coordinates)
        room_one.add("danger_rooms", danger_room_one.get())

    wumpus_room_coordiantes = list_of_all_rooms[9]
    wumpus_room_one = wumpus_room(wumpus_room_coordiantes)
    room_one.add("wumpus_room",wumpus_room_one.get())

    for y in range(10, 20, 1):
        safe_roooms_coordinates = list_of_all_rooms[y]
        safe_rooms_one = safe_rooms(safe_roooms_coordinates)
        room_one.add("safe_rooms", safe_rooms_one.get())

    for z in range(10, 14, 1):
        teleport_coordiantes_to.append(z)

    for x in range(5, 9, 1):
        teleport_rooms_coordinates = list_of_all_rooms[x]
        teleport_room_one = teleport_rooms(teleport_rooms_coordinates)
        room_one.add("teleport_rooms", teleport_room_one.get())

    #x = safe_rooms_one.safe_room_coordiantes[0]
    #print(x)
    #print(list_of_all_rooms)

    x_coordinates = safe_rooms_one.safe_room_coordiantes[0]
    y_coordinates = safe_rooms_one.safe_room_coordiantes[1]
    start_coordinates = [x_coordinates, y_coordinates]
    player_one.start_coordinate(start_coordinates)


    while player_one.is_alive():
        while wumpus_room_one.is_boss_alive():

            list_danger = room_one.get_specific_rooms("danger_rooms")
            list_wumpus = wumpus_room_one.get()
            list_teleport = room_one.get_specific_rooms("teleport_rooms")
            list_safe = room_one.get_specific_rooms("safe_rooms")
            list_player = player_one.get()
            list_player_neighbour = player_one.north_south_west_east()    

            print(list_player)
            print("x")
            print(list_safe)
            print("x")

            print(list_teleport)
            print("x")         

            
               
            
            #x = "m"
            #move = "test"


            print(has_overlapp(list_teleport, list_player))
            print(list_player)
            print(list_teleport)

            if has_overlapp(list_teleport, list_player):
                print("You got teleported")
                i = random.randint(0, 9)
                lst = list_safe[i]
                player_one.start_coordinate(lst)
                print(player_one.get())

            x = input("move or shoot,  m/s   : ")
            if x == "m":
                list_player_neighbour = player_one.north_south_west_east()
                #print(list_player_neighbour)
                #print(list_teleport)
                print(has_intersection(list_teleport, list_player_neighbour))
                #print(player_one.get())
                if has_intersection(list_danger, list_player_neighbour):
                    """checks the surrounding for death"""
                    print("You can feel the wind gust")
                if has_intersection(list_wumpus, list_player_neighbour):
                    """checks the surrounding for wumpus"""
                    print("You can smell wumpus")
                if has_intersection(list_teleport, list_player_neighbour):
                    """checks the surrounding for teleport"""
                    print("You can hear bats")
                    print(list_teleport)
                move = try_string()
                player_one.move(move)

                if move == "test":        
                    print(player_one.get())           
                    #print(room_one.rooms_dictionary)
                    print(room_one.get_specific_rooms("danger_rooms"))
                    print("dangerrooms")                
                    #x = room_one.get_specific_rooms("danger_rooms")
                    #print(x)
                    print(player_one.get())
                    print(player_one.north_south_west_east())
                    print("player location")

                    """checks if dangerrooms and wumpus room is n s w e of the players curren location"""
                    

                    if has_intersection(list_danger, list_player_neighbour):
                        """checks the surrounding for death"""
                        print("You can feel the wind gust")
                    elif has_intersection(list_wumpus, list_player_neighbour):
                        """checks the surrounding for wumpus"""
                        print("You can smell wumpus")
                    elif has_intersection(list_teleport, list_player_neighbour):
                        """checks the surrounding for teleport"""
                        print("You can hear bats")
                        print(list_teleport)
                    elif has_intersection(list_teleport, player_one.get()):
                        print("You got teleported")
                        i = random.randint(0, 9)
                        lst = list_safe[i]
                        player_one.start_coordinate(lst)

  


main()
