import calendar
m = int(input("Nhap so thang vao day"))
y = int(input("Nhap so nam vao day "))
print(calendar.monthrange(y, m)[1])
