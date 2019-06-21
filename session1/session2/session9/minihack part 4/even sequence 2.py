numlist = input("Enter a list of number separated by commas: ")
numlist = numlist.split(",")
numlist = [float(i) for i in numlist]
for i in range(len(numlist)):
    if numlist[i] %2==0:
        print(numlist[i])