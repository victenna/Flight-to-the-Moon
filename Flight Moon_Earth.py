import turtle,time
import winsound
wn=turtle.Screen()
t=turtle.Turtle()
t.hideturtle()
t.up()
turtle.tracer(2)
wn.setup(900,900)

#Moon Sky
wn.bgpic('moon3.gif')
turtle.bgcolor('black')

#Astronaut1
image1=['ast11.gif','ast12.gif','ast11_m.gif','ast12_m.gif']
ast1=turtle.Turtle()
ast1.up()
ast1.goto(-250,-240)
wn.addshape('ast11.gif')
wn.addshape('ast12.gif')
wn.addshape('ast11_m.gif')
wn.addshape('ast12_m.gif')
ast1.shape('ast11.gif')

#______________________Atronaut2 is standing
ast2=turtle.Turtle()
ast2.up()
ast2.goto(390,-240)
wn.addshape('ast2.gif')
ast2.shape('ast2.gif')
#______________________________________

#____________Astronaut3 Comes out of the Shuttle
image3=['ast31.gif','ast32.gif','ast33.gif','ast34.gif','ast35.gif']
ast3=turtle.Turtle()
ast3.hideturtle()
for i in range (4):
    wn.addshape(image3[i])


s = turtle.Shape("compound")

#Space Shuttle
poly1=((0,0),(25,0),(25,10),(0,10))
poly2=((25,0),(35,5),(25,10))
poly3=((0,10),(-5,19),(10,10))
poly4=((0,0),(-5,-10),(10,0))
#poly5=((5,2),(15,2),(15,5),(5,5))
poly5=((5,7),(15,7),(15,10),(5,10))
poly6=((0,3),(-10,-4),(-10,14),(0,8))

s.addcomponent(poly1,'red','black')
s.addcomponent(poly2,'pink','black')
s.addcomponent(poly3,'green','black')
s.addcomponent(poly4,'green','black')
s.addcomponent(poly5,'blue','black')

wn.addshape('roket',s)

Roket=turtle.Turtle(shape='roket')
Roket.penup()
Roket.hideturtle()
Roket.tilt(90)

Roket.setheading(90)
Roket.hideturtle()


s.addcomponent(poly6,'yellow','black')

wn.addshape('roket1',s)
Roket1=turtle.Turtle(shape='roket1')
Roket1.hideturtle()
Roket1.up()
Roket1.shapesize(0.1)
Roket1.tilt(90)
Roket1.hideturtle()
Roket1.goto(400,400)
Roket1.setheading(230)
Roket1.showturtle()
a1=2/100
a2=4/100
length=0.5

#Roket arrives to the Moon
winsound.PlaySound('to_moon.wav', winsound.SND_ASYNC)


for m in range(160):
    Roket1.fd(2)
    Roket1.shapesize(length)

    length=length+0.03
    time.sleep(0.01)
time.sleep(0.1)
print('length=',length)

Roket1.rt(139)

for i in range(82):
    Roket1.fd(-4.5)
    time.sleep(0.1)#  0.01??????????????
time.sleep(0.5)
Roket1.fd(-65)
X,Y=Roket1.position()

#Roket.hideturtle()
Roket.goto(X,Y)
Roket.showturtle()
Roket1.hideturtle()
Roket.shapesize(5)

#_____Astronaut1 moves to the Shuttle
for m in range(21):
    for n in range(2):
        ast1.shape(image1[0])
        ast1.fd(5)
        time.sleep(0.2)
        ast1.shape(image1[1])
        ast1.fd(5)
        time.sleep(0.2)
ast1.hideturtle()
X1,Y1=ast1.position()
#_______________________________

