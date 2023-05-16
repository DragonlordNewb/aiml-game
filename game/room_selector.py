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
#print(Room_map)
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
