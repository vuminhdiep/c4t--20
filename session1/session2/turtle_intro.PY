from turtle import *
shape("turtle")
color("red", "yellow")
begin_fill()

for i in range(3):
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(60)

end_fill()
mainloop()