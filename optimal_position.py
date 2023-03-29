import math
import numpy as np

def table1(pr_dBm):
    if(pr_dBm>=-40):
        return 54
    elif(pr_dBm>=-42):
        return 48
    elif(pr_dBm>=-52):
        return 36
    elif(pr_dBm>=-57):
        return 24
    elif(pr_dBm>=-66):
        return 18
    elif(pr_dBm>=-70):
        return 12
    elif(pr_dBm>=-73):
        return 9
    elif(pr_dBm>=-76):
        return 6
    
def table2(Cj_phy):
    if(Cj_phy == 54):
        return 33.27
    elif(Cj_phy == 48):
        return 29.59
    elif(Cj_phy == 36):
        return 22.14
    elif(Cj_phy == 24):
        return 14.14
    elif(Cj_phy == 18):
        return 10.42
    elif(Cj_phy == 12):
        return 6.71
    elif(Cj_phy == 9):
        return 4.85
    elif(Cj_phy == 6):
        return 3.56

def computeCapacity(pg,users,i,pt):
    C = [] #Capacity
    for user in users:
        # pt = 1 #transmission power of the UAV is 1W
        coord = user["coord"]
        f = 2.4*pow(10,9) #frequency 2.4 GHz
        c = 3*pow(10,8) #speed of light
        dj = np.sqrt((coord[0]-pg[0])**2 + (coord[1]-pg[1])**2)
        # print(dj)
        pr = pt*np.square((c/(f*4*math.pi*dj)))
        pr_dBm = 10*math.log(pr,10)+30
        # print(pr_dBm)
        Cj_phy = table1(pr_dBm)
        Cj = table2(Cj_phy)
        # print(Cj_phy)
        C.append(Cj)
        # print("Distance(dj) = "+str(dj)+" Pr(dBm) = "+str(pr_dBm)+" Capacity(Cj) = "+str(Cj))
    # print(C)
    return C


def estimateThroughput(Users,Rates,Caps):
    users = Users
    timeFracAvail = 1
    throughput = 0
    t = np.zeros(len(users))
    # print(Rates)
    while len(users) and timeFracAvail>0:
        noOfUsers = len(users)
        timeFracPerUser = timeFracAvail/noOfUsers
        usr = users
        for i in range(len(usr)):
            ind = usr[i]["id"]-1
            # print("C+ "+str((t[ind]+timeFracPerUser)*Caps[ind]))
            # print("R+ "+str(Rates[ind]))
            if((t[ind]+timeFracPerUser)*Caps[ind]>=Rates[ind]):
                # print("jdsjk")
                fractUsed = Rates[ind]/Caps[ind]-t[ind]
                t[ind] = Rates[ind]/Caps[ind]
                timeFracAvail = timeFracAvail - fractUsed
                # print(t[ind])
                for index,u in enumerate(users):
                    if(u["id"] == ind+1):
                        users = np.delete(users,index)
                        break
                # print(len(users))
            else:
                t[ind] += timeFracPerUser
                timeFracAvail -= timeFracPerUser

    for ind,cap in enumerate(Caps):
        throughput += t[ind]*cap

    print("T= "+str(throughput))
    return throughput


def optimalPosition(Users,Rates,Pt,grid_points,I):
    throughputMax = 0
    pmax = grid_points[0]
    for i,point in enumerate(grid_points):
        C = computeCapacity(point,Users,I,Pt)
        throughput = estimateThroughput(Users,Rates,C)
        if(throughputMax<throughput):
            throughputMax = throughput
            pmax = point
        
        
    return pmax