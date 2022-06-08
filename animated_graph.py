import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

def caricafile(fname):
    apri = open(fname,'r')
    leggi = apri.readlines()[1:]
    lista = []
    for line in leggi:
        line  = line.strip('\r\n').split(',')
        time  = float(line[0])
        lAPAP = float(line[1])
        gAPAP = float(line[2])
        pAPAP = float(line[3])
        tAPAP = float(line[4])

        lista.append([time,lAPAP,gAPAP,pAPAP,tAPAP])

    return lista

liste = caricafile('concentrations.csv')
liste = liste[1:10000:50]

fig = plt.figure()
l, = plt.plot([], [], 'b-')
l2, = plt.plot([], [], 'orange')
l3, = plt.plot([], [], 'g-')
l4, = plt.plot([], [], 'r-')
p1, = plt.plot([], [], 'k')
p2, = plt.plot([], [], 'm')
p3, = plt.plot([], [], 'm')
p4, = plt.plot([], [], 'm')

plt.xlabel('tempo (h)')
plt.ylabel('concentrazione(mg)')
plt.title('Concentrazione di paracetamolo')
plt.legend(["lAPAP", "gAPAP", "pAPAP", "tAPAP"])
plt.xlim(0, 5)
plt.ylim(0, 1200)

xlist = []
xlist2 = []
xlist3 = []
xlist4 = []
ylist = []
ylist2 = []
ylist3 = []
ylist4 = []

metadata = dict(title='Movie', artist='codinglikemad')
writer = PillowWriter(fps=15, metadata=metadata)

i=0
with writer.saving(fig, "APAP.gif", 100):
    while i < len(liste)-1:

        xlist.append(liste[i][0]) #time
        xlist2.append(liste[i][0]) #time
        xlist3.append(liste[i][0]) #time
        xlist4.append(liste[i][0]) #time
        ylist.append(liste[i][1]) #lAPAP
        ylist2.append(liste[i][2]) #gAPAP
        ylist3.append(liste[i][3]) #pAPAP
        ylist4.append(liste[i][4]) #tAPAP
        l.set_data(xlist,ylist)
        l2.set_data(xlist2,ylist2)
        l3.set_data(xlist3,ylist3)
        l4.set_data(xlist4,ylist4)
        p1.set_data(liste[i][0],liste[i][1])
        p2.set_data(liste[i][0],liste[i][2])
        p3.set_data(liste[i][0],liste[i][3])
        p4.set_data(liste[i][0],liste[i][4])

        writer.grab_frame()
        i+=1
