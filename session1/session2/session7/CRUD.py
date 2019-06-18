items = ["Com", "Pho", "Bun", "Chao"]
command = input("What do you want C, R, U or D: ")
if command == "C":
    favorite = input("What do you like: ")
    items.append(favorite)
    print(items)
elif command == "R":
    for i in range(len(items)):
        print(items[i])
    if len(items) == 0:
        print("Danh sach rong")
elif command == "U":
    replacing_item = int(input("What order do you want to replace: "))
    new_item = input("What do you want to add: ")
    items[replacing_item] = new_item
    print(items)
elif command == "D":
    delete_item = input("What do you want to delete: ")
    items.remove(delete_item)
    print(items)
