import turtle
bl=100
ll=50
angle=90

turtle.left(angle)
turtle.forward(bl)
count=0
while count<4:
    turtle.right(angle//2)
    if count !=3:
        turtle.forward(ll)
        
    else:
        turtle.forward(bl)
    count = count+1
    
turtle.right(90)
turtle.forward(130)