items = ["blue", "red", "teal", "green"]
i = input("What do you want to delete: ")
print(i)
if i.isdigit():
    items.pop(int(i))
    print(items)
if i.isalpha():
    items.remove(str(i))
    print(items)