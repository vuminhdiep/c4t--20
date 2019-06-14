print("12345")
print("abcxyz")
x = int(input("3"))
y = int(input("5"))
print(x + y)

t = turtle.Turtle()
t.fillcolor('blue')
t.begin_fill()
for i in range(4):
  t.forward(150)
  t.right(90)
t.end_fill()