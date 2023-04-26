import random

def tabu_search(initial_pos,grid_points,maxIter,maxTabuIter,clusThr,pri_uav):
    current_sol = initial_pos
    tabulist = []
    best_sol = current_sol
    # print(initial_pos)
    # print(grid_points)
    # print(clusThr)
    bestThr = sysThroughput(best_sol,clusThr)
    print(bestThr)
    for i in range(len(grid_points)):
        lis = [-1 for j in range(len(grid_points[i]))]
        tabulist.append(lis)
    
    it = 1
    while it < maxIter:
        candidate_pos = current_sol
        best_candidate = current_sol
        bestCandThr = 0
        uav = pri_uav
        # while(uav == pri_uav):
        uav = random.randint(0,len(grid_points)-1)
        neighbours = neighbouringPos(uav,current_sol,len(grid_points[uav]))
        print(neighbours)
        while len(neighbours) != 0:
            k = neighbours[0][uav]
            candidate_pos = neighbours[0]
            neighbours.pop(0)    
            if tabulist[uav][k] < it - maxTabuIter:
                thr = sysThroughput(candidate_pos,clusThr)
                print(str(candidate_pos)+str(thr))
                if thr > bestCandThr:
                    best_candidate = candidate_pos
                    bestCandThr = thr
                    return
        current_sol = best_candidate
        bestCanPos = current_sol[uav]
        print(bestCanPos)
        if bestCandThr > bestThr:
            best_sol = current_sol
            bestThr = bestCandThr
        tabulist[uav][bestCanPos] = it
        it = it +1
    
    print(best_sol)
    return best_sol



def neighbouringPos(uavPos,current_sol,len):
    nPos = []
    print(uavPos)
    print(len)
    for i in range(len):
        print(i)
        csol = current_sol
        csol[uavPos] = i
        nPos.append(csol)
    
    return nPos

def sysThroughput(pos,clusThr):
    totThr = 0
    for i,p in enumerate(pos):
        totThr = totThr + clusThr[i][p]
    return totThr
