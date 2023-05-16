#Hello welocme to our AIML game for 2023 This is the main file you will use to do gui eveything else will be working though this i hope inordre to install please do "pip install blessed" 
#into the terminal and please run this file though python launcher for best expncence. enjoy.
#DOCS CAN BE FOUND IN GITHUB
#if you have a version room_Selector that has userinputs it will not work and fail so please make sure your files are up to date 

import blessed
from pydub import AudioSegment
from pydub.playback import play
import time
import keyboard
from room_selector import Current_room
#import engine 
#from engine import rooms
#from save import health
T = blessed.Terminal()
health = 100    
maxHealth = 100  
healthspace = 30
health1 = 50    
maxHealth1 = 50  
healthspace1 = 25
text_state = 0
start_state = True
overall_health = 150
#TEST sATEMENT
#Current_room = 'Cabins'
board = [['-','-','-'],
        ['-','x','-'],
        ['-','-','-']]


def print_slow(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.02)



#Room desctitions needing to add future big room makers and possibly sounds 

def room_selsction():
    global text_state
    if Current_room == 'Cabins' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('CABINS')))
        print_slow(T.move_xy(20,20)('“You poke your head out of the door very slowly, allowing the hallway running from the east to west to become visible. All of the other doors are shut and the silence is only broken by the security guard at the end of the east hallway quite a ways down. His head swinging back and forth in an agitated motion. He looks around the corner and immediately turns and tries to run. He trips and falls on his knees, stumbling to move forward. His hand goes to the pepper spray at his side and he fumbles with the grip. In a moment of particularly bad luck he drops it on the floor just out of his reach as a grotesque, limping… thing steps around the corner. It steps on the spray cracking it into uselessness and reaches for him. You pull the door closed and not a moment later hear the sudden scream of the security guard, then, silence. What would you like to do?”'))
        text_state = 1
        
    elif Current_room == 'Cabins' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('CABINS')))
        print(T.move_xy(20,20)('“You poke your head out of the door very slowly, allowing the hallway running from the east to west to become visible. All of the other doors are shut and the silence is only broken by the security guard at the end of the east hallway quite a ways down. His head swinging back and forth in an agitated motion. He looks around the corner and immediately turns and tries to run. He trips and falls on his knees, stumbling to move forward. His hand goes to the pepper spray at his side and he fumbles with the grip. In a moment of particularly bad luck he drops it on the floor just out of his reach as a grotesque, limping… thing steps around the corner. It steps on the spray cracking it into uselessness and reaches for him. You pull the door closed and not a moment later hear the sudden scream of the security guard, then, silence. What would you like to do?”'))

    elif Current_room == 'Kitchen' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('KITCHEN')))
        print_slow(T.move_xy(20,20)("“You look through the small windows into the kitchen. There are rows of countertops used for making food, and many pots and pans hanging on the wall along with various other cooking materials. You can also see that on the far wall there is a butcher's block with a few knives settled in it, those could possibly make a good weapon if you could get to them. There are 4 of the shuffling creatures wandering around the room, sometimes going through the actions of cooking but otherwise just staring blankly into the distance. All of them have their backs turned to you. They haven't noticed you yet and it seems like you could sneak in without them noticing you… for now. What would you like to do?”"))
        text_state = 1

    elif Current_room == 'Kitchen' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('KITCHEN')))
        print(T.move_xy(20,20)("“You look through the small windows into the kitchen. There are rows of countertops used for making food, and many pots and pans hanging on the wall along with various other cooking materials. You can also see that on the far wall there is a butcher's block with a few knives settled in it, those could possibly make a good weapon if you could get to them. There are 4 of the shuffling creatures wandering around the room, sometimes going through the actions of cooking but otherwise just staring blankly into the distance. All of them have their backs turned to you. They haven't noticed you yet and it seems like you could sneak in without them noticing you… for now. What would you like to do?”"))

    elif Current_room == 'Pool' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('POOL')))
        print_slow(T.move_xy(20,20)("“You walk onto the north pool deck and gaze into the pool. There are 3 floating bodies in the pool, they seem like they aren’t moving and haven't been there long but you can't be sure. You notice a glint of gold in the drain of the pool. It seems to be stuck in the drain pipe and doesn't seem like you will be able to get it without getting into the water. There is also a box of pool toys just to your east, in it, you see a pool noodle, snorkel, kickboard, and some floaties. What would you like to do?”"))
        text_state = 1

    elif Current_room == 'Pool' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('POOL')))
        print(T.move_xy(20,20)("“You walk onto the north pool deck and gaze into the pool. There are 3 floating bodies in the pool, they seem like they aren’t moving and haven't been there long but you can't be sure. You notice a glint of gold in the drain of the pool. It seems to be stuck in the drain pipe and doesn't seem like you will be able to get it without getting into the water. There is also a box of pool toys just to your east, in it, you see a pool noodle, snorkel, kickboard, and some floaties. What would you like to do?”"))

    elif Current_room == 'Fitness center' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('FITNESS CENTER')))
        print_slow(T.move_xy(20,20)("“You see several zombies running on the treadmills and a few ripped zombies hitting the bench press. (if this is where the lock direction/coins spawn) You realize underneath one of the bars that a creature is bench pressing there is a slight glow, possibly from something gold, maybe a lock direction? Next to you there are some weights you think you could throw if necessary. What would you like to do?"))
        text_state = 1

    elif Current_room == 'Fitness cneter' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('FITNESS CENTER')))
        print(T.move_xy(20,20)("“You see several zombies running on the treadmills and a few ripped zombies hitting the bench press. (if this is where the lock direction/coins spawn) You realize underneath one of the bars that a creature is bench pressing there is a slight glow, possibly from something gold, maybe a lock direction? Next to you there are some weights you think you could throw if necessary. What would you like to do?"))

    elif Current_room == 'Casino' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('CASINO')))
        print_slow(T.move_xy(20,20)("You see that to the east of you there are rows and rows of slot machines, some have mindless occupants staring at the pictures and some are even pulling down the bars as if to gamble, it might be best to not disturb them if possible. To the North there are [2-5] zombies that are very invested in their game of blackjack, (if this is where the lock direction spawns) you notice that above them is a chandelier that has a lock direction hanging on it . There are multiple unoccupied slot machines as well as a few coins scattered around the casino from where people must have dropped them during the initial panic. A fire extinguisher is resting on the wall on the opposite wall that could be used in a pinch. What would you like to do?” "))
        text_state = 1

    elif Current_room == 'Casino' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('CASINO')))
        print(T.move_xy(20,20)("You see that to the east of you there are rows and rows of slot machines, some have mindless occupants staring at the pictures and some are even pulling down the bars as if to gamble, it might be best to not disturb them if possible. To the North there are [2-5] zombies that are very invested in their game of blackjack, (if this is where the lock direction spawns) you notice that above them is a chandelier that has a lock direction hanging on it . There are multiple unoccupied slot machines as well as a few coins scattered around the casino from where people must have dropped them during the initial panic. A fire extinguisher is resting on the wall on the opposite wall that could be used in a pinch. What would you like to do?” "))

    elif Current_room == 'Smoking area' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('SMOKING AREA')))
        print_slow(T.move_xy(20,20)("“You open the door to the top deck, wind whipping around you. The smell of salt reaches your nose as well as that of burning BBQ. To the east there is a wall and just beyond the black fog of smoke rises. Pointing in that direction a sign reads “Smoking Area.” In the north  there are vacant picnic tables set up for lunch, topped with still closed picnic baskets placed on blankets. What would you like to do?”"))
        text_state = 1 
    
    elif Current_room == 'Smoking area' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('SMOKING AREA')))
        print(T.move_xy(20,20)("“You open the door to the top deck, wind whipping around you. The smell of salt reaches your nose as well as that of burning BBQ. To the east there is a wall and just beyond the black fog of smoke rises. Pointing in that direction a sign reads “Smoking Area.” In the north  there are vacant picnic tables set up for lunch, topped with still closed picnic baskets placed on blankets. What would you like to do?”"))

    elif Current_room == 'shopping center' and text_state == 0:
        print(T.move_xy(100,10)(T.bold('SHOPPING CENTER')))
        print_slow(T.move_xy(20,20)("“You approach the shop and the doors slide open. Upon looking inside you can tell that it is a small room, there is a counter towards the front and a humanoid robot is standing behind it. “Welcome” it says, raising one of its hands in a greeting gesture, “how can I help you today?”"))
        text_state = 1
    elif Current_room == 'shopping center' and text_state == 1:
        print(T.move_xy(100,10)(T.bold('SHOPPING CENTER')))
        print(T.move_xy(20,20)("“You approach the shop and the doors slide open. Upon looking inside you can tell that it is a small room, there is a counter towards the front and a humanoid robot is standing behind it. “Welcome” it says, raising one of its hands in a greeting gesture, “how can I help you today?”"))
       


