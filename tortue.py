import turtle
turtle.delay(0)
maTortue=turtle.Turtle()
maTortue.pencolor("pink")
maTortue2=turtle.Turtle()
maTortue2.pencolor("blue")
maTortue3=turtle.Turtle()
maTortue3.pencolor("green")
maTortue.speed(0)
import random

#carré
'''

maTortue.speed(1)
maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)
maTortue.left(90)
maTortue.forward(100)

input()
'''

#rond
''' 
import turtle

for i in range (0,360):
    maTortue.forward(1)
    maTortue.left(1)
    maTortue.speed(10)

input()
'''

#escargot carré
'''
distance=3
maTortue=turtle.Turtle()
for i in range(500):
    maTortue.forward(distance)
    maTortue.left(90)
    distance+=3

input()
'''

#escargot rond

'''

for i in range (0,4320):
    maTortue.forward(i/360)
    maTortue.left(1)
    maTortue.speed(0)

input()
'''

#3.a tortue qui marche en ligne droite
'''
while 1 :
    maTortue.forward(1)

input()

'''

#3.b fonction tourner aléatoire

'''

while True:
    var = random.randint(1,3)
    
    if var ==1:
        maTortue.left(90)
    elif var ==2:
        maTortue.right(90)
    else :
        pass
    maTortue.forward(10)
'''

#3.c ajouter plusieurs tortues

'''
def pommedeterre(violette,pissenlit,coquelicot):

    while True:
        pas(violette)
        pas(pissenlit)
        pas(coquelicot)


#pommedeterre(maTortue)
def pas(tortue):
    var = random.randint(0,2)
    if var ==1:
        tortue.left(90)
    elif var ==2:
        tortue.right(90)
    else :
        pass
    tortue.forward(10)

pommedeterre(maTortue2,maTortue,maTortue3)
'''

#4.a démarrer positions aléatoires 

def aubergine(muguet):

    positionx = random.randint(0,100)
    positiony= random.randint(0,100)

    muguet.penup()
    muguet.goto(positionx, positiony)
    muguet.pendown()


