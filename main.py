import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import sqrt
import grid_points
import optimal_position
import random
import enclosing_circle
import tabu_search
import priority_weight


# set the mean and covariance matrix
def compute_cluster(mean,cov,enclosing_circle,ax):

    # generate random points
    points = np.random.multivariate_normal(mean, cov, 20)
    mec = enclosing_circle.minimum_enclosing_circle(points)


    Users = []
    for ind,point in enumerate(points):
        user = {"id":ind+1,"coord":point,"upi":random.randint(1,5)}
        Users.append(user)

    c_sec = (mec[0][0],mec[0][1])
    r_sec = mec[1]
    c_con = c_sec
    r_con = 3*r_sec/2 - r_sec

    # create a Circle patch object with the given c_sec and radius
    enclosing_circle = Circle(c_sec, r_sec, alpha=0.2, edgecolor='maroon', fill=False)
    containing_circle = Circle(c_sec, r_con, alpha=0.2, edgecolor='coral', fill=False)
    
    # add the circle to the axis object
    ax.add_patch(enclosing_circle)
    ax.add_patch(containing_circle)

    grid_x,grid_y = grid_points.grid_points(c_con,r_con)
    grids = np.column_stack((grid_x,grid_y))
    
    Rates = []
    for i in range(len(points)):
        Rates.append(random.uniform(1.5,2))

    throughputList,maxId = optimal_position.optimalPosition(Users,Rates,0.01,grids,1)
   
    return (c_con[0]-r_sec,c_con[0]+r_sec,c_con[1]-r_sec,c_con[1]+r_sec,throughputList,Users,maxId)


 # create a figure and axis object
fig, ax = plt.subplots()
mean = [0, 0]
cov = [[50, 10], [10, 50]]
xl1,xe1,yl1,yr1,thrList1,user1,maxId1 = compute_cluster(mean,cov,enclosing_circle,ax)
mean = [0, 50]
cov = [[50, 10], [10, 50]]
xl2,xe2,yl2,yr2,thrList2,user2,maxId2 = compute_cluster(mean,cov,enclosing_circle,ax)
mean = [200, 30]
cov = [[50, 10], [10, 50]]
xl3,xe3,yl3,yr3,thrList3,user3,maxId3 = compute_cluster(mean,cov,enclosing_circle,ax)
mean = [100, 30]
cov = [[50, 10], [10, 50]]
xl4,xe4,yl4,yr4,thrList4,user4,maxId4 = compute_cluster(mean,cov,enclosing_circle,ax)
clusterThr = [thrList1,thrList2,thrList3,thrList4]
users = [user1,user2,user3,user4]
usrs = user1+user2+user3+user4
x = [point['coord'][0] for point in usrs]
y = [point['coord'][1] for point in usrs]
uav = random.randint(0,3)
finalPt = priority_weight.mean_pos(users[uav],uav,clusterThr[uav])
ini_pos = [0,0,0,0]
ini_pos[uav] = finalPt
best_sol_pri,thr_pri = tabu_search.tabu_search(ini_pos,10,1,clusterThr,uav)
best_sol,thr_op = tabu_search.tabu_search(ini_pos,10,1,clusterThr,4)
best_x = []
best_y = []
for i,pts in enumerate(best_sol):
    d = next((d for d in clusterThr[i] if d["id"] == pts), None)
    best_x.append(d["pt"][0])
    best_y.append(d["pt"][1])

plt.scatter(x,y,color="blue",label="Users")
plt.scatter(best_x,best_y,color="green",label="Optimal Position")
plt.scatter([best_x[uav]],[best_y[uav]],color="pink",label="Priority Position")
# set the x and y limits of the axis to show the circle
ax.set_xlim(min(xl1,xl2,xl3,xl4)-2,max(xe1,xe2,xe3,xe4)+2)
ax.set_ylim(min(yl1,yl2,yl3,yl4)-2,max(yr1,yr2,yr3,yr4)+2)
legend = plt.legend(loc='upper right')
plt.figure(2)
plt.bar(["Tabu Search","Tabu Search w Priority"],[thr_op,thr_pri])

plt.show()
input()