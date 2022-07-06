from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
class wizard_tower(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,1 , 1)
        self.name = "wizard_tower"
        self.range = 6
        self.damage = 20
        self.health = 100
    def setMatrix(self , x , y):    
        hyph = Back.MAGENTA + Fore.BLACK + '-' 
        slash = Back.MAGENTA + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        alpha_c = Back.WHITE + Fore.BLACK + 'W' + Fore.RESET + Back.RESET
        space = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.MAGENTA + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.MAGENTA + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[alpha_c]]
        self.x = x
        self.y = y

    def setMatrix2(self , x , y):    
        hyph = Back.MAGENTA + Fore.BLACK + '-' 
        slash = Back.MAGENTA + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        alpha_c = Back.YELLOW + Fore.BLACK + 'W' + Fore.RESET + Back.RESET
        space = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.MAGENTA + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.MAGENTA + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[alpha_c]]
        self.x = x
        self.y = y

    def setMatrix3(self , x , y):    
        hyph = Back.MAGENTA + Fore.BLACK + '-' 
        slash = Back.MAGENTA + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        alpha_c = Back.MAGENTA + Fore.BLACK + 'W' + Fore.RESET + Back.RESET
        space = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.MAGENTA + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.MAGENTA + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[alpha_c]]
        self.x = x
        self.y = y

    def setMatrix4(self , x , y):    
        hyph = Back.MAGENTA + Fore.BLACK + '-' 
        slash = Back.MAGENTA + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        alpha_c = Back.WHITE + Fore.BLACK + 'W' + Fore.RESET + Back.RESET
        space = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET
        bslash = Back.MAGENTA + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.MAGENTA + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space]]
        self.x = x
        self.y = y

    def kill(self , king , troop , background):
        if self.health <=0:
            return        
        for coord in king_coord:
            if((coord[1]>=self.y - self.range-3 and coord[1]<=self.y - self.range) or (coord[1]<=self.y+self.range +3 and coord[1]>=self.y+self.range)):
                if((coord[0]>=self.x -  self.range-3 and coord[0]<=self.x + self.range + 3)):
                    king.health = king.health - self.damage  
                    return  
            if((coord[0]>=self.x -  self.range-3 and coord[0]<=self.x -  self.range) or (coord[0]<=self.x+self.range+3   and coord[0]>=self.x+self.range)):
                if((coord[1]>=self.y - self.range-3 and coord[1]<=self.y + self.range + 3) ):
                    king.health = king.health - self.damage  
                    return                     
        for t in troop:
            if((t.y >= self.y-self.range-3 and t.y <= self.y - self.range) or (t.y<=self.y+self.range+3 and t.y>=self.y+self.range)):
                if(t.x >= self.x-self.range-3 and t.x<=self.x+self.range+3):
                    t.health = t.health - self.damage
                    if(t.health>60 and t.health<=100):
                        t.setMatrix(t.x , t.y)
                        background.placeElement(t)
                        print("King's health:" , end=" ") 
                        print(king.health)
                        background.convertToString()
                    if(t.health>30 and t.health<=60):
                        t.setMatrix2(t.x , t.y)
                        background.placeElement(t)
                        print("King's health:" , end=" ") 
                        print(king.health)                        
                        background.convertToString()
                    if(t.health>0 and t.health<=30):
                        t.setMatrix3(t.x , t.y)
                        background.placeElement(t)
                        print("King's health:" , end=" ") 
                        print(king.health)                        
                        background.convertToString()   
                    if(t.health<0):
                        t.health = -1                         
                    return
                    
            if((t.x >= self.x-self.range-3 and t.x <= self.x - self.range) or (t.x<=self.x+self.range+3 and t.x>=self.x+self.range)):
                if(t.y >= self.y-self.range-3 and t.y<=self.y+self.range+3):
                    t.health = t.health - self.damage
                    if(t.health>60 and t.health<=100):
                        t.setMatrix(t.x , t.y)
                        background.placeElement(t)
                        print("King's health:" , end=" ") 
                        print(king.health)
                        background.convertToString()
                    if(t.health>30 and t.health<=60):
                        t.setMatrix2(t.x , t.y)
                        background.placeElement(t)
                        print("King's health:" , end=" ") 
                        print(king.health)                        
                        background.convertToString()
                    if(t.health>0 and t.health<=30):
                        t.setMatrix3(t.x , t.y)
                        background.placeElement(t)
                        print("King's health:" , end=" ") 
                        print(king.health)                        
                        background.convertToString()   
                    if(t.health<0):
                        t.health = -1                         
                    return                    

