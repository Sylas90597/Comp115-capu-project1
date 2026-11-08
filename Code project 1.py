import turtle
import random

wn=turtle.Screen()
dave=turtle.Turtle()
dave.hideturtle()

wn.bgcolor('#101B4D')
dave.speed(0)

color1 = 'black'
color2 = '#050A20'  #if need lighter use '#060C23'
color3 = 'green'
color4 = 'blue'
colora = '#D4A351'
colorb = '#4A3B16'
q = -60
w = color1
e = color2
t = color3
y = color4
u = colora
o = colorb
a = 'red'
s = 'orange'

dave.up()           #start of baseline
dave.goto(-200,-40)
dave.down()
dave.begin_fill()
dave.forward(400)
dave.right(90)
dave.forward(20)
dave.right(90)
dave.forward(400)
dave.end_fill()    #end of baseline

dave.color('#080F2E')   #start of water
dave.begin_fill()
dave.left(90)
dave.forward(150)
dave.left(90)
dave.forward(400)
dave.left(90)
dave.forward(150)
dave.end_fill()         #end of water

for i in range(40):                 #start of stars
    x = random.randint(-200,200)
    y = random.randint(-39,200)
    dave.color('white')
    dave.up()
    dave.goto(x,y)
    dave.dot(2)
    dave.color('#52658F')
    dave.goto(x,-y)
    dave.dot(2)                     #end of stars

building_heights = []
total_height = []
    
    
def building(x,y,color1,color2,height,width):
    building_heights.append(height)
    dave.up()
    dave.goto(x,y)
    dave.color(color1)
    dave.down()
    dave.seth(90)
    dave.begin_fill()
    dave.forward(height)
    dave.right(90)
    dave.forward(width)
    dave.right(90)
    dave.forward(height)
    dave.end_fill()
    dave.color(color2)
    dave.begin_fill()
    dave.forward(height)
    dave.right(90)
    dave.forward(width)
    dave.right(90)
    dave.forward(height)
    dave.end_fill()


building(-190,-60,color1,color2,50,15)     #start of main buildings
building(-160,-60,color1,color2,70,25)
building(-130,-60,color1,color2,65,20)
building(-102,-60,color1,color2,40,20)
building(-85,q,w,e,92,18)
building(-60,q,w,e,80,25)
building(-31,q,w,e,120,22)
building(-5,q,w,e,100,12)
building(5,q,w,e,90,12)
building(24,q,w,e,135,15)
building(40,q,w,e,85,20)
building(65,q,w,e,95,22)
building(90,q,w,e,115,12)
building(108,q,w,e,70,15)
building(127,q,w,e,55,20)
building(151,q,w,e,80,18)
building(170,q,w,e,36,16)                 #end of main buildings 

building(-200,q,w,e,30,20)                #start of lower buildings
building(-175,q,w,e,40,10)
building(-165,q,w,e,30,10)
building(-150,q,w,e,35,20)
building(-125,q,w,e,30,30)
building(-95,q,w,e,60,20)
building(-80,q,w,e,40,20)
building(-50,q,w,e,50,20)
building(-20,q,w,e,70,20)
building(15,q,w,e,55,20)
building(30,q,w,e,45,40)
building(70,q,w,e,60,20)
building(90,q,w,e,40,45)
building(160,q,w,e,25,20)                #end of lower buildings


for height in building_heights:
    total_height.append(height * 2) 

print(building_heights)
print(total_height)

def roof(x,y,color1,color2,height,width,number):
    dave.up()
    dave.goto(x,y)
    dave.color(color1)
    dave.down()
    dave.seth(90)
    dave.begin_fill()
    dave.forward(height)
    dave.right(90)
    dave.forward(width)
    dave.right(90)
    dave.forward(height)
    dave.end_fill()
    dave.up()
    dave.color(color2)
    dave.seth(270)
    dave.forward(total_height[number])
    dave.begin_fill()
    dave.forward(height)
    dave.right(90)
    dave.forward(width)
    dave.right(90)
    dave.forward(height)
    dave.end_fill()

roof(-155,-10,w,e,25,15,0)         #start of square roofs
roof(-115,-9,w,e,20,5,0)
roof(-85,31,w,e,5,10,4)
roof(-57.5,20,w,e,10,20,1)
roof(-53.5,27,w,e,10,12,1)
roof(30,75,w,e,5,9,1)
roof(45,20,w,e,30,15,1)
roof(67.5,30,w,e,10,17,1)          
roof(115,10,w,e,10,8,1)
roof(154,15,w,e,10,12,0)
roof(175,-25,w,e,10,7,0)           #end of square roofs



def troof(color1,x,y,angle1,side1,angle2,side2):
    dave.up()
    dave.goto(x,y)
    dave.down()
    dave.color(color1)
    dave.begin_fill()
    dave.seth(90)
    dave.right(angle1)
    dave.forward(side1)
    dave.right(angle2)
    dave.forward(side2)
    dave.end_fill()
    dave.up()


troof(w,34,80,1,60,179,60)          #start of troofs
troof(w,-30,60,60,20,120,10)
troof(w,-49.5,35,4,30,172,30)
troof(w,100,55,1,15,179,15)
troof(w,93,55,1,10,179,10)
troof(w,138,-5,60,10,120,5)
troof(w,128,-5,60,10,120,5)
troof(w,-177,-9,270,13,90,6)        #end of troofs


