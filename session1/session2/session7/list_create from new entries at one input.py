names = input("Name your things: ")
print(names)
name_split = names.split(",")
print(*name_split, sep= ", ")
for i in range(len(name_split)):
    print(name_split[i])