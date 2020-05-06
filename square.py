import turtle
turtle.color("red")
turtle.speed(2)
def draw_sqaure(side_length):
 for i in range(4):
     turtle.forward(side_length)
     turtle.left(90)
 counter=0
 while counter < 90 :
       draw_sqaure(100)
       turtle.right(4)
       counter+= 1
turtle.exitonclick()
