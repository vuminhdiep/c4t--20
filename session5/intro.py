from random import randint
print(randint(0, 100))

month = int(input("Month of a year"))
print(month)

if month < 4:
    print("Xuan")
elif month < 7:
    print("Ha")
elif month < 10:
    print("Thu")
else:
    print("Dong")

from random import randint
weather = int(randint(0, 100))
print(weather)
if weather < 30:
    print("Rainy")
elif 30 <= weather < 60:
    print("Cloudy")
else:
    print("Sunny")

from random import randrange
print(randrange(-2, 100))
