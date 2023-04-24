import blessed
import time

#from save import health
T = blessed.Terminal()
health = 100    
maxHealth = 100  
healthspace = 30
sheild = 100
maxSheild = 100
sheildSpace = 25
bar = ''





#heath system
def health_System():
    dashConvert = int(maxHealth/healthspace)            
    currentDash = int(health/dashConvert)              
    remainingHealth = healthspace - currentDash      
    healthDisplay = T.on_green(' ') * currentDash                 
    remainingDisplay = ' ' * remainingHealth             
    percent = str(int((health/maxHealth)*100)) + "%" 
    bar = healthDisplay + remainingDisplay     
    #print(T.on_green(T.move_xy(10, 10) + healthDisplay + remainingDisplay + T.clear_eol))
    print((T.move_xy(0, 100) + bar))
    #print(T.move_xy(0,100)("              " + percent))
health_System()



def user_Input():
    




def shild():
    dashConvert2 = int(maxSheild/sheildSpace)            
    currentDash2 = int(sheild/dashConvert2)              
    remainingHealth2 = sheild - currentDash2      
    healthDisplay2 = ' ' * currentDash2                 
    remainingDisplay2 = ' ' * remainingHealth2             
    percent1 = str(int((health/maxHealth)*100)) + "%"     
    print(T.home + T.clear + T.move_y(T.height // 1))
    print(T.on_blue(T.move_down(10)(healthDisplay2 + remainingDisplay2)))
    print(("              " + percent1)) 
#shild()           
