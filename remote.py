class r:
    def __init__(self):
        global pulseio
        global board
        global array
        global pwmio
        import pulseio
        import board
        import array
        import pwmio

        global pulsesOutputter
        pulsesOutputter = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=int((25 / 100) * 65536))

        self.listen   = False

        self.ERROR    =    100
        self.ADRESS   =   '10'
        self.ONTIME   =   600
        self.ZEROTIME =   600
        self.ONETIME  =   1650

        self.POWER    = '8'
        self.BACK     = '10'
        self.HOME     = '61'
        self.OK       = '2D'
        self.UP       = '35'
        self.RIGHT    = '4D'
        self.DOWN     = '75'
        self.LEFT     = 'D'
        self.REFRESH  = '41'
        self.MOON     = '2C'
        self.STAR     = '18'
        self.BACK     = '79'
        self.PAUSE    = '21'
        self.SKIP     = '6D'
        self.NETFLIX  = '19'
        self.HULU     = '1D'
        self.SLING    = '51'
        self.NOW      = '73'

        self.VOLUP    = '20'
        self.VOLDOWN  = '60'
        self.VOLMUTE  = '48'

    def flip(self, inArray):
        for i in range(len(inArray)):
            inArray[i]=not inArray[i]
        return inArray

    def hexToBinList(self, hex):
        return list(map(int, list('0'*(7-len(bin(int(hex, 16))[2:]))+bin(int(hex, 16))[2:])))

    def encode(self, hex, check = 0):
        binArray = self.hexToBinList(hex)+[check]+self.flip(self.hexToBinList(hex))+[not check]
        outArray = array.array('H', [])
        for i in binArray:
            if(i):
                outArray.extend(array.array('H', [self.ONTIME, self.ONETIME]))
            else:
                outArray.extend(array.array('H', [self.ONTIME, self.ZEROTIME]))
        return outArray

    def genArray(self, hex):
        outArray = array.array('H', [])
        outArray.extend(array.array('H', [9000, 4450]))
        outArray.extend(self.encode(self.ADRESS))
        outArray.extend(self.encode(hex))
        outArray.extend(array.array('H', [self.ONTIME, 40000]))
        return outArray

    def send(self, command):
        pulsesOutputter.send(self.genArray(getattr(self, command.upper())))
        print('Sent: ' + str(command.upper()))
    def sendArray(self, array):
        for i in array:
            pulsesOutputter.send(self.genArray(getattr(self, i.upper())))
