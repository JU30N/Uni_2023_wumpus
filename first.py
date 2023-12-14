"""git status -> git add -A -> git commit -m "message" -> git push"""
import random
"""make a new file like student files with rooms an like students take 3 of those"""



def welcome():
    print("You are in the culverts under the D building, where the ravenous Wumpus" + 
        "lives. To avoid getting caught, you have to shoot the Wumpus with yours" + 
        "bow and arrow. The culverts have 20 rooms connected by narrow passages." +
        "You can move north, east, south or west from one room to" +
        "another." +
        "However, there are dangers lurking here. In some rooms there are bottomless holes. Stepping" + 
        "you down in such a you die immediately. In other rooms there are bats" +
        "which lifts you up, flies a bit and drops you in an arbitrary" + 
        "room. In one of the rooms there are Wumpus, and if you venture into that room" +
        "you will immediately be busy. Luckily, you can feel it from the rooms next door" +
        "the draft from an abyss or the smell of Wumpus. You can too" +
        "in each room find out which rooms are next to each other." +
        "To win the game you must shoot the Wumpus. When you shoot one" +
        "arrow it moves through three rooms - you can control which direction" +
        "the arrow must select in each room. Don't forget that the tunnels wind" +
        "in unexpected ways. You can shoot yourself..." +
        "You have five arrows. Good luck!")

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

def select_mode():
    x = input("Hard or Normal or Easy, H/N/E : ")
    while not check_if_string(x):
        print("not an H or N or E")
        x = input("Hard or Normal, H/N/E : ")
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

def has_overlapp_intersection(tuple1, x):
    for i in tuple1:
        if x == i:
            return True
    return False
  
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

class teleport_rooms():
    def __init__(self, coordinate):
        self.teleport_room_coordiantes = (coordinate)

    def get(self):
        return self.teleport_room_coordiantes

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

    def boss_move(self, player_coordinate):
        player_x_coord = player_coordinate[0]
        player_y_coord = player_coordinate[1]
        boss_x_coord = self.wumpus_room_coordiantes[0]
        boss_y_coord = self.wumpus_room_coordiantes[1]

        if player_x_coord > boss_x_coord and player_y_coord > boss_y_coord:
            boss_y_coord = boss_y_coord + 1
            if boss_y_coord > 4:
                boss_y_coord = 0 
            self.wumpus_room_coordiantes[1] = boss_y_coord
        
        if player_x_coord > boss_x_coord and player_y_coord < boss_y_coord:
            boss_y_coord = boss_y_coord - 1
            if boss_y_coord < 0:
                boss_y_coord = 4
            self.wumpus_room_coordiantes[1] = boss_y_coord

        if player_x_coord < boss_x_coord and player_y_coord == boss_y_coord:
            boss_x_coord = boss_x_coord + 1
            if boss_x_coord > 3:
                boss_x_coord = 0
            self.wumpus_room_coordiantes[0] = boss_x_coord

        if player_x_coord > boss_x_coord and player_y_coord == boss_y_coord:
            boss_x_coord = boss_x_coord - 1
            if boss_x_coord < 0:
                boss_x_coord = 3
            self.wumpus_room_coordiantes[0] = boss_x_coord

        if player_x_coord < boss_x_coord and player_y_coord < boss_y_coord:
            boss_x_coord = boss_x_coord - 1
            if boss_x_coord > 3:
                boss_x_coord = 0
            self.wumpus_room_coordiantes[0] = boss_x_coord

        if player_x_coord > boss_x_coord and player_y_coord > boss_y_coord:
            boss_x_coord = boss_x_coord + 1
            if boss_x_coord > 3:
                boss_x_coord = 0
            self.wumpus_room_coordiantes[0] = boss_x_coord

        if player_x_coord == boss_x_coord and player_y_coord < boss_y_coord:
            boss_y_coord = boss_y_coord - 1
            if boss_y_coord < 0:
                boss_y_coord = 4
            self.wumpus_room_coordiantes[1] = boss_y_coord

        if player_x_coord == boss_x_coord and player_y_coord > boss_y_coord:
            boss_y_coord = boss_y_coord + 1
            if boss_y_coord > 4:
                boss_y_coord = 0
            self.wumpus_room_coordiantes[1] = boss_y_coord

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
        
