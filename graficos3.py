from matplotlib import pyplot

lenguajes=('python','c','java','go','javascript')
valores=(100,130,90,80,128)
colores=('red','blue','green','yellow','pink')
pyplot.rcParams['toolbar']='None'


pyplot.title("lenguajes")
pyplot.ylabel("productos")
pyplot.bar(lenguajes,height=valores, color=colores, width=0.5)
#pyplot.savefig("hola.png")
pyplot.show()









