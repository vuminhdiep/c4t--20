items = [5, 1, 8, 92, -1, 30]
number = int(input("Enter a number: "))
if number in items:
    print("Found", "Position: ", items.index(number)+1 )
else:
    print("Not found")