import blessed
import time
import keyboard
#from room_selector import Current_room

#from save import health
T = blessed.Terminal()
health = 100    
maxHealth = 100  
healthspace = 30
sheild = 100
maxSheild = 100
sheildSpace = 25
start_state = True
text_state = 0
Current_room = 'cabin'


def print_slow(text):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(0.03)

def room_selsction():
    global text_state
    if Current_room == 'cabin' and text_state == 0:
        print(T.move_xy(5,15)('“You poke your head out of the door very slowly, allowing the hallway running from the east to west to become visible. All of the other doors are shut and the silence is only broken by the security guard at the end of the east hallway quite a ways down. His head swinging back and forth in an agitated motion. He looks around the corner and immediately turns and tries to run. He trips and falls on his knees, stumbling to move forward. His hand goes to the pepper spray at his side and he fumbles with the grip. In a moment of particularly bad luck he drops it on the floor just out of his reach as a grotesque, limping… thing steps around the corner. It steps on the spray cracking it into uselessness and reaches for him. You pull the door closed and not a moment later hear the sudden scream of the security guard, then, silence. What would you like to do?”'))
        text_state += 1
    

#room_selsction()


def update():
    if health >= 100:
        health_System()



#heath system
def health_System():
    global health
    print(T.clear)
    while T.inkey(timeout=0.02) != 'q':
        T.enter_fullscreen
        dashConvert = int(maxHealth/healthspace)            
        currentDash = int(health/dashConvert)              
        remainingHealth = healthspace - currentDash      
        healthDisplay = T.on_green(' ') * currentDash                 
        remainingDisplay = ' ' * remainingHealth             
        percent = str(int((health/maxHealth)*100)) + "%" 
        bar = healthDisplay + remainingDisplay     
        #print(T.on_green(T.move_xy(10, 10) + healthDisplay + remainingDisplay + T.clear_eol))
        Test1 = print((T.move_xy(0, 100) + bar))
        Test = print(T.move_xy(0,100)("              " + percent))
        room_selsction()
        time.sleep(2)
        print('/b' + T.clear)
        health -= 1
        
        
        
def porgram_start():
    health_System()
    update()
    room_selsction()


def start():
    while start_state ==  True:
        print(T.home + T.clear + T.move_y(T.height // 2))
        print(T.black_on_blue(T.center('press any key to start.')))
        with T.cbreak(), T.hidden_cursor():
            inp = T.inkey()
        #print(T.move_down(2) + 'You pressed ' + T.bold(repr(inp)))
        #start_state = False
        porgram_start()
        break




start()
