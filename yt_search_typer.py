import math
import time
from remote import r
r = r()

alphabetytSearch = '''
abcdefg
hijklmn
opqrstu
vwzyz-'
'''
specialytSearch = '''
123&#()
456@!?:
789.-_"
0/$%+[]
'''

#prints out a 3d array
def print3d(array):
    for z in range(len(array[0][0])):
        for y in range(len(array[0])):
            for x in range(len(array)):
                print(array[x][y][z], end=' ')
            print()
        print('\n')

#creates an empty 2d array given dimentions
def createNullArray(x,y):
    return [['null']*y for i in range(x)]

#counts number of characetrs in string
def cstring(char, str):
    return sum(map(lambda x : 1 if char in x else 0, str))
#counts number of characters befor first character
def rstring(char, str):
    return len(str.split(char)[0])
#creates a 2d array based on keyboard
def createkeyboard(string):
    string=string[1:]
    xLen=rstring('\n',string)
    yLen=cstring('\n',string)
    array=createNullArray(xLen,yLen)
    string=[value for value in string if value != '\n']
    for y in range(yLen):
        for x in range(xLen):
            array[x][y]=string.pop(0)
    return array
#combines two 2d arrays into 3d arrays
def clean3d(array):
    cleanArray = array[0]
    for x in range(len(cleanArray)):
        for y in range(len(cleanArray[0])):
            cleanArray[x][y] = [array[0][x][y],array[1][x][y]]
    return cleanArray
#create the keyboard array
keyboardYTsearch=clean3d([createkeyboard(alphabetytSearch),createkeyboard(specialytSearch)])
#finds the cords of a char on the keyboard
def find(char, array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            for z in range(len(array[0][0])):
                if(str(array[x][y][z])==str(char)):
                    return [x,y,z]
    return False
#finds the path from one pos to end pos
def path2d(start, finish):
    vector=[finish[0]-start[0],finish[1]-start[1]]
    dirX=['right' if vector[0]>0 else 'left']
    dirY=['down' if vector[1]>0 else 'up']
    if(abs(vector[0])>abs(vector[1])):
        path=(dirX+dirY)*abs(vector[1])+((dirX+['star'])*abs(abs(vector[1])-abs(vector[0])))[:-1]
    else:
        path=(dirY+dirX)*abs(vector[0])+((dirY+['star'])*abs(abs(vector[1])-abs(vector[0])))[:-1]
    return path
#accounts for switching layers
def pathfind(start, finish):
    path=[]
    if(start[2]!=finish[2]):
        path.extend(path2d(start,[6,1])+['star','right','ok','left','star'])
        start=[6,1]
    path.extend(path2d(start,finish))
    path.append('ok')
    path.append('star')
    return path
#the main function
def ytSearch(string)
    #sends some commands to put the cursor at 0,0
    r.sendArray(['back','star','back',]+(['up','star']*4)[:-1])
    r.sendArray(path2d([0,0],[0,4])+['right','ok']+(['up','star']*4)[:-1])
    curPos=[0,0,0]
    for char in string:
        #accounts for the space char
        if(char==' '):
            r.sendArray(['down','star']*(4-curPos[1])+['ok','up'])
            curPos=[curPos[0],3,curPos[2]]
        else:
            #paths from the curent char to the next char
            r.sendArray(pathfind(curPos,find(char,keyboardYTsearch)))
            curPos=find(char,keyboardYTsearch)

print3d(keyboardYTsearch)
while True:
    ytSearch(input('Input a string that you would like to type\n'))
