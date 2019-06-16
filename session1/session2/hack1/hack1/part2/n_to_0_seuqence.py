n = int(input("Nhap so n vao day"))

if n%2==1:
    for i in range(n, 0, -2):
        print(i)
else:
    for i in range(n-1, 0, -2):
        print(i)

     
