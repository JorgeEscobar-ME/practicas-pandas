import numpy as np
x=np.random.randint(1,200, 30)
print(x)
#np.where permite hacer condiciones y ejecutar un valor si si o un valor si no
q=np.where((x<10) | (x>190), 30,x)
print(q)

