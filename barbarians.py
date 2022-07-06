from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
from huts import *
class barbarians(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,1 , 1)
        self.name ="barb"
        self.damage = 10
        self.inpos = 1
        self.freq=0
        self.movement_speed = 1
        self.health =40
        self.huts_present = 0
    def setMatrix(self , x , y): 
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        alpha_b = Back.RED + Fore.BLACK + 'B' + Fore.RESET + Back.RESET
        slash = Back.RED + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[alpha_b]]
        self.x = x
        self.y = y
    def setMatrix2(self , x , y): 
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        alpha_b = Back.YELLOW + Fore.BLACK + 'B' + Fore.RESET + Back.RESET
        slash = Back.RED + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[alpha_b]]
        self.x = x
        self.y = y        

    def setMatrix3(self , x , y): 
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        alpha_b = Back.WHITE + Fore.BLACK + 'B' + Fore.RESET + Back.RESET
        slash = Back.RED + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[alpha_b]]
        self.x = x
        self.y = y

    def check_bounds(self,x,y):
        if (x,y) in all_coord:
            return 1
        if x<0:
            return 1
        elif x>40:
            return 1
        elif y<0:
            return 1
        elif y>148:
            return 1
        else:
            return 0

    def moveandkill(self , all_huts , background , hall , king):
        self.freq = self.freq+1
        h = huts(background)
        min = 1000
        self.inpos=1
        targetx = -5
        targety= -5
        target = 0
        for i in range(6):
            if(all_huts[i].health >0):
                self.huts_present=1
                if (min > np.sqrt(np.square(all_huts[i].x - self.x)+np.square(all_huts[i].y - self.y))):
                    min = np.sqrt(np.square(all_huts[i].x - self.x)+np.square(all_huts[i].y - self.y))
                    targetx = all_huts[i].x
                    targety = all_huts[i].y   
                    h = all_huts[i]
            if(hall.health>0 and min > np.sqrt(np.square(23 - self.x)+np.square(73 - self.y))):
                min = np.sqrt(np.square(23 - self.x)+np.square(73 - self.y))
                target = 1
                targetx = 23
                targety = 73  
            
                  
        if(abs(self.x - targetx )>2):         
            if(self.x > targetx):
                background._grid[self.x][self.y] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
                self.setMatrix(self.x-1 , self.y)
                self.x = self.x -1
                self.inpos = 0
                background.placeElement(self)

                return
            else:
                background._grid[self.x][self.y] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET             
                self.setMatrix(self.x+1 , self.y)
                self.x = self.x + 1
                self.inpos =0
                background.placeElement(self)
 
                return

        if(abs(self.y - targety) > 2):
            if(self.y > targety):
                background._grid[self.x][self.y] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET               
                self.setMatrix(self.x , self.y-1)
                self.y = self.y -1
                self.inpos=0
                background.placeElement(self)
 
                return
            else:
                background._grid[self.x][self.y] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET             
                self.setMatrix(self.x , self.y+1)
                self.y = self.y + 1
                self.inpos=0
                background.placeElement(self)
 
                return                                          
        if (self.inpos==1 and self.freq%10==0):
                for i in range(6):   
                    if (target ==1 and abs(73 - self.y)<2) :
                        self.destroyhall(hall , background)

                        return                                                                                     
                    if(abs(h.y - self.y)<2):
                        self.destroyhuts(h , background) 

                        return                                                              
                    if(abs(h.y+2 - self.y)<2):
                        self.destroyhuts(h , background) 

                        return                                                                                     
                    if(abs(h.x == self.x)<2):
                        self.destroyhuts(h , background) 

                        return                                                                                        
                    if(abs(h.x + 3 == self.x)<2):
                        self.destroyhuts(h , background) 

                        return
                        

    def destroyhuts(self , hut , background):
        hut.health = hut.health - self.damage
        print(hut.health)
        if(hut.health>60 and hut.health<=100):
            hut.setMatrix(hut.x , hut.y)
            background.placeElement(hut)
        if(hut.health>30 and hut.health<=60):
            hut.setMatrix2(hut.x , hut.y)
            background.placeElement(hut)
        if(hut.health>0 and hut.health<=30):
            hut.setMatrix3(hut.x , hut.y)
            background.placeElement(hut)     
        if(hut.health<=0):
            hut.setMatrix4(hut.x , hut.y)
            background.placeElement(hut)
            for p in range(hut.x , hut.x + hut.rows):
                for j in range(hut.y , hut.y+hut.cols):
                    if (p,j) in all_coord:
                        all_coord.remove((p,j)) 
        if(hut.health < 0):
            hut.health= -1 

    def destroyhall(self , hall ,background):
        hall.health = hall.health - self.damage
        if(hall.health>60 and hall.health<=100):
            hall.setMatrix()
            background.placeElement(hall)
        if(hall.health>30 and hall.health<=60):
            hall.setMatrix2()
            background.placeElement(hall)
        if(hall.health>0 and hall.health<=30):
            hall.setMatrix3()
            background.placeElement(hall)     
        if(hall.health<=0):
            hall.setMatrix4()
            background.placeElement(hall)
            for p in range(hall.x , hall.x + hall.rows):
                for j in range(hall.y , hall.y+hall.cols):
                    if (p,j) in all_coord:
                        all_coord.remove((p,j)) 
        if(hall.health < 0):
            hall.health= -1         

        
                
            
              

