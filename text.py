from turtle import Turtle, Screen
oyna = Screen()
oyna.title('mening oynam')

chiq = Turtle()
chiq.color('red')
chiq.pensize(5)
chiq.speed(0)
chiq.hideturtle()
chiq.up()
chiq.goto(300,300)
chiq.down()
chiq.goto(300,-300)
chiq.goto(-300,-300)
chiq.goto(-300, 300)
chiq.goto(300, 300)

top = Turtle()
top.shape('circle')
top.up()
top.goto(0, 0)
top.color('blue')
step_x = 3
step_y = 2
while True:
    x, y  = top.position()
    if x+ step_x >=300 or x+step_x<= -300:
        step_x = -step_x
    if y+step_y>=300 or y+step_y <= -300 :
        step_y= -step_y    
    top.goto(x+step_x, y+step_y)
    
oyna.mainloop() 