import turtle
import random
turtle.delay(0)
'''maTortue=turtle.Turtle()
maTortue.pencolor("pink")
maTortue2=turtle.Turtle()
maTortue2.pencolor("blue")
maTortue3=turtle.Turtle()
maTortue3.pencolor("green")
maTortue.speed(0)'''


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

listeofT=[]
turtle.shapesize(3)
turtle.shape("turtle")
turtle.color("red")
def frangipanier(n):
    liste=[]
    for i in range(n):
        liste.append(turtle.Turtle())
    return liste

def aubergine(liste):
    for i in liste:

        i.penup()
        i.goto(random.randint(-400,400), random.randint(-400,400))
        i.pendown()
        i.color(random.random(),random.random(),random.random())
        i.shapesize(random.randint(1,8))

def pas(tortue):
    var = random.randint(0,2)
    if var ==1:
        tortue.left(90)
    elif var ==2:
        tortue.right(90)
    else :
        pass
    tortue.forward(10)

def pommedeterre(liste):
    for i in liste:
        pas(i)

def changeUp():
    turtle.setheading(90)
def changeRight():
    turtle.setheading(0)
def changeLeft():
    turtle.setheading(180)
def changeDown():
    turtle.setheading(270)

turtle.onkeypress(changeUp,"Up")
turtle.onkeypress(changeRight,"Right")
turtle.onkeypress(changeDown,"Down")
turtle.onkeypress(changeLeft,"Left")
turtle.listen()

listeofT=(frangipanier(9))
aubergine(listeofT)
aubergine(listeofT)



while 1:
    turtle.forward(10)
    pommedeterre(listeofT)
