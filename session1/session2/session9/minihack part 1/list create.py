items = ["blue", "red", "teal", "green"]
print("Our color list: ", *items, sep=", ")
new_color = input("What do you want to add? ")
items.append(new_color)
print("Our new color list: ", *items, sep=", ")