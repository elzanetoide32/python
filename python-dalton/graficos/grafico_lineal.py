import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df=pd.read_csv("graficos\\pedos.csv")
#creando el grafico
sns.lineplot(x="fecha",y="pedo",data=df)
#poniendo el puntito en el maximo
plt.plot("01/09",17,"o")
#mostrando el grafico
plt.show()











