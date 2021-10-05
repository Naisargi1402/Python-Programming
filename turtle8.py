import turtle

turtle.bgcolor("black")
na=turtle.Turtle()

width=5
height=7

dd=25

na.setpos(-250,250)

def spiral(m,n):
    k=0
    l=0
    f=0
    na.color("white")
    
    while(k<m and l<n):
        if(f==1):
            na.right(90)
            
        for i in range(l,n):
            na.forward(dd)
        
        k+=1
        f=1
        
        na.right(90)
        
        for i in range(k,m):
            na.forward(dd)
            
        n-=1
        na.right(90)        
            
        if(k<m):
            for i in range(n-1,l-1,-1):
                na.forward(dd)
            
            m-=1
        na.right(90)
        if(l<n):
        
            for i in range(m-1,k-1,-1):
                na.forward(dd)
                #print(a[i][l],end=" ")
            l+=1
            
 
spiral(10,10) 