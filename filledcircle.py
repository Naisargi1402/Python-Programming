import turtle
import time
t= turtle.Pen()
def mycircle(red, green, blue):
 t.color(red, green, blue)
 t.begin_fill()
 t.circle(50)
 t.end_fill()
 
mycircle(0,1,0)
time.sleep(5)

mycircle(1,1,1)
time.sleep(5)