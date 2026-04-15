
import colorgram
import random
import turtle as turtle_module
turtle_module.colormode(255)
tim=turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
colors=colorgram.extract('image.jpg',30)
rgb_list=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r,g,b)
    rgb_list.append(new_color)

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
num_of_dots=100
for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(rgb_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen=turtle_module.Screen()
screen.exitonclick()
