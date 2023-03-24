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
Current_room_main = ''
Player_res = ''


print("You're in",Current_room)
print("north-",Room_north)
print("east-",Room_east)
print("south-",Room_south)
print("west-",Room_west)

#start of inputs test and the endless loop #chage to classes if possible?
Player_res = input("Please select a side ")



def room_selection(old_room, New_room):
    old_room = New_room
     

 #Add NLP ai Remove later
def userinput(User_input):
    if User_input == "east":
        room_selection(Current_room, Room_east)

userinput(Player_res)




#tests remove later
print("You're in",Current_room_main)
print("north-",Room_north)
print("east-",Room_east)
print("south-",Room_south)
print("west-",Room_west)
