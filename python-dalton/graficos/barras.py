import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df= pd.read_csv("graficos\\ingresos_cofla.csv")
#creando el grafico
sns.barplot(x="fuente", y="ingreso" ,data=df)

#total de ingresos
total=df['ingreso'].sum()
print(f"el total es: {total}")

#mostrando el grafico
plt.show()



