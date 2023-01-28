import pandas as pd
granada={
'Jugador':['Luis SuÃ¡rez','Jorge Molina', 'Antonio Puertas', 'GermÃ¡n SÃ¡nchez', 'Luis Milla', 'LuÃ­s Manuel Arantes Maximiano'],

'Posicion':['Delantero', 'Delantero', 'Centrocampista', 'Defensa', 'Centrocampista', 'Portero'],


'Altura':[185.0, 187.0, 185.0, 187.0, 175.0, 190.0],

'Goles':[7, 7, 5, 2, 2, 0]}

granada_df=pd.DataFrame(granada,[9, 23, 10, 6, 5, 1])
print(granada_df)