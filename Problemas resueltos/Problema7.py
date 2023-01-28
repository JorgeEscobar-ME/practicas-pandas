# El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

# Generar un DataFrame con los datos del fichero.
# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
# Mostrar por pantalla los datos del pasajero con identificador 148.
# Mostrar por pantalla las filas pares del DataFrame.
# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
# Eliminar del DataFrame los pasajeros con edad desconocida.
# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.


import pandas as pd

## Generar un DataFrame con los datos del fichero.
titanic=pd.read_csv("/home/jorge/numppd/Problemas resueltos/titanic.csv")

# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
print("Las dimensiones del dataFrame son ", titanic.shape, "\n contiene ", titanic.size, "elementos \n", "Las columnas son: ", titanic.columns,"las filas son: ", titanic.index, "Los tipos de datos son: ", titanic.dtypes)
print("Las diez primeras filas: ")
print(titanic.head(10))
print("Las dies ultimas filas: ")
print(titanic.tail(10))

# Mostrar por pantalla los datos del pasajero con identificador 148.
print(titanic.iloc[147])

# Mostrar por pantalla las filas pares del DataFrame.
print(titanic.iloc[range(0,titanic.shape[0],2)])

# Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
primeraclase=[]
for i in range(len(titanic)):
    if titanic.loc[i,'Pclass']==1:
        primeraclase.append(titanic.iloc[i,3])
print(sorted(primeraclase))
# Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
print("Porcentaje de personas que sobrevivieron: ",round(len(titanic[titanic["Survived"]==1])*100/len(titanic), 2))
print("Porcentaje de personas que murieron: ", round(100-len(titanic[titanic["Survived"]==1])*100/len(titanic),2))

# Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
conjunto=list(set(titanic[titanic["Survived"]==1]["Pclass"]))
print("Clases diferentes:", conjunto)
primera_clase=(titanic[titanic["Survived"]==1]["Pclass"]==1).sum()
segunda_clase=titanic[titanic["Survived"]==1]["Pclass"]==2
tercera_clase=titanic[titanic["Survived"]==1]["Pclass"]==3
conteo_1=primera_clase.sum()
conteo_2=segunda_clase.sum()
conteo_3=tercera_clase.sum()
#Con indexado como un animal:
print("El porcentaje de personas que sobrevivieron en primera clase es: ", round((titanic[titanic["Survived"]==1]["Pclass"]==1).sum()*100/(titanic.loc[:,"Pclass"]==1).sum(),2))
print("El porcentaje de personas que sobrevivieron en segunda clase es: ", round((titanic[titanic["Survived"]==1]["Pclass"]==2).sum()*100/(titanic.loc[:,"Pclass"]==2).sum(),2))
print("El porcentaje de personas que sobrevivieron en tercera clase es: ", round((titanic[titanic["Survived"]==1]["Pclass"]==3).sum()*100/(titanic.loc[:,"Pclass"]==3).sum(),2))
#Con groupby como un caballero:
print(titanic.groupby("Pclass")["Survived"].value_counts(normalize=True))

# Eliminar del DataFrame los pasajeros con edad desconocida.
titanic=titanic.dropna(subset="Age")

# Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
print("Edad media de las mujeres que viajaban en cada clase")
print(round(titanic.groupby(["Pclass", "Sex"])["Age"].mean().unstack()["female"],2))

# Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
titanic["Mayor_de_edad"] = titanic["Age"] >= 18
print(titanic)

# Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.
print(titanic.groupby(["Pclass", "Survived"])["Mayor_de_edad"].value_counts(normalize=True))
#Usando query:
titanic_sobrevivientes = titanic.query("Survived == 1")
print(titanic_sobrevivientes.groupby(["Pclass", "Survived"])["Mayor_de_edad"].mean())