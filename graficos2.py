from matplotlib import pyplot

lenguajes=('python','c','java','go','javascript')
slices=(100,130,90,80,128)
colores=('red','blue','green','yellow','pink')
valores=(0.1,0,0,0,0)
pyplot.rcParams['toolbar']='None'
_, _, texto= pyplot.pie(slices, colors=colores, labels=lenguajes, autopct='%1.1f%%', explode=valores, startangle=90)

for tex in texto:
    tex.set_color('white')

pyplot.axis('equal')
pyplot.title('graficos de lenguajes de programacion')
#pyplot.legend(labels=lenguajes)
pyplot.show()
#pyplot.savefig('lenguajes.png')
