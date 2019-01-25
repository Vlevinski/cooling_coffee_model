from __future__ import unicode_literals
import matplotlib.pyplot as plt

## Simulation of simulation of a cooling cup of coffee
## by Newtons law of cooling asserts

class System(object):

    ##   system model for Newton law model
    def __init__(self, initT = None, volume = None, r = None, tEnv = None, tEnd = None, dT= None):
        self.initT = initT
        self.volume= volume
        self.r = r
        self.tEnv = tEnv
        self.tEnd =tEnd
        self.dT = dT

    ## print Sustem params
    def getSystem(self):
        print ("#System params")
        print ("init : ", self.initT)
        print ("volume:", self.volume)
        print ("r :    ", self.r)
        print ("tEnv : ", self.tEnv)
        print ("tEnd : ", self.tEnd)
        print ("dT   : ", self.dT)

    ## The temperature value
    def setTempSystem(self, t=None):
        self.initT = t

    def getTempSystem(self):
#        print ("init : ", self.initT)
        return round(self.initT,2)

    ## calculations
    def updateSystem(self):
        T = self.initT
        T += -self.r*(T -self.tEnv)*self.dT
#        tR = round(T,2)
        return self.setTempSystem(t=T)

def main():

    # start the prpcess
    initT = 0
    coffee = System(initT=initT,
                volume=300,
                r=0.02,
                tEnv=22,
                tEnd=30,
                dT=1)

#    coffee.getSystem()
    coffee.setTempSystem(t=90)
    coffee.getTempSystem()

    ## follow the process
    x = []; y = [];
    for i in range(250):
        coffee.updateSystem()
        x.append(i)
        y.append(coffee.getTempSystem())

    #make it visual
    plt.plot(x,y)
    plt.show()

main()

