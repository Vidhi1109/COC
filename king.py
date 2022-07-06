from colorama import Fore, Back, Style
import numpy as np 
from background import *
from elements import *
from global_var import *
class king(boardElements):
    def __init__(self , background):
        boardElements.__init__(self,4 , 3)
        self.name = "king"
        self.damage = 20
        self.movement_speed = 1
        self.health = 100
    def setMatrix(self , x , y): 
        hyph = Back.RED + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        slash = Back.RED + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.RED + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.RED + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.RED + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[space,slash,bslash,slash],
        [space,straight,straight,slash],
        [space,straight,straight,space]
        ]
        self.x = x
        self.y = y

                

                     
        '''
        self.matrix = [
            list(Fore.BLACK + Back.MAGENTA + "   ^^^^^        " + Fore.RESET+Back.RESET),
            list("   /   \\       "),
            list("   \\   /  //// "),
            list("   /    \\////  "),
            list("   |  |  |      "),
            list("    ---         ")
      ]
        print(len(self.matrix[0]))
        '''
        '''
        hyph = Back.MAGENTA + Fore.BLACK + '-' + Fore.RESET + Back.RESET
        slash = Back.MAGENTA + Fore.BLACK + '/' + Fore.RESET + Back.RESET
        space = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET
        bslash = Back.MAGENTA + Fore.BLACK + '\\' + Fore.RESET + Back.RESET
        straight = Back.MAGENTA + Fore.BLACK + '|' + Fore.RESET + Back.RESET
        colorspace = Back.MAGENTA + Fore.BLACK + ' ' + Fore.RESET + Back.RESET 
        self.matrix = [[slash,bslash],
        [straight,straight],
        [hyph,hyph]
        ]
        '''
        '''
        self.matrix = [
            [' ',' ','^','^','^',' ',' '],
            [' ',' ','\\',' ','/',' ',' '],

        ]
        '''

        #list("  / . . \\  ////"),