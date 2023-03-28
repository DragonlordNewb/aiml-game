#RoomDatabase.py
import random
#roomdatabase
#from game import main_game
#import NLP_database
Room_list = ['Cabins','Kitchen','Pool','Fitnesscenter','Casino','Smokingarea','shoppingcenter','Captainsroom','The Bridge']
Room_map = []
#RoomSuffle system

Room_num = random.randint(0,9)



def Room_mapCr(num):
    Roomapper = Room_list.pop(num)
    print(Roomapper)
Room_mapCr(Room_num)    


#RoomVars
#Current room is the room the user is in currently
Current_room = Room_list[0]
#rooms east through west store the rooms in that position compares to the user's position 
Room_north = Room_list[1]
Room_east = Room_list[2]
Room_south = Room_list[3]
Room_west = Room_list[4]
#test and old room system 
Current_room_old = ''
Player_res = ''
hp = 3

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
