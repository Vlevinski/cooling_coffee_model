from __future__ import unicode_literals
import matplotlib.pyplot as plt

## Simulation of a cooling cup of coffee
## by Newtons law of cooling asserts

class System(object):

    ##   system model for Newton law of cooling asserts
    def __init__(self, initT = None, volume = None, r = None, tEnv = None, tEnd = None, dT= None):
        self.initT = initT
        self.volume= volume
        self.r = r
        self.tEnv = tEnv
        self.tEnd =tEnd
        self.dT = dT

    ## print System params
    def getSystem(self):
        print ("#System state")
        print ("init : ", self.initT)
        print ("volume:", self.volume)
        print ("r :    ", self.r)
        print ("tEnv : ", self.tEnv)
        print ("tEnd : ", self.tEnd)
        print ("dT   : ", self.dT)

    ## Temperature value set-up
    def setTempSystem(self, t=None):
        self.initT = t

    ## Round the value
    def getTempSystem(self):
#        print ("init : ", self.initT)
        return round(self.initT,2)

    ## Calculations
    def updateSystem(self):
        T = self.initT
        T += -self.r*(T -self.tEnv)*self.dT
        return self.setTempSystem(t=T)

def main():

    # start the process
    initT = 90
    coffee = System(initT=initT, volume=300,r=0.02, tEnv=22, tEnd=30, dT=1)

    ## follow the process
    x = [0]; y = [initT];
    for i in range(1, 250):
        coffee.updateSystem()
        x.append(i)
        y.append(coffee.getTempSystem())

    #make it visual
    plt.plot(x,y)
    plt.show()

main()

