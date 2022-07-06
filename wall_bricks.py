from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
class wallBrick(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,1, 1)
        self.name="wall"
    def setMatrix(self , x , y):    
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        brick = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET
        brick_reset  = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[brick]]
        self.x = x
        self.y = y
    def setMatrix2(self , x , y):    
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        brick = Back.RED + Fore.BLACK + 'I' + Fore.RESET + Back.RESET
        brick_reset  = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[brick_reset]]
        self.x = x
        self.y = y