#Astronaut2 comes out!!!!!!!!!!!!!!!!!!!!!!!!!!!!
delta=5
ast3.hideturtle()
ast3.up()
ast3.goto(X1,Y1)
ast3.showturtle()
for m in range(50):
    m1=m%4
    wn.addshape(image3[m1])
    ast3.shape(image3[m1])
    ast3.goto(X1,Y1)
    X1=ast3.xcor()
    X1=X1-delta
    time.sleep(0.2)
wn.addshape(image3[4])
ast3.shape('ast35.gif')
ast3.showturtle()
time.sleep(1)

winsound.PlaySound('come.wav', winsound.SND_ASYNC)

# Shuttle starts from the moon
length=5
Roket.shapesize(0.01)
for i in range(130):
    Roket1.showturtle()
    Roket1.rt(0.35)
    Roket1.shapesize(length)
    length=length-0.04
    time.sleep(0.01)
   
    Roket1.fd(5)
time.sleep(0.2)

     
wn.setup(900,900)
Roket1.hideturtle()
Roket1.shapesize(2)

#________________Shuttle in free space
ast1.hideturtle()
ast2.hideturtle()
ast3.hideturtle()
sky=['sk1.gif','sk2.gif']
winsound.PlaySound('kosmos.wav', winsound.SND_ASYNC)
for m in range(2):
    Roket1.goto(-400,-400)
    Roket1.setheading(45)
    Roket1.showturtle()
    k=0
    for i in range(430):
        k=k+1
        k1=k%15
        if k1==0:
            wn.bgpic(sky[0])
        if k1==7:
            wn.bgpic(sky[1])
         
         
        Roket1.fd(3)
        time.sleep(0.01)
turtle.tracer(1)      
# Shuttle arrives to the Earth   
wn.bgpic('Spaceport2.gif') #   Earth Image  


winsound.PlaySound('to_earth.wav', winsound.SND_ASYNC)

#____________________________Guest3 and Guest4 meet the roket
imageg3=['guest11.gif','guest12.gif']#,'guest13.gif']
imageg4=['guest21.gif','guest22.gif']#,'guest23.gif','guest24.gif','guest25.gif']
guest3=turtle.Turtle()
guest3.hideturtle()
guest3.up()
guest3.goto(350,-350)

guest4=turtle.Turtle()
guest4.hideturtle()
guest4.up()
guest4.goto(-200,-120)

for i in range(2):
    wn.addshape(imageg3[i])

for i in range(2):
    wn.addshape(imageg4[i])

guest3.shape(imageg3[0])
guest4.shape(imageg4[0])

Roket1.hideturtle()
Roket1.goto(400,400)
Roket1.setheading(-135)
a1=2/100
a2=4/100
length=0.3
Roket1.shapesize(length)
Roket1.showturtle()

guest3.showturtle()
guest4.showturtle()
#_____________________________

#_________________________Roket arrives to the Earth
for m in range(180):
    Roket1.fd(2)
    Roket1.shapesize(length)

    length=length+0.025
    time.sleep(0.01)

Roket1.setheading(90)

for i in range(95):
    Roket1.fd(-4.5)
    time.sleep(0.02)
   
X,Y=Roket1.position()
time.sleep(0.5)

Roket.goto(X,Y)
Roket.showturtle()
Roket1.hideturtle()
Roket.shapesize(5)
#________________________________________________

ast1.goto(100,-240)
ast1.showturtle()

winsound.PlaySound('clap.wav', winsound.SND_ASYNC)
#turtle.tracer(2)
for i in range(70):
    i1=i%2
    #i2=i%5

    if i<10:
        for n in range(4):
            n1=n%2
            ast1.shape(image1[2])
            ast1.fd(-5)
            time.sleep(0.04)
            ast1.shape(image1[3])
            ast1.fd(-5)
            time.sleep(0.04)
            guest3.shape(imageg3[n1])
            guest4.shape(imageg4[n1])
    if i>=10:  
        guest3.shape(imageg3[i1])
        guest4.shape(imageg4[i1])
        time.sleep(0.08)
        ast1.shape(image1[0])







