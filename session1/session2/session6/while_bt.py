while True:
    txt = input("Enter your password?")
    print(txt)
    if txt.isdigit() and len(txt) >= 8:
        print("correct")
        break
    else:
        print("incorrect")




       
