# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
squares = [i*i for i in range(1,6)]
input_value = [i for i in range(1,6)]
plt.plot(input_value, squares, linewidth=2)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()