def print_board():
    global n
    newboard = ""
    for i in board:
        for j in i:
            newboard += (str(j) + ' ')
        newboard += "\n"
    return newboard
    
    

def find_room():
        global board
        for i in range (3):
            for j in range (3):
                if board[i][j] == 'x':
                    return (i,j)
        return None



def arrow_keys():
    y,x = find_room()
    while True:
        if keyboard.is_pressed("left arrow"):
            try:
                board[y][x-1] = 'x'
                board[y][x] = '-'
                print_board()
                return
            except:
                pass
        elif keyboard.is_pressed("right arrow"):
            try:
                board[y][x+1] = 'x'
                board[y][x] = '-'
                print_board()
                return
            except:
                pass
        elif keyboard.is_pressed("up arrow"):
            try:
                board[y-1][x] = 'x'
                board[y][x] = '-'
                print_board()
                return
            except:
                pass
        elif keyboard.is_pressed("down arrow"):
            try:
                board[y+1][x] = 'x'
                board[y][x] = '-'
                print_board()
                return
            except:
                pass


#room_selsction()


def update():
    global health1
    global health
    if overall_health > 100:
        health1 -= 1
        #print(T.clear)
        health_System()
    elif overall_health <= 100:
        health -= 1
        #print(T.clear)
        health_System()
        



