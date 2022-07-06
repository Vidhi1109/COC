from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
class huts(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,2 , 3)
        self.name = "hut"
    def setMatrix(self , x , y):    
        hyph = Back.MAGENTA + Fore.BLACK + '-' 
        slash = Back.MAGENTA + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.MAGENTA + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.MAGENTA + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[slash,bslash],
        [straight,straight],
        [hyph,hyph]
        ]
        self.x = x
        self.y = y

    def setMatrix2(self , x , y):    
        hyph = Back.YELLOW + Fore.BLACK + '-' 
        slash = Back.YELLOW + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.YELLOW + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.YELLOW + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.YELLOW + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.YELLOW + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[slash,bslash],
        [straight,straight],
        [hyph,hyph]
        ]
        self.x = x
        self.y = y

    def setMatrix3(self , x , y):    
        hyph = Back.WHITE + Fore.BLACK + '-' 
        slash = Back.WHITE + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.WHITE + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.WHITE + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.WHITE + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.WHITE + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[slash,bslash],
        [straight,straight],
        [hyph,hyph]
        ]
        self.x = x
        self.y = y


    def setMatrix4(self , x , y):    
        hyph = Back.WHITE + Fore.BLACK + '-' 
        slash = Back.WHITE + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.GREEN + Fore.GREEN + ' ' + Back.RESET + Fore.RESET
        bslash = Back.WHITE + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.WHITE + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.WHITE + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,space],
        [space,space],
        [space,space]
        ]
        self.x = x
        self.y = y
