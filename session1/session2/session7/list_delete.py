items = ["Sport", "LOL", "BTS", "Spider Man"]
items.pop(1)
print(items)
while False:
    items.remove("LOL")
    print(items)

i = input("What item do you want to remove: ")
items.pop(int(i))
print(items)

x = input("What to remove: ")
items.remove(x)
print(items)