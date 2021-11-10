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
ytSignInAlpha = '''
1234567890
qwertyuiop
asdfghjkl@
zxcvbnm_-.
'''
ytSignInSpecial = '''
1234567890
|/\;:,-"'`
^~<>{}[]()
+=#%&?$*@!
'''

def printArray(array):
    for i in range(len(array[0])):
        for j in range(len(array)):
            print(array[j][i], end=' ')
        print()

def print3d(array):
    for z in range(len(array[0][0])):
        for y in range(len(array[0])):
            for x in range(len(array)):
                print(array[x][y][z], end=' ')
            print()
        print('\n')

def createNullArray(x,y):
    return [['null']*y for i in range(x)]

def cstring(char, str):
    return sum(map(lambda x : 1 if char in x else 0, str))
def rstring(char, str):
    return len(str.split(char)[0])

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
def clean3d(array):
    cleanArray = array[0]
    for x in range(len(cleanArray)):
        for y in range(len(cleanArray[0])):
            cleanArray[x][y] = [array[0][x][y],array[1][x][y]]
    return cleanArray
'''
create the keyboard layouts
'''
keyboardYTsearch=clean3d([createkeyboard(alphabetytSearch),createkeyboard(specialytSearch)])
ytSignInKey=clean3d([createkeyboard(ytSignInAlpha),createkeyboard(ytSignInSpecial)])
def find(char, array):
    for x in range(len(array)):
        for y in range(len(array[0])):
            for z in range(len(array[0][0])):
                if(str(array[x][y][z])==str(char)):
                    return [x,y,z]
    return False
def path2d(start, finish):
    vector=[finish[0]-start[0],finish[1]-start[1]]
    #print(vector)
    dirX=['right' if vector[0]>0 else 'left']
    dirY=['down' if vector[1]>0 else 'up']
    #print(dirX,dirY)
    #print(vector)
    #print(abs(vector[0])>abs(vector[1]))
    if(abs(vector[0])>abs(vector[1])):
        path=(dirX+dirY)*abs(vector[1])+((dirX+['star'])*abs(abs(vector[1])-abs(vector[0])))[:-1]
    else:
        path=(dirY+dirX)*abs(vector[0])+((dirY+['star'])*abs(abs(vector[1])-abs(vector[0])))[:-1]
    return path
def pathfind(start, finish):
    path=[]
    if(start[2]!=finish[2]):
        path.extend(path2d(start,[6,1])+['star','right','ok','left','star'])
        start=[6,1]
    path.extend(path2d(start,finish))
    path.append('ok')
    path.append('star')
    return path
def pathfindSignIn(start,finish):
    path=[]
    if(start[2]!=finish[2]):
        path.extend(path2d(start,[9,3])+['star','right','ok','left','star'])
        start=[9,3]
    path.extend(path2d(start,finish))
    path.append('ok')
    return path
def ytSearch(string):
    r.sendArray(['back','star','back',]+(['up','star']*4)[:-1])
    r.sendArray(path2d([0,0],[0,4])+['right','ok']+(['up','star']*4)[:-1])
    curPos=[0,0,0]
    for char in string:
        if(char==' '):
            r.sendArray(['down','star']*(4-curPos[1])+['ok','up'])
            curPos=[curPos[0],3,curPos[2]]
        else:
            r.sendArray(pathfind(curPos,find(char,keyboardYTsearch)))
            curPos=find(char,keyboardYTsearch)
def ytSignIn(email,password):
    r.sendArray(['left','up','star','up','ok','star','ok'])
    time.sleep(.5)
    r.send('ok')
    time.sleep(3)
    curPos=[0,0,0]
    for char in email:
        r.sendArray(pathfindSignIn(curPos,find(char,ytSignInKey)))
        curPos=find(char,ytSignInKey)
    r.sendArray(path2d(curPos,[0,0])+['star','up','ok','up','ok'])
    curPos=[0,0,0]
    time.sleep(1)
    for char in password:
        r.sendArray(pathfindSignIn(curPos,find(char,ytSignInKey)))
        curPos=find(char,ytSignInKey)
    r.sendArray(path2d(curPos,[0,0])+['star','up','star','up','ok'])

#pathfind('@','y')
print3d(ytSignInKey)
#ytSearch('sneaky')
#print(path2d([0,0],[1,3]))
#ytSearch('sneaky worlds 2020')
while True:
    ytSearch(input('enter when ready\n'))
