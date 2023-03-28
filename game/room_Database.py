#RoomDatabase.py
import random
#roomdatabase
#from game import main_game
#import NLP_database
Room_list = ['Cabins','Kitchen','Pool','Fitnesscenter','Casino','Smokingarea','shoppingcenter','Captainsroom']

#RoomSuffle system
def Roomshuffle():
    random.shuffle(Room_list)
Roomshuffle()

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
        oldRoom(Player_res)
        

    
    #Add NLP ai Remove later
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




    def oldRoom(user_input):
        global Current_room_old
        if user_input == 'east':
            Room_west = Current_room_old
            print("You're in",Current_room)
            print("north-",Room_north)
            print("east-",Room_east)
            print("south-",Room_south)
            print("west-",Room_west)
        elif user_input == 'west':
            Room_east = Current_room_old
            print("You're in",Current_room)
            print("north-",Room_north)
            print("east-",Room_east)
            print("south-",Room_south)
            print("west-",Room_west)
        elif user_input == 'north':
            Room_south = Current_room_old
            print("You're in",Current_room)
            print("north-",Room_north)
            print("east-",Room_east)
            print("south-",Room_south)
            print("west-",Room_west)
        elif user_input == 'south':
            Room_north = Current_room_old
            print("You're in",Current_room)
            print("north-",Room_north)
            print("east-",Room_east)
            print("south-",Room_south)
            print("west-",Room_west)

    userinput(Player_res)

#tests remove later



#replace/remove later
if hp == 0:
    print('you died')
