# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.figure(figsize=(10, 6))
    # for i in range(rw.num_points):
    #     print ("[%d,%d]"%(rw.x_values[i],rw.y_values[i]))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none',s=10)
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
s=100)
    #plt.scatter(rw.x_values, rw.y_values, s=1)
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = raw_input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
