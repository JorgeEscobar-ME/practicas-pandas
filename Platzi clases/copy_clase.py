import numpy as np
x=np.arange(1,10)
piece=x[2:6]
piece[:]=0
print(x)
x_copy=x.copy()
x_copy[:]=100
print(x,x_copy)