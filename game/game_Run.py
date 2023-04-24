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
    




