import numpy as np
x=np.random.randint(1,10,(3,2))
y=np.random.randint(10,20,(3,2))
z=np.random.randint(20,30,(3,2))
ten=np.array([[x],[y],[z]])
ten_reshape=ten.reshape(1,18)
print(ten_reshape)
