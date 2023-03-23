#RoomDatabase.py
import random
from game import main_game
#roomdatabase
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

#tests remove later
print("Your in",Current_room)
print("north-",Room_north)
print("east-",Room_east)
print("south-",Room_south)
print("west-",Room_west)
