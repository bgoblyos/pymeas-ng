import Devices.Common
# Common class for Stanford Research Lock-In Amplifiers
# Implements several common control commands and r/w operations
class SRCommon(Devices.Common.GPIBInstrument):
    def __init__(self, rm, address):
        super().__init__(rm, address)

    def clear(self):
        self.writeStr('*CLS;REST')

    def frequency(self, f):
        self.writeParam('FREQ', f)

    # This was taken from the original project
    # TODO: Check how it works ASAP
    def readLockIn(self, *params):
        if len(params) > 1:
            com = 'SNAP?'
            for param in params:
                com += self.par_dict[param] + ','
            com = com[:-1]
            self.writeStr(com)
            result_s = self.readValue().split(',')
            result = []
            for s in result_s:
                result.append(float(s))
            return result
        else:
            self.writeStr('OUTP?' + self.par_dict[params[0]])
            return float(self.readValue())

    def setAmplitude(self, amp):
        if float(amp)>0.004 and float(amp) < 5:
            self.writeParam('SLVL', str(amp))
        else:
            print("Invalid amplitude, must be between 0.004 and 5.0")

    def setPhase(self, phase):
        if float(phase) > -360 and float(phase) < 729.99:
            self.write('SLVL', str(phase))
        else:
            print("Invalid phase, must be between -360 and 730")

    def readFreq(self):
        self.writeStr('FREQ?')
        return float(self.readValue())
        
    def readAmp(self):
        self.writeStr('SLVL?')
        return float(self.readValue())

    def readPhase(self):
        self.writeStr('PHAS?')
        return float(self.readValue())

    def readTau(self):
        self.writeStr('OFLT?')
        return int(self.readValue())

    def readSens(self):
        self.writeStr('SENS?')
        return int(self.readValue())
    
    def triggerStartScan(self, state):
        self.writeParam('TSTR', state)

    def sampleRate(self, state):
        self.writeParam('SRAT ', state)

    def aux(self, channel, value):
        if float(value) > -10.5 and float(value) < 10.5:
            self.writeStr('AUXV '+ channel + ',' + value)

    def display(self, channel, value, ratio):
        self.writeStr('DDEF ' + channel + ',' + value + ',' + ratio)

    def harmDet(self, value):
        self.writeParam('HARM', value)

    def rest(self):
        self.writeStr('REST')

    def trigger(self):
        self.writeStr('TRIG')

    def pause(self):
        self.writeStr('PAUS')

    def readBuffer(self):
        self.writeStr('SPTS?')
        return int(self.read())

    def readBufferValue(self, firstPoint, numberOfPoints):
        self.writeStr('TRCA? 1,' + str(firstPoint) + ',' + str(numberOfPoints))
        rawResult = self.readValue()
        result = []
        for data in rawResult.split(',')[:-1]:
            result.append(float(data))
        return result
        
    # TODO: Review this
    def freqSweepSetup(self):
        tau = self.readTau()
        
        self.display('1', '1', '0')
        self.harmDet('1')
        self.triggerStartScan('1')
        if tau==9:
            self.sampleRate('5')
            sampling = 1.0/2.0
        elif tau==8:
            self.sampleRate('7')
            sampling=1.0/8.0
        elif tau==7:
            self.sampleRate('9')
            sampling=1.0/32.0
        elif tau==6:
            self.sampleRate('11')
            sampling=1.0/128.0
        elif tau==5:
            self.sampleRate('13')
            sampling=1.0/512.0
        else:
            print("Invalid time constant")
            sampling = -1
        return sampling

# SR830 class, contains dictionaries for
# sensitivity and time constant settings 
class SR830(SRCommon):
    def __init__(self, rm, address):
        super().__init__(rm, address)

        self.sensDict = {
            '2 nV' : '0',
            '5 nV' : '1',
            '10 nV' : '2',
            '20 nV' : '3',
            '50 nV' : '4',
            '100 nV' : '5',
            '200 nV' : '6',
            '500 nV' : '7',
            '1 uV' : '8',
            '2 uV' : '9',
            '5 uV' : '10',
            '10 uV' : '11',
            '20 uV' : '12',
            '50 uV' : '13',
            '100 uV' : '14',
            '200 uV' : '15',
            '500 uV' : '16',
            '1 mV' : '17',
            '2 mV' : '18',
            '5 mV' : '19',
            '10 mV' : '20',
            '20 mV' : '21',
            '50 mV' : '22',
            '100 mV' : '23',
            '200 mV' : '24',
            '500 mV' : '25',
            '1 V' : '26'
        }

        self.timeConstDict = {
            '10 us'  : '0' ,
            '30 us'  : '1' ,
            '100 us' : '2' ,
            '300 us' : '3' ,
            '1 ms'   : '4' ,
            '3 ms'   : '5' ,
            '10 ms'  : '6' ,
            '30 ms'  : '7' ,
            '100 ms' : '8' ,
            '300 ms' : '9' ,
            '1 s'    : '10',
            '3 s'    : '11',
            '10 s'   : '12',
            '30 s'   : '13',
            '100 s'  : '14',
            '300 s'  : '15',
            '1 ks'   : '16',
            '3 ks'   : '17',
            '10 ks'  : '18',
            '30 ks'  : '19'
        }
    
    def setTimeConstant(self, tc):
        self.writeParam('OFLT', tc)

    def setSensitivity(self, sens):
        self.writeParam('SENS', sens)
    


