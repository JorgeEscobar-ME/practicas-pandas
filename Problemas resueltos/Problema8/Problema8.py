import pandas as pd
#Generar un DataFrame con los datos de los cuatro ficheros.
e16=pd.read_csv("/home/jorge/numppd/Problemas resueltos/Problema8/emisiones-2016.csv", sep=";")
e17=pd.read_csv("/home/jorge/numppd/Problemas resueltos/Problema8/emisiones-2017.csv", sep=";")
e18=pd.read_csv("/home/jorge/numppd/Problemas resueltos/Problema8/emisiones-2018.csv", sep=";")
e19=pd.read_csv("/home/jorge/numppd/Problemas resueltos/Problema8/emisiones-2019.csv", sep=";")
data=pd.concat([e16,e17,e18,e19])
print(data)
#Filtrar las columnas del DataFrame para quedarse con las columnas 
# ESTACION, MAGNITUD, AÑO, MES y las correspondientes a los días D01, D02, etc.
columnas = ['ESTACION', 'MAGNITUD', 'ANO', 'MES']
columnas.extend([columna for columna in data if columna.startswith("D")])
data=data[columnas]
print(data)
#Reestructurar el DataFrame para que los valores de los contaminantes
#  de las columnas de los días aparezcan en una única columna.
