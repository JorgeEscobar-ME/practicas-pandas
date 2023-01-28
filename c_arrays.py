import numpy as np
#arange crea un vector de la longitud y steps que uno desee
x=np.arange(0,10)
ceros=np.zeros((10,10))
print(ceros)
unos=np.ones((10,10))
print(unos)
#usando linspace
espaciado=np.linspace(0,10,10)
print(espaciado)
#Matriz identidad
identidad=np.eye(5)
print(identidad)
#ALeatorios y aleatorios enteros
aleatorios=np.random.rand(3,3)
print(aleatorios)
aleatorios_enteros=np.random.randint(1,5,(5,4))
print(aleatorios_enteros)