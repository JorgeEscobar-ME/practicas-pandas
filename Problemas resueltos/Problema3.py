#Escribir una función que reciba un diccionario con las notas de los alumnos de un curso 
# y devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.
import pandas as pd

notas = {'Juan':9, 'María':10.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}

def orden(notas):
    serie_notas=pd.Series(notas)
    notas_ordenadas=serie_notas.sort_values(ascending=False)
    return notas_ordenadas

ordenadas=orden(notas)
print(ordenadas)