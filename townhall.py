from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
class townhall(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,4 , 3)
        self.name="hall"
    def setMatrix(self):    
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        slash = Back.RED + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,hyph,hyph,space],
        [slash,space,space,bslash],
        [straight,space,space,straight]
        ]
        self.x = 23
        self.y = 73

    def setMatrix2(self):    
        hyph = Back.YELLOW + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        slash = Back.YELLOW + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.YELLOW + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.YELLOW + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.YELLOW + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.YELLOW + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,hyph,hyph,space],
        [slash,space,space,bslash],
        [straight,space,space,straight]
        ]
        self.x = 23
        self.y = 73

    def setMatrix3(self):    
        hyph = Back.WHITE + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        slash = Back.WHITE + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.WHITE + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.WHITE + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.WHITE + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.WHITE + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,hyph,hyph,space],
        [slash,space,space,bslash],
        [straight,space,space,straight]
        ]
        self.x = 23
        self.y = 73

    def setMatrix4(self):    
        hyph = Back.GREEN + Fore.GREEN + '-' + Fore.RESET + Back.RESET
        slash = Back.GREEN + Fore.GREEN + '/' + Fore.RESET + Back.RESET
        space = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET
        bslash = Back.GREEN + Fore.GREEN + '\\' + Fore.RESET + Back.RESET
        straight = Back.GREEN + Fore.GREEN + '|' + Fore.RESET + Back.RESET
        colorspace = Back.GREEN + Fore.GREEN + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,hyph,hyph,space],
        [slash,space,space,bslash],
        [straight,space,space,straight]
        ]
        self.x = 23
        self.y = 73