class coordinate_to_room_name():
    def __init__(self): 
        self.dictionary_lst1 = {(0, 0) : "1", (0, 1) : "2", (0, 2) : "3", (0, 3) : "4", (0, 4) : "5",
                                (1, 0) : "6", (1, 1) : "7", (1, 2) : "8", (1, 3) : "9", (1, 4) : "10",
                                (2, 0) : "11", (2, 1): "12", (2, 2):"13", (2, 3): "14", (2, 4): "15",
                                (3, 0) : "16", (3, 1): "17", (3, 2):"18", (3, 3): "19", (3, 4):"20"}
    
    def __str__(self):
        return f""

    def what_location_player(self, lst1, type_room):
        x = self.dictionary_lst1.get(lst1)
        if type_room == "player":
            return x    
        else:
            return x
        
    def neighbour_room_number(self, list_tuple1):
        room_numbers = []
        for i in list_tuple1:
            x = self.dictionary_lst1.get(i)
            room_numbers.append(x)
        return ", ".join(room_numbers)       
    

class score():
    def __init__(self):
        self.score_value = 0

    def get(self):
        return f"{self.score_value}"
    
    def add(self):
        self.score_value = self.score_value + 1

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

        if direction == "S":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 0
            new_coordinate_y = coordinate_y - 1
            if new_coordinate_y < 0:
                new_coordinate_y = 4
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y

        if direction == "E":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x + 1
            new_coordinate_y = coordinate_y + 0
            if new_coordinate_x > 3:
                new_coordinate_x = 0
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y

        if direction == "W":
            coordinate_x = self.player_coordinate.get("x")
            coordinate_y = self.player_coordinate.get("y")
            new_coordinate_x = coordinate_x - 1
            new_coordinate_y = coordinate_y + 0
            if new_coordinate_x < 0:
                new_coordinate_x = 3
            self.player_coordinate["x"] = new_coordinate_x
            self.player_coordinate["y"] = new_coordinate_y
            
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
    
    def back_alive(self):
        self.alive = True
    
    def get(self):
        x_coordinate = self.player_coordinate.get("x")
        y_coordinate = self.player_coordinate.get("y")
        
        return x_coordinate, y_coordinate
    
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

def true_or_not(input):
    if input == "1":
        return True
    else:
        return False

def check_n_h(x):
    if x == "N":
        return True
    elif x =="H":
        return True
    elif x =="E":
        return True
    else:
        print("N or H or E")
        return True
    

