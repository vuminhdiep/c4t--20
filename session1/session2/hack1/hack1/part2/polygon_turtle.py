
n = int(input("Nhap so canh vao day"))
print(n)
a = (n-2)*180/n
from turtle import *
shape("turtle")
for i in range(n):
    forward(100)
    right(a)

mainloop()