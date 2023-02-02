import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df=pd.read_csv("graficos\\bigotes.csv")
#creando el grafico
sns.boxplot(x="categoria",y="valor",data=df)

#mostrando el grafico
plt.show()
