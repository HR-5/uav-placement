import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def grid_points(center,radius):
    # define the horizontal and vertical spacing between the grid points
    dx = 3
    dy = 3

    # calculate the range of x and y values to generate the grid
    x_range = np.arange(center[0]-radius, center[0]+radius+dx, dx)
    y_range = np.arange(center[1]-radius, center[1]+radius+dy, dy)

    # create a meshgrid of x and y values
    x, y = np.meshgrid(x_range, y_range)

    # calculate the distance of each point from the center of the circle
    r = np.sqrt((x-center[0])**2 + (y-center[1])**2)

    # filter out the points outside the circle
    x = x[r<=radius]
    y = y[r<=radius]

    # create a figure and axis object
    # fig, ax = plt.subplots(1)

    # # create a Circle patch object with the given center and radius
    # circle = Circle(center, radius, alpha=0.2, edgecolor='r', fill=False)

    # # add the circle to the axis object
    # ax.add_patch(circle)

    # # plot the grid of points inside the circle
    # plt.scatter(x, y)

    # # display the plot
    # f = plt.figure(2)
    # f.show()
    return x,y
