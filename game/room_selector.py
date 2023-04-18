#RoomDatabase.py
import random
#roomdatabase
from game import main_game
import x1
#import NLP_database

#Moved system into Game.py This system will be the input sytem with add NLP soon



Room_list = ['Cabins','Kitchen','Pool','Fitness center','Casino','Smoking area','shopping center','Captains room','The Bridge']
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
        #Current_room_old = Current_room
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
                Room_east = " No Room"   
            try:
                Room_west = Room_map[y][x]
            except:
                Room_west = " No Room"
            try:
                Room_south = Room_map[y+1][x+1]
            except:
                Room_south = " No Room"
            try:
                Room_north = Room_map[y-1][x+1]
            except:
                Room_north = " No Room"
            printTest()
        elif User_input == "south":
            try:
                Current_room = Room_map[y+1][x]
            except:
                print("not valid room ")
            try:
                Room_east = Room_map[y+1][x+1]
            except:
                Room_east = " No Room"   
            try:
                Room_west = Room_map[y+1][x-1]
            except:
                Room_west = " No Room"
            try:
                Room_south = Room_map[y+2][x]
            except:
                Room_south = " No Room"
            try:
                Room_north = Room_map[y][x]
            except:
                Room_north = " No Room"
            printTest()
        elif User_input == "west":
            try:
                Current_room = Room_map[y][x-1]
            except:
                print("not valid room ")
            try:
                Room_east = Room_map[y][x]
            except:
                Room_east = " No Room"   
            try:
                Room_west = Room_map[y][x-2]
            except:
                Room_west = " No Room"
            try:
                Room_south = Room_map[y+1][x-1]
            except:
                Room_south = " No Room"
            try:
                Room_north = Room_map[y-1][x-1]
            except:
                Room_north = " No Room"
            printTest()
        elif User_input == "north":
            try:
                Current_room = Room_map[y-1][x]
            except:
                print("not valid room ")
            try:
                Room_east = Room_map[y-1][x+1]
            except:
                Room_east = " No Room"   
            try:
                Room_west = Room_map[y-1][x-1]
            except:
                Room_west = " No Room"
            try:
                Room_south = Room_map[y][x]
            except:
                Room_south = " No Room"
           #None Of this works It goes in a loop need to fix before firday inorder to submit subitive
       
            try:
                Room_north = Room_map[y-2][x]
            except:
                Room_north = " No Room"
            printTest()


    def printTest():
        print('')
        print("You're in",Current_room)
        print("north-",Room_north)
        print("east-",Room_east)
        print("south-",Room_south)
        print("west-",Room_west)


    Shift_room(Player_res)



#luxs thing for his room sys
def searchKeywords(string: str, targets: list[str]) -> str:
    for target in targets:
        if target in string:
            return target
    return None

#replace/remove later
    if hp == 0:
        print('you died')
