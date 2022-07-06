import colorama
import random
from colorama import Fore, Back, Style
from background import *
from townhall import *
from huts import *
from king import *
from barbarians import *
from canon import *
from wall_bricks import *
from queen import *
from wizard_tower import *
from archers import *
from aerial import *
import termios
import subprocess as sp
import time
import tty
import sys
import os
inp = (int)(input("Press 1 king and 2 for archer queen : "))
print(inp)
from input import input
from utils import Get, input_to
colorama.init()
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
input = input()
b = background(50 , 150)
file = open("times.txt", "r")
for line in file:
    for char in line:
        x = int(char)
        x = x+1
b.num_times=x                
file.close()
file = open("times.txt", "w")
file.write(str(x))  
file.close() 
def make_and_run_game(b , level):
    b = background(50 , 150)
    last_move = 'n'
    b.archer_used = 0
    b.ballons_used = 0
    b.barbarians_used = 0
    hut_coord = set()
    barbarian_coord = set()
    king_coord = set()
    townhall_coord = set()  
    wall_coord = set() 
    all_coord = set()
    king_move=0
    king_x = 10
    king_y = 10
    t = townhall(b)
    t.setMatrix()
    b.placeElement(t)
    all_huts = []    
    for i in range(6):
        all_huts.append(huts(b))
    all_huts[0].setMatrix(random.randint(10,20),random.randint(10,40))
    b.placeElement(all_huts[0] )
    all_huts[1].setMatrix(all_huts[0].x ,all_huts[0].y + 2)
    b.placeElement(all_huts[1] )
    all_huts[2].setMatrix(all_huts[1].x ,all_huts[1].y + 2)
    b.placeElement(all_huts[2] )    
    all_huts[3].setMatrix(random.randint(10,20),random.randint(100,140))
    b.placeElement(all_huts[3] )
    all_huts[4].setMatrix(all_huts[3].x ,all_huts[3].y + 2)
    b.placeElement(all_huts[4] )
    all_huts[5].setMatrix(random.randint(30,40),random.randint(100,140))
    b.placeElement(all_huts[5] )
    if inp==1:
        k = king(b)
        k.setMatrix(10,10)
        king_x = 10
        king_y = 10
        b.placeElement(k)
    if inp==2:
        k = queen(b)
        k.setMatrix(10,10)
        b.placeElement(k)
    all_canons = []
    all_wizards = []
    canon1 = canon(b)
    canon1.setMatrix(15 , 75)
    b.placeElement(canon1)
    all_canons.append(canon1)
    wizard1 = wizard_tower(b)
    wizard1.setMatrix(13 , 75)
    b.placeElement(wizard1)
    all_wizards.append(wizard1)
    canon2 = canon(b)
    canon2.setMatrix(37 , 75)
    b.placeElement(canon2)
    all_canons.append(canon2)
    wizard2 = wizard_tower(b)
    wizard2.setMatrix(39 , 75)
    b.placeElement(wizard2)
    all_wizards.append(wizard2)
    if level == 2:
        canon3 = canon(b)
        canon3.setMatrix(all_huts[2].x+1 , all_huts[2].y + 3)
        b.placeElement(canon3)
        all_canons.append(canon3)
        wizard3 = wizard_tower(b)
        wizard3.setMatrix(all_huts[2].x+2 , all_huts[2].y + 3)
        b.placeElement(wizard3)
        all_wizards.append(wizard3)
    if level == 3:
        canon3 = canon(b)
        canon3.setMatrix(all_huts[2].x+1 , all_huts[2].y + 3)
        b.placeElement(canon3)
        all_canons.append(canon3)
        wizard3 = wizard_tower(b)
        wizard3.setMatrix(all_huts[2].x+2 , all_huts[2].y + 3)
        b.placeElement(wizard3)
        all_wizards.append(wizard3)        
        canon4 = canon(b)
        canon4.setMatrix(all_huts[4].x+1 , all_huts[4].y + 3)
        b.placeElement(canon4)
        all_canons.append(canon4)
        wizard4 = wizard_tower(b)
        wizard4.setMatrix(all_huts[4].x+1 , all_huts[4].y + 3)
        b.placeElement(wizard4)
        all_wizards.append(wizard4)            
           
    brick = wallBrick(b)
    brick.setMatrix(20,70)
    b.placeElement(brick)

    all_bricks = [] 
    cnt = 0
    for i in range(9):
        all_bricks.append(wallBrick(b))
        all_bricks[i].setMatrix(20 , 70+i)
        wall_coord.add((20,70+i))
        b.placeElement(all_bricks[i]) 
        cnt = cnt+1
    for i in range(9):
        all_bricks.append(wallBrick(b))
        all_bricks[cnt].setMatrix(28 , 70+i)
        wall_coord.add((28,70+i))
        b.placeElement(all_bricks[cnt])  
        cnt = cnt+1    
    for i in range(8):
        all_bricks.append(wallBrick(b))
        all_bricks[cnt].setMatrix(20+i , 70)
        wall_coord.add((20+i,70))
        b.placeElement(all_bricks[cnt])
        cnt = cnt+1

    for i in range(8):   
        all_bricks.append(wallBrick(b))
        all_bricks[cnt].setMatrix(20+i , 78)
        wall_coord.add((20+i,78))
        b.placeElement(all_bricks[cnt])  
        cnt = cnt + 1  

    print("King's health:" , end=" ") 
    print(k.health)
    b.convertToString()
    troop = []
    num = 100000
    loop = 0
    wait = 20
    while True:  
        loop = loop +1
        if loop%num==0 :
            for barbs in troop:
                if(barbs.health > 0):   
                    if barbs.name == "barb":
                        barbs.moveandkill(all_huts , b , t , k)   
            print("King's health:" , end=" ")
            print(k.health)  
            b.check_walls()
            if(t.health>60 and t.health<=100):
                t.setMatrix()
                b.placeElement(t)
            if(t.health>30 and t.health<=60):
                t.setMatrix2()
                b.placeElement(t)
            if(t.health>0 and t.health<=30):
                t.setMatrix3()
                b.placeElement(t)     
            if(t.health<=0):
                t.setMatrix4()
                b.placeElement(t)                         
            b.convertToString()                        
        if loop%(num/2)==0 :
            for barbs in troop:
                if(barbs.health > 0):
                    if barbs.name == "arch":
                        barbs.moveandkill(all_huts , b , t , k)   
                    if barbs.name == "aerial":
                        barbs.moveandkill(all_huts , all_canons , all_wizards , b , t , k)                                                        
            print("King's health:" , end=" ")
            print(k.health) 
            if(t.health>60 and t.health<=100):
                t.setMatrix()
                b.placeElement(t)
            if(t.health>30 and t.health<=60):
                t.setMatrix2()
                b.placeElement(t)
            if(t.health>0 and t.health<=30):
                t.setMatrix3()
                b.placeElement(t)     
            if(t.health<=0):
                t.setMatrix4()
                b.placeElement(t)
            b.check_walls()    
            b.convertToString()              
        if loop%1000000==0:            
            canon1.kill(k , troop , b)
            canon2.kill(k,troop , b) 
            wizard1.kill(k,troop , b)
            wizard2.kill(k,troop,b)
            if level == 2:
                canon3.kill(k,troop,b)
                wizard3.kill(k,troop,b)
            if level == 3:
                canon3.kill(k,troop,b)
                wizard3.kill(k,troop,b)
                canon4.kill(k,troop,b)
                wizard4.kill(k,troop,b)                                    
        if input.kbhit():
            val = input.getch()
            if(val == 'q' or val == 'Q'):
                    break
            if((val == 'a' or val == 'A') and k.health > 0):
                last_move = 'l'
                for i in range(k.movement_speed):
                    b.moveleft_king(k)
                    print("King's health:" , end=" ") 
                    print(k.health)
                    b.convertToString()
            if((val == 'w' or val == 'W') and k.health > 0):
                last_move = 'u'
                for i in range(k.movement_speed):
                    b.moveup_king(k) 
                    print("King's health:" , end=" ") 
                    print(k.health)                
                    b.convertToString()
            if((val == 'd' or val == 'D') and k.health>0):
                last_move = 'r'
                for i in range(k.movement_speed):
                    b.moveright_king(k) 
                    print("King's health:" , end=" ") 
                    print(k.health)                
                    b.convertToString()                                 
            if((val == 'S' or val == 's') and k.health>0):
                last_move = 'd'
                for i in range(k.movement_speed):
                    b.movedown_king(k) 
                    print("King's health:" , end=" ") 
                    print(k.health)                
                    b.convertToString()   
            if(val == ' '):
                    print(inp) 
                    if inp==2:
                        b.attack_queen(k ,all_canons , all_wizards, all_huts , t , all_bricks , last_move)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()
                    else:
                        b.attack_king(k , all_canons , all_wizards , all_huts, t , all_bricks) 
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString() 
            if(val == '1'):
                    if b.barbarians_used < b.barbarians:
                        barb = barbarians(b)
                        barb.setMatrix(45 , 10)
                        b.placeElement(barb)
                        troop.append(barb)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()
                        b.barbarians_used = b.barbarians_used + 1
            if(val == '2'):
                    if b.barbarians_used < b.barbarians:
                        barb = barbarians(b)
                        barb.setMatrix(0 , 15)
                        b.placeElement(barb)
                        troop.append(barb)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()
                        b.barbarians_used = b.barbarians_used + 1
    
            if(val == '3'):
                    if b.barbarians_used < b.barbarians:
                        barb = barbarians(b)
                        barb.setMatrix(0 , 145)
                        b.placeElement(barb)
                        troop.append(barb)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()
                        b.barbarians_used = b.barbarians_used + 1 
            if(val == '4'):
                    if b.archer_used < b.archers:
                        arch = archer(b)
                        arch.setMatrix(45 , 10)
                        b.placeElement(arch)
                        troop.append(arch)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()
                        b.archer_used = b.archer_used + 1
            if(val == '5'):
                    if b.archer_used < b.archers:
                        arch = archer(b)
                        arch.setMatrix(0 , 15)
                        b.placeElement(arch)
                        troop.append(arch)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString() 
                        b.archer_used = b.archer_used + 1  
            if(val == '6'):
                    if b.archer_used < b.archers:
                        arch = archer(b)
                        arch.setMatrix(0 , 145)
                        b.placeElement(arch)
                        troop.append(arch)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString() 
                        b.archer_used = b.archer_used + 1                                       
            if(val == '7'):
                    if b.ballons_used < b.ballons:
                        ballon = aerial(b)
                        ballon.setMatrix(45,10)
                        b.placeElement(ballon)
                        troop.append(ballon)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString() 
                        b.ballons_used = b.ballons_used + 1 
            if(val == '8'):
                    if b.ballons_used < b.ballons:
                        ballon = aerial(b)
                        ballon.setMatrix(0,15)
                        b.placeElement(ballon)
                        troop.append(ballon)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()
                        b.ballons_used = b.ballons_used + 1
            if(val == '9'):
                    if b.ballons_used < b.ballons:
                        ballon = aerial(b)
                        ballon.setMatrix(0,145)
                        b.placeElement(ballon)
                        troop.append(ballon)
                        print("King's health:" , end=" ") 
                        print(k.health)                
                        b.convertToString()  
                        b.ballons_used = b.ballons_used + 1                                                                                 
            if(val == 'R' or val=='r'):
                    k.movement_speed = k.movement_speed*2
                    num = num/2
                    for tx in troop:
                        tx.movement_speed = tx.movement_speed*2
                        tx.damage = tx.damage*2
                    k.damage = k.damage*2
            if(val == 'H' or val=='h'):
                    k.health = (float)(k.health*1.5)
                    for tx in troop:
                        tx.health = tx.health*1.5 
                    print("King's health:" , end=" ") 
                    print(k.health)                
                    b.convertToString()                                  
    
        else:
            pass              
        ret = b.checkgame(all_canons , all_wizards , all_huts  ,k , troop , t)   
        if(ret == 2):
            continue
        else:
            break         
    
    if(ret == 0):
        print("YOU LOST")
        return ret
    elif (ret==1):
        print("YOU WON!")    
        return ret

level = 1
res = make_and_run_game(b, level)
if res==1:
    level = level + 1
    res = make_and_run_game(b,level)
    if res==1:
        level = level+1
        res = make_and_run_game(b,level)



    