def main():
    
    welcome()


    """making all the objects"""
    room_one = rooms()
    player_one = player()
    arrow_one = arrow()
    score_one = score()

    teleport_coordiantes_to = []

    """suffles all the rooms to random coordinates"""
    list_of_all_rooms = [(y, x) for x in range(5) for y in range(4)]
    random.shuffle(list_of_all_rooms)

    """selecting difficulty"""
    x = select_mode()
    while check_n_h(x):
        if x == "H":
            mode_level = 9
            mode_level_teleport = 20
            mode_level_safe = 11
            mode_level_a_one  = 16
            mode_level_teleport_a = 15
            mode_level_safe_a = 20
            true_for_boss_movment = 1
            break
        elif x == "N":
            mode_level = 5
            mode_level_a_one = 13
            mode_level_teleport = 18
            mode_level_teleport_a = 12
            mode_level_safe = 7
            mode_level_safe_a = 20
            true_for_boss_movment = 0
            break
        elif x == "E":
            mode_level = 5
            mode_level_a_one = 11
            mode_level_teleport = 16
            mode_level_teleport_a = 10
            mode_level_safe = 7
            mode_level_safe_a = 20
            true_for_boss_movment = 0
            break
        else:
            x = select_mode()


    """creating rooms"""
    """Hard        0      9      """
    """Normal      0      5 """
    """ez          0      5 """
    for i in range(0, mode_level, 1):
        danger_rooms_coordinates = list_of_all_rooms[i]
        danger_room_one = danger_room(danger_rooms_coordinates)
        room_one.add("danger_rooms", danger_room_one.get())


    """hard                    10 """
    """normal                   6"""
    """ez                       6"""
    wumpus_room_location = mode_level + 1
    wumpus_room_coordiantes = list_of_all_rooms[wumpus_room_location]
    wumpus_room_one = wumpus_room(wumpus_room_coordiantes)
    room_one.add("wumpus_room",wumpus_room_one.get())


    """Hard:             11              20           """
    """Normal            7              20"""
    """ez                7               20"""
    for y in range(mode_level_safe, mode_level_safe_a, 1):
        safe_roooms_coordinates = list_of_all_rooms[y]
        safe_rooms_one = safe_rooms(safe_roooms_coordinates)
        room_one.add("safe_rooms", safe_rooms_one.get())

    """hard              11                     15"""
    """normal             7                      12"""
    """ez                  7                      10"""
    for z in range(mode_level_safe, mode_level_teleport_a, 1):
        teleport_coordiantes_to.append(z)

    """hard                   16             20     """
    """normal                 13             18 """
    """ez                    11              16"""
    for x in range(mode_level_a_one, mode_level_teleport, 1):
        teleport_rooms_coordinates = list_of_all_rooms[x]
        teleport_room_one = teleport_rooms(teleport_rooms_coordinates)
        room_one.add("teleport_rooms", teleport_room_one.get())

    x_coordinates = safe_rooms_one.safe_room_coordiantes[0]
    y_coordinates = safe_rooms_one.safe_room_coordiantes[1]
    start_coordinates = [x_coordinates, y_coordinates]
    player_one.start_coordinate(start_coordinates)

    """main gaming """
    while wumpus_room_one.is_boss_alive():
            list_teleport = room_one.get_specific_rooms("teleport_rooms")
            player_coord = player_one.get()
            list_danger = room_one.get_specific_rooms("danger_rooms")
            list_wumpus = wumpus_room_one.get()
            list_safe = room_one.get_specific_rooms("safe_rooms")
            list_player_neighbour = player_one.north_south_west_east() 
            coordinate_to_room_name_one = coordinate_to_room_name()   

            if has_overlapp(list_teleport, player_coord):
                print("You got teleported")
                amount = mode_level_safe_a - mode_level_safe
                i = random.randint(0, amount)
                lst = list_safe[i]
                player_one.start_coordinate(lst)
                player_coord = player_one.get()

            if has_overlapp(list_danger, player_coord):
                """checks if player is on the danger"""
                print("You fell down a cliff")
                print("game over")
                wumpus_room_one.boss_dead()
                player_one.dead()

            

            while player_one.is_alive():
                print("You are in room " + coordinate_to_room_name_one.what_location_player(player_coord, "player"))
                print("Room beside you are rooms " + coordinate_to_room_name_one.neighbour_room_number(list_player_neighbour))

                if true_or_not(true_for_boss_movment):
                    wumpus_room_one.boss_move(player_coord)

                if has_intersection(list_danger, list_player_neighbour):
                    """checks the surrounding for death"""
                    print("You can feel the wind gust")

                if has_overlapp_intersection(list_player_neighbour, list_wumpus):
                    """checks the surrounding for wumpus"""
                    print("You can smell wumpus")


                if has_intersection(list_teleport, list_player_neighbour):
                    """checks the surrounding for teleport"""
                    print("You can hear bats") 

            
                """shoot or move"""
                x = input("move or shoot,  m/s   : ")
                score_one.add()
                if x == "m":
                    move = try_string()
                    player_one.move(move)
                    break
                elif x == "s":
                    amount_of_arrows = 0
                    arrow_one.start_coordinate(player_coord)
                    arrow_one.back_alive() 
                    while arrow_one.is_alive():
                        shot = try_string()                    
                        arrow_one.move(shot)

                        if arrow_one.get() == wumpus_room_one.get():
                            wumpus_room_one.boss_dead()
                            print("game won")
                            score_str = score_one.get()
                            with open("high_score", 'a') as file:
                                file.write(score_str)
                                file.write("\n")
                            player_one.dead()
                            arrow_one.dead()
                            break

                        amount_of_arrows = amount_of_arrows + 1

                        if amount_of_arrows == 5:
                            arrow_one.dead()
                else:
                    print("error")

main()