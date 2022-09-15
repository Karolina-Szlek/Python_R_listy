from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random



# W każdym kroku wyróżniona jest jedna komórka nazywana "mrówką", 
# która oprócz koloru ma określony także kierunek, w którym się porusza. 
# Mrówka zachowuje się według następujących zasad:

#     jeśli znajduje się na polu białym to obraca się w lewo (o kąt prosty), zmienia kolor pola na czarny i przechodzi na następną komórkę;
#     jeśli znajduje się na polu czarnym to obraca się w prawo (o kąt prosty), zmienia kolor pola na biały i przechodzi na następną komórkę;
#     porusza się na nieskończonej planszy podzielonej na kwadratowe komórki (pola) w dwóch możliwych kolorach: czarnym i białym.



fig = plt.figure(figsize = (6, 6))#okienko
ax = plt.axes(xlim = (0,100), ylim = (0, 100))#oś OX iOY

Table = np.zeros((101,101, 3), 'u1')#plansza
Table[:,:] = [255, 16, 143]#[0,0,0]#[42,122,88]
tb = plt.imshow(Table, interpolation='nearest')#displays an image without trying to interpolate between pixels 


#białe i czarne pola
white = [88, 52, 184]#[255, 16, 143]#[255,128,16]
black = [0, 0, 0]


#miejsce startu
X = random.randint(1,100)
Y = random.randint(1,100)
A = 0   # set direction: 0-up, 1-right, 2-down, 3-left (looking at the screen)



def init():
    tb.set_data(Table)
    return tb,


#zasady mrówki
def change():
    global X,Y,A, Table
    c = Table[X,Y]#zaczynamy
   # if all(Table[X,Y] == white) :
    if (c[0] == white[0]) and (c[1] == white[1]) and (c[2] == white[2]) :#jeśli pole jest białe 
        Table[X,Y] = black#zrób na czarne
        if A == 0: # w którą sronę w zależności jakie A podane
            X -= 1
        elif A == 1:
            Y += 1
        elif A == 2:
            X += 1
        else:
            Y -=1
        A = (A - 1) % 4# zmień A na kolejne, żeby zawsze w lewo iść
    else :#pole jest czarne
        Table[X,Y] = white#zmień na białe i idę w przeciwną stronę niż na białym( czyli w prawo)
        if A == 0:
            X += 1 
        elif A == 1:
            Y -= 1
        elif A == 2:
            X -= 1
        else:
            Y += 1
        A = (A + 1) % 4
        
    X = X % 100#jakby wyszpo poza
    Y = Y % 100
    return Table



# z wykładu
def animate(i):
    #print (X,Y,A)
    tablt = change()
    tb = plt.imshow(tablt, interpolation='nearest')
    return tb,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=800, interval=4, blit=True)


plt.show()