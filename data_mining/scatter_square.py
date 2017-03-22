# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
# #散点图
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=20)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# plt.tick_params(axis='both', which='major', labelsize=14)

#自动计算
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=1)
plt.axis([0, 1100, 0, 1100000])
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
