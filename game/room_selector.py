#RoomDatabase.py
import random
#roomdatabase
#from game import main_game
#import NLP_database

#Moved system into Game.py This system will be the input sytem with add NLP soon



Room_list = ['Cabins','Kitchen','Pool','Fitnesscenter','Casino','Smokingarea','shoppingcenter','Captainsroom','The Bridge']
temp_list = Room_list
Room_map = [['','',''],['','',''],['','','']]
#RoomSuffle system

def Room_maper():
    global Room_map
    global temp_list
    for i in range(3):
        for j in range(3):
            Roomapper = temp_list.pop(random.randint(0,len(temp_list)-1))
            Room_map[i][j] = Roomapper
           
Room_maper()
print(Room_map)
#RoomVars
#Current room is the room the user is in currently
#test and old room system 
player_faceing = ''
Room_north = ''
Room_east = ''
Room_south = ''
Room_west = ''
Current_room = ''
Current_room_old = ''
Player_res = ''
hp = 3


def startout_sides():
    global Room_map
    global Current_room
    global Room_north
    global Room_east
    global Room_south
    global Room_west
    Current_room = Room_map[1][1]
    Room_north = Room_map[0][1]
    Room_east = Room_map[1][2]
    Room_south = Room_map[2][1]
    Room_west = Room_map[1][0]

startout_sides()

print("You're in",Current_room)
print("north-",Room_north)
print("east-",Room_east)
print("south-",Room_south)
print("west-",Room_west)

#replace
while hp > 0:


#start of inputs test and the endless loop #chage to classes if possible?
    Player_res = input("Please select a side ")

    def room_selection(side,y,x):
        global Current_room
        Current_room = side
        try:
            side = Room_map[y][x]
        except:
            print("No room there")
        hp-1
        #oldRoom(Player_res)

    def find_room(room_name):
        global Room_map
        for i in range (3):
            for j in range (3):
                if Room_map[i][j] == room_name:
                    return (i,j)
        return None




    
    #!!!!Once NLP is Done Repace this to fit NLP system!!!!
    #this system is going to die one day.
    def Shift_room(User_input):
        global Current_room_old
        global Current_room
        global Room_map
        global Room_north
        global Room_east
        global Room_south
        global Room_west
        #add NLP
        Current_room_old = Current_room
        ##print(Current_room_old)
        y,x = find_room(Current_room)
        if User_input == "east":
            try:
                Current_room = Room_map[y][x+1]
            except:
                print("not valid room ")
            try:
                Room_east = Room_map[y][x+2]
            except:
                print("no room to the east ")    
            try:
                Room_west = Room_map[y][x]
            except:
                print("no room to the west ")
            try:
                Room_south = Room_map[y+1][x]
            except:
                print("no room to the south ")
            try:
                Room_north = Room_map[y-2][x]
            except:
                print("no room to the north ")

        
            oldRoom('east')
        elif User_input == "south":
            pass
        elif User_input == "west":
            pass
        elif User_input == "north":
            pass


    def printTest():
        print('')
        print("You're in",Current_room)
        print("north-",Room_north)
        print("east-",Room_east)
        print("south-",Room_south)
        print("west-",Room_west)

    def oldRoom(user_input):
        global Current_room_old
        global Room_north
        global Room_east
        global Room_south
        global Room_west
        if user_input == 'east':
            Room_west = Current_room_old
            printTest()
        elif user_input == 'west':
            Room_east = Current_room_old
            printTest()
        elif user_input == 'north':
            Room_south = Current_room_old
            printTest()
        elif user_input == 'south':
            Room_north = Current_room_old
            printTest()

    Shift_room(Player_res)

#replace/remove later
    if hp == 0:
        print('you died')
