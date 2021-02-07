import turtle as R_circle 

R_circle.bgcolor('black') 
R_circle.pensize(2) 
R_circle.speed(10) 
for i in range(6): 
    for color in ('green', 'magenta','white','yellow', 'blue',  
                  'cyan', 'red'): 
        R_circle.color(color) 
        R_circle.circle(100) 
        R_circle.left(10) 
    R_circle.hideturtle()