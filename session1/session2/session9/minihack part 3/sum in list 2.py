numlist = input("Enter a list of number separated by commas: ")
numlist = numlist.split(",")
numlist = map(int, numlist)
print("Sum of all entered numbers: ", sum(numlist))