import math
import numpy as np

# def calCapacityphy():


def computeCapacity(pg,users,i,pt):
    C = [] #Capacity
    for user in users:
        # pt = 1 #transmission power of the UAV is 1W
        coord = user["coord"]
        f = 2.4*pow(10,9) #frequency 2.4 GHz
        c = 3*pow(10,8) #speed of light
        dj = np.sqrt((coord[0]-pg[0])**2 + (coord[1]-pg[1])**2)
        # pr = pt*np.square((4*math.pi*dj*f/c))
        pr = pt*np.square((c/(f*4*math.pi*dj)))
        pr_dBm = 10*math.log(pr,10)+30
        print(pr_dBm)
        # print("dj = "+str(dj))
        # print("x"+str(pr/pt))
        # print("pr"+str(pr))
        # sinr = pr/(i+n)
        #Cj_phy
        #Cj
        C.append(250/dj)
    print(C)
    return C
        
