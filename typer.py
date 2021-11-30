class typer:
    def __init__(self):
        '''
        keyboardArray       3d array that represents the keyboard
        layerSwitch         array that represets the cordanites where the layer swich is and the direction it should go after it
                            eg. [6,5,'right']
        setup               function that gets called before typing anythnig
        space()             how to send a space
        '''
        self.keyboardArray = keyboardArray
        self.layerSwich =    layerSwich

    def findChar(self, char):
        for x in range(len(self.keyboardArray)):
            for y in range(len(self.keyboardArray[0])):
                for z in range(len(self.keyboardArray[0][0])):
                    if(str(self.keyboardArray[x][y][z])==str(char)):
                        return [x,y,z]
    def path2d(start, finish):
        vector=[finish[0]-start[0],finish[1]-start[1]]
        dirX=['right' if vector[0]>0 else 'left']
        dirY=['down' if vector[1]>0 else 'up']
        if(abs(vector[0])>abs(vector[1])):
            path=(dirX+dirY)*abs(vector[1])+((dirX+['star'])*abs(abs(vector[1])-abs(vector[0])))
        else:
            path=(dirY+dirX)*abs(vector[0])+((dirY+['star'])*abs(abs(vector[1])-abs(vector[0])))
        return path
    def findPath(self,start,finish):
        path=[]
        if(start[2]!=finish[2]):

        path.extend(path2d(start,finish))
        path.append('ok')
        return path
    def typer(str):
        curPos = [0,0,0]
        for i in str:
