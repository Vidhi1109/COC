x=0
inputnum = input()
file = open("times.txt", "r")
for line in file:
    for char in line:
        x = char
file = open("replay"+x+".txt", "r")
outputstr=""
loop = 0
for line in file:
    for character in line:
        if(character == 's'):
            while loop != 1000000:
                loop = loop +1
            print(outputstr)
            loop  = 0
            outputstr=""
        else:
            outputstr+=character    
