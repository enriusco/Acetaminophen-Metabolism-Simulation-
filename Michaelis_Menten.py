import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

df = pd.read_csv('example.csv', sep=',', header=0)
df = df.drop(["time","gAPAP","pAPAP","tAPAP"], axis = 1)
df1 = df.iloc[:4000:10]
df2 = df.iloc[4000::1000]
df3 = pd.merge(df1,df2,how='outer')
df3.sort_values(by=['lAPAP'], inplace = True)

lista = []
for irex, frow in df3.iterrows():
    riga  = frow.tolist()
    lAPAP = riga[0]
    V_CYP = (0.99*lAPAP)/(276+lAPAP)
    lista.append([lAPAP, V_CYP])

fig = plt.figure()
l, = plt.plot([], [], 'm--')
p1, = plt.plot([], [], 'm')

plt.hlines(y=0.99, xmin=0, xmax=9000, colors="black")

plt.xlabel('[lAPAP]')
plt.ylabel('velocità')

plt.xlim(0, 7000)
plt.ylim(0, 1.1,)

xlist = []
ylist = []

metadata = dict(title='Movie', artist='codinglikemad')
writer = PillowWriter(fps=15, metadata=metadata)

i=0
with writer.saving(fig, "V_CYP.gif", 100):
    while i < len(lista)-1:
        xlist.append(lista[i][0]) #lAPAP
        ylist.append(lista[i][1]) #V_CYP
        l.set_data(xlist,ylist)
        p1.set_data(lista[i][0],lista[i][1])
        writer.grab_frame()
        i+=1
