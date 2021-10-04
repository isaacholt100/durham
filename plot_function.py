from math import pi, sin
from matplotlib import pyplot as plt

# The next five lines are the part of the program which does the real
# work. But don't try to understand them for now.
def plot_function(f, startx, endx, nx):
    deltax = (endx-startx)/(nx-1)
    xlst = [startx + i*deltax for i in range(nx)]
    ylst = [f(x) for x in xlst]
    plt.plot(xlst, ylst, '-+r')
    plt.show()

# The next three lines define the Python version of the mathematical
# function for which the plot will be drawn
def my_fun(x):
    y = sin(x)
    return y

# The next line actually causes the plot to be drawn
plot_function(my_fun, 0, 4*pi, 80)

