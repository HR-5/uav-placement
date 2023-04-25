import random

def tabu_search(initial_pos,neighbouring_fn,grid_points,maxIter):
    current_sol = initial_pos
    tabulist = []
    best_sol = current_sol

    for i in range(len(grid_points)):
        lis = [-1 for j in range(len(grid_points[i]))]
        tabulist.append(lis)
    
    it = 1
    while it < maxIter:
        candidate_pos = current_sol
        best_candidate = current_sol
        bestCandThr = 0
        uav = random.randint(0,len(grid_points)-1)
        neighbours = neighbouringPos(uav,current_sol,len(grid_points[uav]))
        while len(neighbours) != 0:
            k = neighbours[0][uav]
            neighbours.pop()



def neighbouringPos(uavPos,current_sol,len):
    nPos = []
    for i in range(len):
        csol = current_sol
        csol[uavPos] = i
        nPos.append(csol)
    
    return nPos
