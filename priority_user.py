import numpy as np

def findDist(p1,p2):
    dj = np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return dj

def optimalPos(grid_points,user):
    print(user)
    minDist = findDist(grid_points[0],user)
    minPt = grid_points[0]
    for point in grid_points:
        # print(point)
        dist = findDist(point,user)
        if(dist<minDist):
            minDist=dist
            minPt = point

    return minPt