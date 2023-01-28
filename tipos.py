import numpy as np
#'f8' es el tipo de dato del array. se usa f8 para flout e i4 para int
arr=np.array([1,2,3,4],dtype='f8')
print(arr.dtype)
ten=np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]], [[13,14,15],[16,17,18]], [[19,20,21],[22,23,24]],[[25,26,27],[28,29,30]]])
#expand aumenta una dimension en el eje que se elija
tenex=np.expand_dims(ten, axis=1)
print(ten.ndim)
#np.squeeze reduce las dimensiones de eje 0
tenc=np.squeeze(tenex)
