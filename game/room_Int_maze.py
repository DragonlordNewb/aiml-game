#RoomDatabase.py
import random
#roomdatabase
#from game import main_game
#import NLP_database

#Moved system into Game.py This system will set the layout of each room allways diffrent will try imports and will build off this.
#help



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

    def room_selection(side):
        global Current_room
        Current_room = side
        hp-1
        oldRoom(Player_res)
    
    #!!!!Once NLP is Done Repace this to fit NLP system!!!!
    def userinput(User_input):
        global Current_room_old
        #add NLP
        Current_room_old = Current_room
        ##print(Current_room_old)
        if User_input == "east":
            room_selection(Room_east)
        elif User_input == "south":
            room_selection(Room_south)
        elif User_input == "west":
            room_selection(Room_west)
        elif User_input == "north":
            room_selection(Room_north)

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

    userinput(Player_res)

#replace/remove later
    if hp == 0:
        print('you died')
