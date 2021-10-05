import turtle

turtle.bgcolor("black")
na=turtle.Turtle()

from random import randint

dd =25
w=5
h=5

na.penup()
color=["white","yellow","blue","green","orange","red","pink","brown","violet","grey"]

na.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0

    col=randint(0,10)
    na.color(color[col])
    while(k<m and l<n):
            if(f==1):
                na.right(90)
                
            for i in range(l,n):
                na.dot()
                na.forward(dd)
            
            k+=1
            f=1
            
            
            na.right(90)
            col=randint(0,10)
            na.color(color[col])
            for i in range(l,n):
                na.dot()
                na.forward(dd)

            n-=1
            
            na.right(90)
            col=randint(0,10)
            na.color(color[col])
            if(k<n):
                for i in range(n-1, l-1,-1):
                    na.dot()
                    na.forward(dd)
            
                l+=1


spiral(10,10)