#heath system
def health_System():
    global overall_health
    print(T.clear)
    while T.inkey(timeout=0.02) != 'q':
        dashConvert = int(maxHealth/healthspace)            
        currentDash = int(health/dashConvert)              
        remainingHealth = healthspace - currentDash      
        healthDisplay = T.on_green(' ') * currentDash                 
        remainingDisplay = ' ' * remainingHealth             
        percent = str(int((health/maxHealth)*100)) + "%" 
        bar = healthDisplay + remainingDisplay     
        dashConvert1 = int(maxHealth1/healthspace1)            
        currentDash1 = int(health1/dashConvert1)              
        remainingHealth1 = healthspace1 - currentDash1      
        healthDisplay1 = T.on_blue(' ') * currentDash1                 
        remainingDisplay1 = ' ' * remainingHealth1             
        percent1 = str(int((health1/maxHealth1)*100)) + "%" 
        bar1 = healthDisplay1 + remainingDisplay1
        #print(T.on_green(T.move_xy(10, 10) + healthDisplay + remainingDisplay + T.clear_eol))
        print((T.move_xy(0, 98) + bar1))
        print('')
        print((T.move_xy(0,100))+ bar)
        print(T.move_xy(0,100)("              " + percent))
        print(T.move_right(200)+ print_board())
        room_selsction()
        
        time.sleep(2)
        overall_health -= 1
        update()
        #print_slow(T.clear)
        


def porgram_start():
    health_System()
    update()
    #room_selsction()


def start():
    while start_state ==  True:
        print(T.home + T.clear + T.move_y(T.height // 2))
        print(T.black_on_blue(T.center('press any key to continue.')))
        with T.cbreak(), T.hidden_cursor():
            inp = T.inkey()
        #print(T.move_down(2) + 'You pressed ' + T.bold(repr(inp)))
        #start_state = False
        #start_up = AudioSegment.from_file("aiml-game-main\game\Maps\Sounds\Start_up.wav"
            print_board()
            porgram_start()
        break
start()





