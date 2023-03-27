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
Current_room = Room_list[0]
Room_north = Room_list[1]
Room_east = Room_list[2]
Room_south = Room_list[3]
Room_west = Room_list[4]
Current_room_old = ''
Player_res = ''
hp = 3

print("You're in",Current_room)
print("north-",Room_north)
print("east-",Room_east)
print("south-",Room_south)
print("west-",Room_west)


#add while loop



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
    Current_room_old = Room_east
    print(Current_room_old)
    if User_input == "east":
        room_selection(Room_east)


def oldRoom(user_input):
    global Current_room_old
    if user_input == 'east':
        Current_room_old = Room_south
        print(Room_south)





userinput(Player_res)

#tests remove later
print("You're in",Current_room)
print("north-",Room_north)
print("east-",Room_east)
print("south-",Room_south)
print("west-",Room_west)

