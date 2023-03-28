import pyautogui as py
import time
    
        
def quit_mision():
    try:
        x, y = py.locateCenterOnScreen("resources/button_menu.PNG" , confidence=0.9)
    except:
        x, y = -1, -1
        
    if x != -1 and y != -1:
        py.click(x, y)
        time.sleep(1)
        while True:        
            try:
                x, y = py.locateCenterOnScreen("resources/button_retreat1.PNG" , confidence=0.9)
                py.click(x, y)
                time.sleep(1)
                while True:
                    try:
                        x, y = py.locateCenterOnScreen("resources/button_retreat2.PNG" , confidence=0.9)
                        py.click(x, y)
                        time.sleep(1)
                        return True
                    except:
                        continue
            except:
                continue
                


k = 1 #step
loop = 0 #loop
running_start = time.time() #start of script
time_inic = time.time() #counter
reload = "f5" #reload button
reload_count = 0 #reload counter
x, y = -1, -1 #position variables

while True:
    if k == 1:
        #Granblue slimes bookmark
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 2:
        #summon
        try:
            x, y = py.locateCenterOnScreen("resources/summon.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 3:
        #Ok button
        try:
            x, y = py.locateCenterOnScreen("resources/button_ok.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    if k == 4:
        #Search attack button icon
        try:
            x, y = py.locateCenterOnScreen("resources/button_attack.PNG" , confidence=0.9)
        except:
            #Search Potion use button
            try:
                #item_loc = py.locateOnScreen("resources/potion.PNG" , confidence=0.9)
                x, y = py.locateCenterOnScreen("resources/potion.PNG" , confidence=0.9)
                py.click(x, y+150)
                time_inic = time.time()
                continue
            except:
                x, y = -1, -1
            #Search ok button for refill
            try:
                x, y = py.locateCenterOnScreen("resources/button_ok_refill.PNG" , confidence=0.9)
                py.click(x, y)
                time_inic = time.time()
                continue
            except:
                x, y = -1, -1
    if k == 5:
        #Reload
        time.sleep(1)
        py.press(reload)
        k += 1
        continue
    if k == 6:
        # Restart
        #Ok button
        try:
            x, y = py.locateCenterOnScreen("resources/button_ok2.PNG" , confidence=0.9)
        except:
            x, y = -1, -1
    
    #Control print
    elapsed_time = time.time() - running_start
    print("Loop:", loop, "- Stage:", k, "- Execution time:", time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    loop += 1
    
    #validates image found and does the click on position x, y
    if  x != -1 and y != -1:
        #Reload timer and reload count
        time_inic = time.time()
        reload_count = 0
        #Reload loop
        if k == 10:
            k = 1
            continue
        #delay before attack
        if k == 4:
            time.sleep(0)
        #Click
        py.click(x, y)
        #Press f5 to avoid stuck on f6
        k += 1
        
    #validates timer and reload the page based on step do other things
    if time.time() - time_inic > 10:
        #Before entering battle restart from step 1
        if k == 2:
            k = 4
        elif k <= 4:
            k = 1
        
        #If reload more than 3 times without cliking start from step 1
        if reload_count >= 3:
            quit_mision()
            k = 1
        
        #Reloads
        #Search bookmark and clicks
        try:
            x, y = py.locateCenterOnScreen("resources/granblue_bookmark.PNG" , confidence=0.9)
            py.click(x, y)
            time.sleep(1)
        except:
            x, y = -1, -1
        py.press(reload)
        time.sleep(2)
        time_inic = time.time() #reload timer
        reload_count += 1 #Add to reload counter
