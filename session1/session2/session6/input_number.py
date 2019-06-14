while True:
    txt = input("Enter your name? ")
    print(txt)
    if txt.isalpha():
        print("done")
        break
    else:
        print("again")
        

