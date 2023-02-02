import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df=pd.read_csv("graficos\\dispersion.csv")
#creando el grafico
sns.scatterplot(x="tiempo", y="dinero",data=df)

#mostrando el grafico
plt.show()




