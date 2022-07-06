from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
from global_var import *
class queen(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,4 , 3)
        self.name = "queen"
        self.damage = 10
        self.movement_speed = 1
        self.health = 100
    def setMatrix(self , x , y): 
        hyph = Back.YELLOW + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        slash = Back.YELLOW + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.YELLOW + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.YELLOW + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.YELLOW + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.YELLOW + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,slash,bslash,slash],
        [space,straight,straight,slash],
        [space,straight,straight,space]
        ]
        self.x = x
        self.y = y
