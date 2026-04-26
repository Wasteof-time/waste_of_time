import math
import matplotlib.pyplot as mp

x_axis = list(range(1000))
y_sin = [math.sin(x) for x in range(1000)]
y_cos = [math.cos(x) for x in range(1000)]


mp.plot(x_axis,y_sin,label = "sinwave")
mp.plot(x_axis,y_cos , label = "coswave")
mp.show()







