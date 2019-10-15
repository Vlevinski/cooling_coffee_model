from __future__ import unicode_literals
import matplotlib.pyplot as plt
import csv

'''
## Simulation of a cooling cup of coffee
## by Newtons law of cooling asserts
                                @vlevinski
'''

class System():


    def __init__(self, initT = None, volume = None, r = None, tEnv = None, tEnd = None, dT= None):
        '''
        ##   system model for Newton law of cooling asserts
        :param initT:
        :param volume:
        :param r:
        :param tEnv:
        :param tEnd:
        :param dT:
        '''
        self.initT = initT
        self.volume= volume
        self.r = r
        self.tEnv = tEnv
        self.tEnd =tEnd
        self.dT = dT


    def getSystem(self):
        '''
        ## print System params
        :return:
        '''
        print ("#System state")
        print ("init : ", self.initT)
        print ("volume:", self.volume)
        print ("r :    ", self.r)
        print ("tEnv : ", self.tEnv)
        print ("tEnd : ", self.tEnd)
        print ("dT   : ", self.dT)


    def setInit(self, t=None):
        '''
        ## Temperature value set-up
        :param t:
        :return:
        '''
        self.initT = t


    def roundInit(self):
        '''
        ## Round the value
        :return:
        '''
        return round(self.initT,2)


    def updateState(self):
        '''
        ## Calculations
        :return:
        '''
        T = self.initT
        T += -self.r*(T -self.tEnv)*self.dT
        return self.setInit(t=T)

def main():

    # start the process
    initT = 90
    coffee = System(initT=initT, volume=300,r=0.02, tEnv=22, tEnd=30, dT=1)

    ## follow the process
    x = [0]; y = [initT];
    for i in range(1, 250):
        coffee.updateState()
        x.append(i)
        y.append(coffee.roundInit())

    #make it visual
    plt.plot(x,y,'-r',label='Total', linewidth=2.5)
    plt.title("Coolling coffee model")
    plt.xlabel("Time, min.")
    plt.ylabel("Temperature, Celcius deg..")
    plt.legend(loc='best')
    plt.grid(b=True, linewidth=0.5)
    plt.show()
#    plt.savefig("coolingCoffeModel/coolingCoffee.png")


    data = [['Time', 'Temperture']]
    for row in range(len(x)):
        data.append([x[row],y[row]])

    with open('coolingCoffeModel/cooling_coffee_model.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
        f.close()

main()

