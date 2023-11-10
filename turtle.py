import args
import math

def square(t:turtle, tam:float):
    for i in range(2):
        t.fd(tam)
        t.lt(90)
        t.fd(tam)
        t.lt(90)

def polygon(t:turtle, tam:float, n:int):
    angulo = 360 / n
    for i in range(n):
        t.fd(tam)
        t.lt(angulo)

def circle(t:turtle, raio:int):
    t.rt(90)
    t.fd(raio/math.pi)
    polygon(t, raio, 12)

bob = turtle.Turtle()

circle(bob, 100)

turtle.mainloop()