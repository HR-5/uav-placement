import numpy as np

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
        # print("t = "+str(noOfUsers))
        # if(timeFracPerUser == 0):
        #     break

        for i in range(len(usr)):
            ind = usr[i]["id"]-1
            if((t[ind]+timeFracPerUser)*Caps[ind]>=Rates[ind]):
                # print("jdsjk")
                fractUsed = Rates[ind]/Caps[ind]-t[ind]
                t[ind] = Rates[ind]/Caps[ind]
                timeFracAvail = timeFracAvail - fractUsed
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

    return throughput

