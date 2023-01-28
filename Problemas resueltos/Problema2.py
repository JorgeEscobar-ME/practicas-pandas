#Escribir una función que reciba un diccionario con las notas de los alumno de un 
# curso y devuelva una serie con la nota mínima, la máxima, media y la desviación típica.
import pandas as pd
#from pandas import ExcelWriter
import numpy as np
notas = {'Juan':9, 'María':10.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

def infor(directorio):
    serie_datos=pd.Series(notas[key]for key in directorio.keys())
    respuesta=pd.Series([np.min(serie_datos), np.max(serie_datos), np.mean(serie_datos), np.std(serie_datos)], index=["Minimo", "Maximo", "Media", "Desviacion estandar"])
    return respuesta

prueba=infor(notas)
print(prueba)

# writer = ExcelWriter('ejemplo.xlsx')
# info.to_excel(writer, 'Hoja de datos', index=False)
# writer.save()