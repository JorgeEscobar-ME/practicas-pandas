import pandas as pd
import numpy as np
df_books=pd.read_csv('/home/jorge/numppd/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv',sep=',', header=0)
print(df_books)
#El metodo .groupby() agrupa los datos con respecto a las columnas que se escriban como lista
#El metodo .agg() permite anyadir columnas a esa tabla con la info que se necesite como un diccionario
autores=df_books.groupby(["Author","Year"]).agg({'Reviews':['min','max'], 'User Rating': 'mean'})
print(autores)
arr = np.array([13, 6, 3, 5, 10])
print(np.argmax(arr))