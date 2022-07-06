from colorama import Fore, Back, Style
import numpy as np 
from global_var import *
from global_var import *
class background:
    def __init__(self , rows , cols ):
        self.num_rows = rows
        self.num_cols = cols
        self._grid = ([[Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET for col in range(self.num_cols)]
                       for row in range(self.num_rows)])
        self._copygrid = ([[Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET for col in range(self.num_cols)]
                       for row in range(self.num_rows)])  
        self.coordinates = [[[]]]                            
        self.num_times=0    
        self.archers=6
        self.barbarians=6
        self.ballons=3
        self.archer_used = 0
        self.barbarians_used = 0
        self.ballons_used = 0
        self.attack_townhall = 0

    def convertToString(self):
        outputstr=""    
        file1 = open("replay"+str(self.num_times)+".txt", "a")  # append mode
        for r in range (self.num_rows):
            for c in range(self.num_cols):
                outputstr += self._grid[r][c]
            outputstr += "\n" 
        file1.write(outputstr) 
        file1.write("s")      
        file1.close()     
        print(outputstr)       

    def copygrid1(self):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                self._copygrid[row][cols] = self._grid[row][cols]

    def copygrid2(self):
        for row in range(self.num_rows):
            for cols in range(self.num_cols):
                self._grid[row][cols] = self._copygrid[row][cols]

    def check_bounds(self,x,y):
        if (x,y) in all_coord:
            return 1
        if x<0:
            return 1
        elif x>48:
            return 1
        elif y<0:
            return 1
        elif y>148:
            return 1
        else:
            return 0  

    def placeElement(self , element):
        row=0
        col=0
        for i in range(element.x , element.x + element.rows):
            col=0
            for j in range(element.y , element.y+element.cols):
                if element.name == "hut":
                    all_coord.add((i,j))
                if element.name == "canon":
                    all_coord.add((i,j))  
                if element.name == "wizard_tower":
                    all_coord.add((i,j))                      
                if element.name == "wall":
                    all_coord.add((i,j))       
                if element.name == "hall":
                    all_coord.add((i,j))                                                   
                if element.name=="king":
                    king_coord.add((i,j))
                if element.name=="queen":
                    king_coord.add((i,j))                                           
                self._grid[i][j]=element.matrix[row][col]    
                col=col+1 
            row = row+1    

    def moveleft_king(self , element):       
        backup_set=set()
        self.copygrid1()
        for set_elem in king_coord:
            if(self.check_bounds(set_elem[0] , set_elem[1]-1)):
                return 1      
        element.y =  element.y - 1           
        for set_elems in king_coord:
            self._copygrid[set_elems[0]][set_elems[1]] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            lastx = set_elems[0]
            lasty = set_elems[1]
            backup_set.add((set_elems[0] , set_elems[1]))
        king_coord.clear()    
        for set_elems in backup_set:
            king_coord.add((set_elems[0] , set_elems[1]-1))
        self.copygrid2()  
        element.setMatrix(element.x , element.y)
        self.placeElement(element)

    def moveup_king(self , element):       
        backup_set=set()
        self.copygrid1()
        for set_elem in king_coord:
            if(self.check_bounds(set_elem[0]-1 , set_elem[1])):
                return 1   
        element.x =  element.x - 1                      
        for set_elems in king_coord:
            self._copygrid[set_elems[0]][set_elems[1]] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            lastx = set_elems[0]
            lasty = set_elems[1]
            backup_set.add((set_elems[0] , set_elems[1]))
        king_coord.clear()    
        for set_elems in backup_set:
            king_coord.add((set_elems[0]-1 , set_elems[1]))
        self.copygrid2()  
        element.setMatrix(element.x , element.y)
        self.placeElement(element)

    def moveright_king(self , element):        
        backup_set=set()
        self.copygrid1()
        for set_elem in king_coord:
            if(self.check_bounds(set_elem[0] , set_elem[1]+1)):
                return 1 
        element.y =  element.y + 1                       
        for set_elems in king_coord:
            self._copygrid[set_elems[0]][set_elems[1]] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            lastx = set_elems[0]
            lasty = set_elems[1]
            backup_set.add((set_elems[0] , set_elems[1]))
        king_coord.clear()    
        for set_elems in backup_set:
            king_coord.add((set_elems[0] , set_elems[1]+1))
        self.copygrid2()  
        element.setMatrix(element.x , element.y)
        self.placeElement(element)

    def movedown_king(self , element):  
        backup_set=set()
        self.copygrid1()
        for set_elem in king_coord:
            if(self.check_bounds(set_elem[0]+1 , set_elem[1])):
                return 1 
        element.x =  element.x + 1                             
        for set_elems in king_coord:
            self._copygrid[set_elems[0]][set_elems[1]] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            lastx = set_elems[0]
            lasty = set_elems[1]
            backup_set.add((set_elems[0] , set_elems[1]))
        king_coord.clear()    
        for set_elems in backup_set:
            king_coord.add((set_elems[0]+1 , set_elems[1]))
        self.copygrid2()  
        element.setMatrix(element.x , element.y)
        self.placeElement(element)

    def attack_king(self , king , all_canons , all_wizards , all_huts , townhall , all_bricks):
        x1 = king.x
        x2 = king.x + 3
        y1 = king.y
        y2 = king.y + 4 
        if(y2==73):
            if(x1 >= 23):
                if(x2 <= 27):
                    print("townhall")
                    townhall.health = townhall.health - king.damage
                    if(townhall.health>60 and townhall.health<=100):
                        townhall.setMatrix()
                        self.placeElement(townhall) 
                    if(townhall.health>30 and townhall.health<=60):
                        townhall.setMatrix2()
                        self.placeElement(townhall)    
                    if(townhall.health>0 and townhall.health<=30):
                        townhall.setMatrix3()
                        self.placeElement(townhall) 
                    if(townhall.health<=0):
                        townhall.setMatrix4()
                        townhall.health = -1
                        self.placeElement(townhall)
                        for p in range(townhall.x , townhall.x + townhall.rows):
                            for j in range(townhall.y , townhall.y+townhall.cols):
                                all_coord.remove((p,j))
                          
        if(y1==77):
            if(x1 >= 23):
                if(x2 <= 27):
                    townhall.health = townhall.health - king.damage
                    if(townhall.health>60 and townhall.health<=100):
                        townhall.setMatrix()
                        self.placeElement(townhall) 
                    if(townhall.health>30 and townhall.health<=60):
                        townhall.setMatrix2()
                        self.placeElement(townhall)    
                    if(townhall.health>0 and townhall.health<=30):
                        townhall.setMatrix3()
                        self.placeElement(townhall) 
                    if(townhall.health<=0):
                        townhall.setMatrix4()
                        townhall.health = -1
                        self.placeElement(townhall) 
                        for p in range(townhall.x , townhall.x + townhall.rows):
                            for j in range(townhall.y , townhall.y+townhall.cols):
                                all_coord.remove((p,j))
                        

        if(x2==23):
            if(y1 >= 73):
                if(y2 <= 77):
                    townhall.health = townhall.health - king.damage
                    if(townhall.health>60 and townhall.health<=100):
                        townhall.setMatrix()
                        self.placeElement(townhall) 
                    if(townhall.health>30 and townhall.health<=60):
                        townhall.setMatrix2()
                        self.placeElement(townhall)    
                    if(townhall.health>0 and townhall.health<=30):
                        townhall.setMatrix3()
                        self.placeElement(townhall) 
                    if(townhall.health<=0):
                        townhall.setMatrix4()
                        townhall.health = -1
                        self.placeElement(townhall)
                        for p in range(townhall.x , townhall.x + townhall.rows):
                            for j in range(townhall.y , townhall.y+townhall.cols):
                                all_coord.remove((p,j))
        if(x1==26):
            if(y1 >= 73):
                if(y2 <= 77):
                    townhall.health = townhall.health - king.damage
                    if(townhall.health>60 and townhall.health<=100):
                        townhall.setMatrix()
                        self.placeElement(townhall) 
                    if(townhall.health>30 and townhall.health<=60):
                        townhall.setMatrix2()
                        self.placeElement(townhall)    
                    if(townhall.health>0 and townhall.health<=30):
                        townhall.setMatrix3()
                        self.placeElement(townhall) 
                    if(townhall.health<=0):
                        townhall.setMatrix4()
                        townhall.health = -1
                        self.placeElement(townhall)   
                        for p in range(townhall.x , townhall.x + townhall.rows):
                            for j in range(townhall.y , townhall.y+townhall.cols):
                                all_coord.remove((p,j))                                                

        if(y2==70):
            self._grid[x1][y2] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1,y2) in all_coord:
                all_coord.remove((x1,y2))   
            self._grid[x1+1][y2] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1+1,y2) in all_coord:
                all_coord.remove((x1+1,y2)) 
            self._grid[x1+2][y2] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1+2,y2) in all_coord:
                all_coord.remove((x1+2,y2))  
        if(y1==79):
            self._grid[x1][y1-1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1,y1-1) in all_coord:
                all_coord.remove((x1,y1-1))   
            self._grid[x1+1][y1-1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1+1,y1-1) in all_coord:
                all_coord.remove((x1+1,y1-1)) 
            self._grid[x1+2][y1-1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1+2,y1-1) in all_coord:
                all_coord.remove((x1+2,y1-1))  
        if(x1==29):
            self._grid[x1-1][y1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1-1,y1) in all_coord:
                all_coord.remove((x1-1,y1))   
            self._grid[x1-1][y1+1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1-1,y1+1) in all_coord:
                all_coord.remove((x1-1,y1+1)) 
            self._grid[x1-1][y1+2] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1-1,y1+2) in all_coord:
                all_coord.remove((x1-1,y1+2))   
            self._grid[x1-1][y1+3] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x1-1,y1+3) in all_coord:
                all_coord.remove((x1-1,y1+3))    
        if(x2==20):
            self._grid[x1-1][y1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x2,y1) in all_coord:
                all_coord.remove((x2,y1))   
            self._grid[x2][y1+1] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x2,y1+1) in all_coord:
                all_coord.remove((x2,y1+1)) 
            self._grid[x2][y1+2] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x2,y1+2) in all_coord:
                all_coord.remove((x2,y1+2))   
            self._grid[x2][y1+3] = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
            if (x2,y1+3) in all_coord:
                all_coord.remove((x2,y1+3))                                                                                                                       
        for i in range(6):                                                                                         
            if(all_huts[i].y == y2):
                all_huts[i].health = all_huts[i].health - king.damage
                if(x1 == all_huts[i].x):
                    if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                        all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])
                if(x1 == all_huts[i].x):
                    if(all_huts[i].health > 30 and all_huts[i].health <= 60):
                        all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])    
                if(x1 == all_huts[i].x):
                    if(all_huts[i].health >= 0 and all_huts[i].health <= 30):
                        all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])
                if(all_huts[i].health == 0):
                    all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                    all_huts[i].health = -1
                    self.placeElement(all_huts[i])   
                    for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                        for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                            all_coord.remove((p,j))                                                           
            if(all_huts[i].y+2 == y1):
                all_huts[i].health = all_huts[i].health - king.damage
                if(x1 == all_huts[i].x):
                    if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                        all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])  
                if(x1 == all_huts[i].x):
                    if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                        all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])  
                if(x1 == all_huts[i].x):
                    if(all_huts[i].health >= 0 and all_huts[i].health <= 30 ):
                        all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i]) 
                if(all_huts[i].health == 0):
                    all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                    all_huts[i].health = -1
                    self.placeElement(all_huts[i])  
                    for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                        for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                            all_coord.remove((p,j))                                                                                    
            if(all_huts[i].x == x2):
                all_huts[i].health = all_huts[i].health - king.damage
                if(y1 == all_huts[i].y-1):  
                    if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                        all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])  
                if(y1 == all_huts[i].y-1):  
                    if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                        all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i]) 
                if(y1 == all_huts[i].y-1):  
                    if(all_huts[i].health >=0 and all_huts[i].health <= 30 ):
                        all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i]) 
                if(all_huts[i].health == 0):
                    all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                    all_huts[i].health = -1
                    self.placeElement(all_huts[i])  
                    for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                        for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                            all_coord.remove((p,j))    
                                                                                                          
            if(all_huts[i].x + 3 == x1):
                all_huts[i].health = all_huts[i].health - king.damage                
                if(y1 == all_huts[i].y-1):
                    if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                        all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])                    
                if(y1 == all_huts[i].y-1):
                    if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                        all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i]) 
                if(y1 == all_huts[i].y-1):
                    if(all_huts[i].health > 0 and all_huts[i].health <= 30 ):
                        all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                        self.placeElement(all_huts[i])                         
                if(all_huts[i].health == 0):
                    all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                    all_huts[i].health = -1
                    self.placeElement(all_huts[i])
                    for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                        for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                            all_coord.remove((p,j))
        for wizard in all_wizards:
            if abs(y2-wizard.y)<=1 and (wizard.x >= x1 and wizard.x <=x2):
                self.destroywizard(wizard , king)
            if abs(y1-wizard.y)<=1 and (wizard.x >= x1 and wizard.x <=x2):  
                self.destroywizard(wizard , king)
            if abs(x1 - wizard.x) <=1 and (wizard.y >=y1 and wizard.y<=y2):
                self.destroywizard(wizard , king)
            if abs(x2 - wizard.x) <=1 and (wizard.y >=y1 and wizard.y<=y2):
                self.destroywizard(wizard , king)

        for canon in all_canons:
            if abs(y2-canon.y)<=1 and (canon.x >= x1 and canon.x <=x2):
                self.destroycanon(canon , king)
            if abs(y1-canon.y)<=1 and (canon.x >= x1 and canon.x <=x2):  
                self.destroycanon(canon , king)
            if abs(x1 - canon.x) <=1 and (canon.y >=y1 and canon.y<=y2):
                self.destroycanon(canon , king)
            if abs(x2 - canon.x) <=1 and (canon.y >=y1 and canon.y<=y2):
                self.destroycanon(canon , king)                       

    
    def checkgame(self , all_canons , all_wizards, all_huts , king , troop , townhall):
        player_win = 0
        computer_win = 0
        t_alive = 0
        hut_alive = 0
        for t in troop:
            if(t.health>0):
                t_alive = 1
                break
        if(t_alive == 0 and king.health<=0):
            return 0 
        for i in range(6):
            if(all_huts[i].health >0):
                hut_alive=1
        for wizard in all_wizards:
            if wizard.health>0:
                hut_alive =1
                
        for canon in all_canons:
            if canon.health>0:
                hut_alive = 1                
        if(townhall.health <= 0 and hut_alive==0):
            return 1 
        return 2 

    def attack_queen(self , king , all_canons , all_wizards , all_huts , townhall , all_bricks , last_move):
        print(townhall.health , end=" ")
        print("townhall")    
        attack_townhall = 0
        attack_huts = [0,0,0,0,0,0]
        print(last_move)
        x1 = king.x
        x2 = king.x + 3
        y1 = king.y
        y2 = king.y + 4 
        center_col = y1+2
        center_row = x1+1
        if (last_move == 'r'):
                for row in range(center_row -2 , center_row+3):
                    for col in range(center_col+6 , center_col+11):
                        if row>=23 and row<=26:
                            if col>=73 and col<=77:
                                if attack_townhall==0:
                                    attack_townhall = 1
                                    townhall.health = townhall.health - king.damage
                                    if(townhall.health>60 and townhall.health<=100):
                                        townhall.setMatrix()
                                        self.placeElement(townhall)
                                        
                                    if(townhall.health>30 and townhall.health<=60):
                                        townhall.setMatrix2()
                                        self.placeElement(townhall)    
                                        
                                    if(townhall.health>0 and townhall.health<=30):
                                        townhall.setMatrix3()
                                        self.placeElement(townhall) 
                                        
                                    if(townhall.health<=0):
                                        townhall.setMatrix4()
                                        townhall.health = -1
                                        self.placeElement(townhall)
                                        for p in range(townhall.x , townhall.x + townhall.rows):
                                            for j in range(townhall.y , townhall.y+townhall.cols):
                                                all_coord.remove((p,j))

                        for i in range(6):
                            if row >=all_huts[i].x and row<=all_huts[i].x+3:
                                if col>=all_huts[i].y and col<=all_huts[i].y+2:
                                    if attack_huts[i] == 0:
                                        all_huts[i].health = all_huts[i].health - king.damage
                                        attack_huts[i] = 1
                                        if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                                            all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])
                                        if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                                            all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])  
                                        if(all_huts[i].health > 0 and all_huts[i].health <= 30 ):
                                            all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])    
                                        if(all_huts[i].health <=0 ):
                                            all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                                            all_huts[i].health = -1
                                            self.placeElement(all_huts[i])   
                                            for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                                                for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                                                    all_coord.remove((p,j))    
                        if ((row == 20 and (col>=70 and col <=78)) or (row == 28 and (col>=70 and col<=78)) or (col==70 and (row>=20 and row<=28)) or (col==78 and (row>=20 and row<=28))):    
                            self._grid[row][col] = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET    
                            if(row , col) in all_coord:
                                all_coord.remove((row , col))  

                        for wizard in all_wizards:
                            if wizard.x == row and wizard.y == col:
                                self.destroywizard(wizard , king)
                        for canon in all_canons:
                            if canon.x == row and canon.y == col:
                                self.destroycanon(canon , king)        

                
        elif (last_move == 'l'):
            for row in range(center_row -2 , center_row+3):
                for col in range(center_col-10 , center_col-5):
                        if row>=23 and row<=26:
                            if col>=73 and col<=77:
                                if attack_townhall==0:
                                    attack_townhall = 1
                                    townhall.health = townhall.health - king.damage
                                    if(townhall.health>60 and townhall.health<=100):
                                        townhall.setMatrix()
                                        self.placeElement(townhall)
                                        
                                    if(townhall.health>30 and townhall.health<=60):
                                        townhall.setMatrix2()
                                        self.placeElement(townhall)    
                                        
                                    if(townhall.health>0 and townhall.health<=30):
                                        townhall.setMatrix3()
                                        self.placeElement(townhall) 
                                        
                                    if(townhall.health<=0):
                                        townhall.setMatrix4()
                                        townhall.health = -1
                                        self.placeElement(townhall)
                                        for p in range(townhall.x , townhall.x + townhall.rows):
                                            for j in range(townhall.y , townhall.y+townhall.cols):
                                                all_coord.remove((p,j))
                                                

                        for i in range(6):
                            if row >=all_huts[i].x and row<=all_huts[i].x+3:
                                if col>=all_huts[i].y and col<=all_huts[i].y+2:
                                    if attack_huts[i] == 0:
                                        all_huts[i].health = all_huts[i].health - king.damage
                                        attack_huts[i] = 1
                                        if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                                            all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])
                                        if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                                            all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])  
                                        if(all_huts[i].health > 0 and all_huts[i].health <= 30 ):
                                            all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])    
                                        if(all_huts[i].health <=0 ):
                                            all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                                            all_huts[i].health = -1
                                            self.placeElement(all_huts[i])   
                                            for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                                                for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                                                    all_coord.remove((p,j)) 
                        if ((row == 20 and (col>=70 and col <=78)) or (row == 28 and (col>=70 and col<=78)) or (col==70 and (row>=20 and row<=28)) or (col==78 and (row>=20 and row<=28))):    
                            self._grid[row][col] = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET 
                            if(row , col) in all_coord:
                                all_coord.remove((row , col))   
                        for wizard in all_wizards:
                            if wizard.x == row and wizard.y == col:
                                self.destroywizard(wizard , king)
                        for canon in all_canons:
                            if canon.x == row and canon.y == col:
                                self.destroycanon(canon , king)                                                           

        elif (last_move == 'u'):
            for row in range(center_row-10 , center_row-5):
                for col in range(center_col-2 , center_col+3):
                        if row>=23 and row<=26:
                            if col>=73 and col<=77:
                                if attack_townhall==0:
                                    attack_townhall = 1
                                    townhall.health = townhall.health - king.damage
                                    if(townhall.health>60 and townhall.health<=100):
                                        townhall.setMatrix()
                                        self.placeElement(townhall)
                                        
                                    if(townhall.health>30 and townhall.health<=60):
                                        townhall.setMatrix2()
                                        self.placeElement(townhall)    
                                        
                                    if(townhall.health>0 and townhall.health<=30):
                                        townhall.setMatrix3()
                                        self.placeElement(townhall) 
                                        
                                    if(townhall.health<=0):
                                        townhall.setMatrix4()
                                        townhall.health = -1
                                        self.placeElement(townhall)
                                        for p in range(townhall.x , townhall.x + townhall.rows):
                                            for j in range(townhall.y , townhall.y+townhall.cols):
                                                all_coord.remove((p,j))                                                

                        for i in range(6):
                            if row >=all_huts[i].x and row<=all_huts[i].x+3:
                                if col>=all_huts[i].y and col<=all_huts[i].y+2:
                                    if attack_huts[i] == 0:
                                        all_huts[i].health = all_huts[i].health - king.damage
                                        attack_huts[i] = 1
                                        if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                                            all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])
                                        if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                                            all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])  
                                        if(all_huts[i].health > 0 and all_huts[i].health <= 30 ):
                                            all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])    
                                        if(all_huts[i].health <=0 ):
                                            all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                                            all_huts[i].health = -1
                                            self.placeElement(all_huts[i])   
                                            for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                                                for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                                                    all_coord.remove((p,j))
                        if ((row == 20 and (col>=70 and col <=78)) or (row == 28 and (col>=70 and col<=78)) or (col==70 and (row>=20 and row<=28)) or (col==78 and (row>=20 and row<=28))):    
                            self._grid[row][col] = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET 
                            if(row , col) in all_coord:
                                all_coord.remove((row , col))                                                                                
                        for wizard in all_wizards:
                            if wizard.x == row and wizard.y == col:
                                self.destroywizard(wizard , king)
                        for canon in all_canons:
                            if canon.x == row and canon.y == col:
                                self.destroycanon(canon , king)                                                       
        elif (last_move == 'd'):
            for row in range(center_row+6 , center_row+11):
                for col in range(center_col-2 , center_col+3):
                        if row>=23 and row<=26:
                            if col>=73 and col<=77:
                                if attack_townhall==0:
                                    attack_townhall = 1
                                    townhall.health = townhall.health - king.damage
                                    if(townhall.health>60 and townhall.health<=100):
                                        townhall.setMatrix()
                                        self.placeElement(townhall)
                                        
                                    if(townhall.health>30 and townhall.health<=60):
                                        townhall.setMatrix2()
                                        self.placeElement(townhall)    
                                        
                                    if(townhall.health>0 and townhall.health<=30):
                                        townhall.setMatrix3()
                                        self.placeElement(townhall) 
                                        
                                    if(townhall.health<=0):
                                        townhall.setMatrix4()
                                        townhall.health = -1
                                        self.placeElement(townhall)
                                        for p in range(townhall.x , townhall.x + townhall.rows):
                                            for j in range(townhall.y , townhall.y+townhall.cols):
                                                all_coord.remove((p,j))                                                 

                        for i in range(6):
                            if row >=all_huts[i].x and row<=all_huts[i].x+3:
                                if col>=all_huts[i].y and col<=all_huts[i].y+2:
                                    if attack_huts[i] == 0:
                                        all_huts[i].health = all_huts[i].health - king.damage
                                        attack_huts[i] = 1
                                        if(all_huts[i].health > 60 and all_huts[i].health <= 100 ):
                                            all_huts[i].setMatrix(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])
                                        if(all_huts[i].health > 30 and all_huts[i].health <= 60 ):
                                            all_huts[i].setMatrix2(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])  
                                        if(all_huts[i].health > 0 and all_huts[i].health <= 30 ):
                                            all_huts[i].setMatrix3(all_huts[i].x , all_huts[i].y)
                                            self.placeElement(all_huts[i])    
                                        if(all_huts[i].health <=0 ):
                                            all_huts[i].setMatrix4(all_huts[i].x , all_huts[i].y)
                                            all_huts[i].health = -1
                                            self.placeElement(all_huts[i])   
                                            for p in range(all_huts[i].x , all_huts[i].x + all_huts[i].rows):
                                                for j in range(all_huts[i].y , all_huts[i].y+all_huts[i].cols):
                                                    all_coord.remove((p,j))
                        if ((row == 20 and (col>=70 and col <=78)) or (row == 28 and (col>=70 and col<=78)) or (col==70 and (row>=20 and row<=28)) or (col==78 and (row>=20 and row<=28))):    
                            self._grid[row][col] = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET  
                            if(row , col) in all_coord:
                                all_coord.remove((row , col))                                                                                                       
                        for wizard in all_wizards:
                            if wizard.x == row and wizard.y == col:
                                self.destroywizard(wizard , king)
                        for canon in all_canons:
                            if canon.x == row and canon.y == col:
                                self.destroycanon(canon , king)   
        
    def check_walls(self):
        for i in range(9):
            if (20,70+i) in all_coord:
                self._grid[20][70+i] = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET 
        for i in range(9):
            if (28,70+i) in all_coord:
                self._grid[28][70+i] = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET           
        for i in range(8):
            if (20+i,70) in all_coord:
                self._grid[20+i][70] = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET
        for i in range(8):     
            if (20+i,78) in all_coord:
                self._grid[20+i][78] = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET        



    def destroycanon(self , canon , king ):
        canon.health = canon.health - king.damage
        if(canon.health>60 and canon.health<=100):
            canon.setMatrix(canon.x , canon.y)
            self.placeElement(canon)               
        if(canon.health>30 and canon.health<=60):
            canon.setMatrix(canon.x , canon.y)
            self.placeElement(canon) 
        if(canon.health>0 and canon.health<=30):
            canon.setMatrix3(canon.x , canon.y)
            self.placeElement(canon)  
        if(canon.health<=0):
            canon.setMatrix4(canon.x , canon.y)
            self.placeElement(canon)  
            all_coord.remove((canon.x,canon.y))        
        if(canon.health < 0):
            canon.health = -1 

    def destroywizard(self , canon , king):
        canon.health = canon.health - king.damage
        if(canon.health>60 and canon.health<=100):
            canon.setMatrix(canon.x , canon.y)
            self.placeElement(canon)               
        if(canon.health>30 and canon.health<=60):
            canon.setMatrix(canon.x , canon.y)
            self.placeElement(canon) 
        if(canon.health>0 and canon.health<=30):
            canon.setMatrix3(canon.x , canon.y)
            self.placeElement(canon)  
        if(canon.health<=0):
            canon.setMatrix4(canon.x , canon.y)
            self.placeElement(canon)  
            all_coord.remove((canon.x,canon.y))        
        if(canon.health < 0):
            canon.health = -1     

                            
