import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from math import sqrt
import grid_points
import optimal_position
import random
import enclosing_circle
import priority_user

# set the mean and covariance matrix
def compute_cluster(mean,cov,enclosing_circle,ax):
    # mean = [0, 0]
    # cov = [[50, 10], [10, 50]]

    # generate random points
    points = np.random.multivariate_normal(mean, cov, 20)
    mec = enclosing_circle.minimum_enclosing_circle(points)


    Users = []
    for ind,point in enumerate(points):
        user = {"id":ind+1,"coord":point}
        Users.append(user)

    c_sec = (mec[0][0],mec[0][1])
    r_sec = mec[1]
    c_con = c_sec
    r_con = 3*r_sec/2 - r_sec

    # fig1, ax1 = plt.subplots()

    # create a Circle patch object with the given c_sec and radius
    enclosing_circle = Circle(c_sec, r_sec, alpha=0.2, edgecolor='r', fill=False)
    containing_circle = Circle(c_sec, r_con, alpha=0.2, edgecolor='r', fill=False)
    center_plot = Circle(c_sec, 0.02, alpha=1, edgecolor='r',fill=True)

    # add the circle to the axis object
    ax.add_patch(enclosing_circle)
    ax.add_patch(containing_circle)
    # ax.add_patch(center_plot)

    # print(c_sec)
    # print(r_sec)

    # plot the points on a scatter plot
    plt.scatter(points[:,0], points[:,1],color="blue")
    
    grid_x,grid_y = grid_points.grid_points(c_con,r_con)
    grids = np.column_stack((grid_x,grid_y))
    # print(grid_x)
    # print(grids)
    Rates = []

    for i in range(len(points)):
        Rates.append(random.uniform(1.5,2))

    pmax = optimal_position.optimalPosition(Users,Rates,0.01,grids,1)
    # print(pmax)
    plt.scatter([pmax[0]],[pmax[1]],color="green")

    pri_user = random.randint(1,len(Users))
    print(Users[pri_user-1])
    pri_pt = priority_user.optimalPos(grids,Users[pri_user-1]["coord"])
    print(pri_pt)
    plt.scatter([pri_pt[0],Users[pri_user-1]["coord"][0]],[pri_pt[1],Users[pri_user-1]["coord"][1]],color="red")

    # # create a figure and axis object
    # fig, ax = plt.subplots(1)

    # # create a Circle patch object with the given center and radius
    # circle = Circle(c_con, r_con, alpha=0.2, edgecolor='r', fill=False)

    # # add the circle to the axis object
    # ax.add_patch(circle)

    # # plot the grid of points inside the circle
    # plt.scatter(grid_x, grid_y)

    # # display the plot
    # f = plt.figure(2)
    # f.show()

 # create a figure and axis object
fig, ax = plt.subplots()
 # set the x and y limits of the axis to show the circle
ax.set_xlim(-30,55)
ax.set_ylim(-25,55)
mean = [0, 0]
cov = [[50, 10], [10, 50]]
compute_cluster(mean,cov,enclosing_circle,ax)
mean = [30, 30]
cov = [[50, 10], [10, 50]]
compute_cluster(mean,cov,enclosing_circle,ax)
plt.show()
input()