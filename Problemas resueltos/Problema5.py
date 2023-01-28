#Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
#  una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.
import pandas as pd
reporte=pd.DataFrame(list(zip(["Enero","Febrero", "Marzo", "Abril"],[30500, 35600, 28300, 33900],[22000, 23400, 18100, 20700])),columns=["Mes", "Ventas", "Gastos"])
def gen_balance(reporte):
    balance=[]
    for i in range (len(reporte)):
        balance.append(reporte.iloc[i,1]-reporte.iloc[i,2])
    reporte_final=pd.concat([reporte, pd.Series(balance,name="Balance")], axis=1)
    return reporte_final
final=gen_balance(reporte)
print(final)