from colorama import Fore, Back, Style
import numpy as np 
from background import *

class boardElements:
    def __init__(self , cols , rows):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        self.name=""
        self.health = 100
        self.x=0
        self.y=0

