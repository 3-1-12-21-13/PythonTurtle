from turtle import *

speed(1)

# step 1 - background color
bgcolor("black")

# step 2 - pen color
color("orange")

# step 3 - draw the first planet
begin_fill()
circle(60)
end_fill()

# step 4 - move the marker to the next planet
penup()
forward(100)
pendown()

# step 5 - draw the second planet
color("gray")
begin_fill()
circle(20)
end_fill()

# step 6 - move the marker to the next planet
penup()
forward(100)
pendown()

# step 7 - draw the third planet
color("red")
begin_fill()
circle(40)
end_fill()

# step 8 - move the marker to the next planet
penup()
forward(100)
pendown()

# step 9 - draw the fourth planet
color("green")
begin_fill()
circle(20)
end_fill()


done()
