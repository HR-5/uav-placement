import random
import math
import optimal_position
import numpy as np

def tabu_search(initial_pos,maxIter,maxTabuIter,clusThr,pri_uav):
    current_sol = initial_pos
    tabulist = []
    best_sol = current_sol
    # print(initial_pos)
    # print(grid_points)
    # print(clusThr)
    bestThr = sysThroughput(best_sol,clusThr)
    print([len(clusThr[0]),len(clusThr[1]),len(clusThr[2]),len(clusThr[3])])
    print(pri_uav)
    print(bestThr)
    for i in range(4):
        lis = [-1000000 for j in range(len(clusThr[i]))]
        tabulist.append(lis)
    
    it = 1
    while it < maxIter:
        candidate_pos = current_sol
        best_candidate = current_sol
        bestCandThr = 0
        uav = pri_uav
        while(uav == pri_uav):
            uav = random.randint(0,3)
        neighbours = neighbouringPos(uav,current_sol,len(clusThr[uav]))
        while len(neighbours) != 0:
            # print(neighbours)
            # print(bestCandThr)
            k = neighbours[0][uav]
            candidate_pos = neighbours[0]
            neighbours.pop(0)    
            if tabulist[uav][k] < it - maxTabuIter:
                thr = sysThroughput(candidate_pos,clusThr)
                # print(str(candidate_pos)+str(thr))
                if thr > bestCandThr:
                    best_candidate = candidate_pos
                    bestCandThr = thr
        current_sol = best_candidate
        bestCanPos = current_sol[uav]
        # print(bestCanPos)
        if bestCandThr > bestThr:
            best_sol = current_sol
            bestThr = bestCandThr
        tabulist[uav][bestCanPos] = it
        it = it +1

    # print(best_sol)
    # print(bestThr)
    return best_sol,bestThr



def neighbouringPos(uavPos,current_sol,len):
    nPos = []
    for i in range(len):
        csol = current_sol.copy()
        csol[uavPos] = i
        nPos.append(csol)
    return nPos

def sysThroughput(pos,clusThr):
    totThr = 0
    uavCo = []
    for i,p in enumerate(pos):
        d = next((d for d in clusThr[i] if d["id"] == p), None)
        totThr = totThr + d["thr"]
        uavCo.append(d["pt"])
    
    return totThr