def light(x,y,colora,colorb,height,width,distance):
    dave.up()
    dave.goto(x,y)
    dave.color(colora)
    dave.down()
    dave.seth(90)
    dave.begin_fill()
    dave.forward(height)
    dave.right(90)
    dave.forward(width)
    dave.right(90)
    dave.forward(height)
    dave.end_fill()
    dave.up()
    dave.forward(distance)
    dave.color(colorb)
    dave.down()
    dave.begin_fill()
    dave.forward(height)
    dave.right(90)
    dave.forward(width)
    dave.right(90)
    dave.forward(height)
    dave.end_fill()   


light(-185,-20,u,o,3,4,80)

light(-155,0,u,o,2,1,80)             #start of lights
light(-150,-10,u,o,2,1,80)
light(-145,0,u,o,2,1,80)             
light(-155,-20,u,o,2,1,80)
light(-155,-30,u,o,2,1,80)             
light(-145,-20,u,o,2,1,80)
light(-150,-30,u,o,2,1,80)

light(-117,-12,u,o,3,2,110)
light(-117,-19,u,o,3,2,110)
light(-117,-5,u,o,3,2,110)

light(-80,20,u,o,1,1,155)
light(-75,20,u,o,1,1,155)
light(-80,10,u,o,1,1,155)
light(-75,-10,u,o,1,1,155)

light(-49,15,u,o,1,3,120)
light(-54,15,u,o,1,1,120)
light(-41,15,u,o,1,1,120)
light(-49,0,u,o,1,3,120)
light(-54,0,u,o,1,1,120)
light(-41,0,u,o,1,1,120)
light(-49,-15,u,o,1,3,120)
light(-54,-15,u,o,1,1,120)
light(-41,-15,u,o,1,1,120)


light(-29,50,u,o,1,4,150)
light(-20,50,u,o,1,1,150)
light(-29,40,u,o,1,4,150)
light(-20,40,u,o,1,1,150)
light(-29,30,u,o,1,4,150)
light(-20,30,u,o,1,1,150)
light(-29,20,u,o,1,4,150)
light(-20,20,u,o,1,1,150)
light(-29,10,u,o,1,4,150)
light(-20,10,u,o,1,1,150)
light(-29,0,u,o,1,4,150)
light(-20,0,u,o,1,1,150)
light(-29,-10,u,o,1,4,150)
light(-20,-10,u,o,1,1,150)


light(132,-15,u,o,3,3,80)
light(140,-15,u,o,3,3,80)
light(132,-20,u,o,3,3,80)
light(140,-20,u,o,3,3,80)

light(70,20,u,o,4,1,120)
light(75,10,u,o,4,1,120)
light(70,10,u,o,4,1,120)
light(80,10,u,o,4,1,120)
light(75,0,u,o,4,1,120)
light(80,-10,u,o,4,1,120)
light(75,-10,u,o,4,1,120)


light(98,40,u,o,8,1,130)
light(94,30,u,o,8,1,130)
light(98,20,u,o,8,1,130)
light(94,10,u,o,8,1,130)
light(94,0,u,o,8,1,130)
light(98,-10,u,o,8,1,130)
light(94,-20,u,o,8,1,130)
light(98,-20,u,o,8,1,130)

light(160,-10,u,o,2,1,100)
light(165,0,u,o,2,1,100)             
light(155,-20,u,o,2,1,100)
light(155,-30,u,o,2,1,100)             
light(165,-20,u,o,2,1,100)
light(160,-30,u,o,2,1,100)
light(160,10,u,o,2,1,100)
light(165,0,u,o,2,1,100)             
light(157.5,20,u,o,2,1,100)
light(155,10,u,o,2,1,100)             
light(162.5,20,u,o,2,1,100)
light(160,10,u,o,2,1,100)

light(114,0,u,o,3,5,90)
light(114,-15,u,o,3,5,90)
light(114,-30,u,o,3,5,90)


light(28,20,u,o,1,1,160)
light(33.5,20,u,o,1,1,160)
light(28,70,u,o,1,1,160)
light(33.5,70,u,o,1,1,160)
light(28,60,u,o,1,1,160)
light(33.5,60,u,o,1,1,160)
light(28,50,u,o,1,1,160)
light(33.5,50,u,o,1,1,160)
light(28,40,u,o,1,1,160)
light(33.5,40,u,o,1,1,160)
light(28,30,u,o,1,1,160)
light(33.5,30,u,o,1,1,160)
light(28,10,u,o,1,1,160)
light(33.5,10,u,o,1,1,160)
light(28,0,u,o,1,1,160)
light(33.5,0,u,o,1,1,160)
light(28,-10,u,o,1,1,160)
light(33.5,-10,u,o,1,1,160)

light(55,10,u,o,3,2,135)
light(55,18,u,o,3,2,135)
light(55,26,u,o,3,2,135)
light(48,34,u,o,3,2,135)
light(48,26,u,o,3,2,135)
light(48,2,u,o,3,2,135)

light(-2,20,u,o,3,2,135)
light(4,20,u,o,3,2,135)
light(10,20,u,o,3,2,135)
light(-2,5,u,o,3,2,135)
light(4,5,u,o,3,2,135)
light(10,5,u,o,3,2,135)
light(-2,-10,u,o,3,2,135)
light(4,-10,u,o,3,2,135)
light(10,-10,u,o,3,2,135)

