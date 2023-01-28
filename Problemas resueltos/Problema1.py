#Escribir un programa que pregunte al usuario por las ventas de un rango de años
#  y muestre por pantalla una serie con los datos de las ventas indexada por los años, 
# antes y después de aplicarles un descuento del 10%.
import pandas as pd

cantidad_datos=int(input("Ingrese la cantidad de datos"))
arr_ventas=[]
arr_years=[]
for i in range (cantidad_datos):
    arr_years.append(input('Ingrese el anyo: '))
    arr_ventas.append(input('Ingrese las ventas totales de ese anyo: '))
    
sales=pd.Series(arr_ventas,index=arr_years,dtype='float64')
sales10=sales[:]*0.9

print("Estas son las ventas: \n",sales)
print(sales10)