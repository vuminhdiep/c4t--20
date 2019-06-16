user_name = input("Nhap ten dang nhap vao day")
pass_word = input("Nhap mat khau vao day")
while True:
    email = input("Nhap email vao day")
    print(email)
    print(int(len(email)))
    if len(email) >= 8 and "@" in email and "." in email:
        print("Valid")
        break
    else:
        print("Invalid")
print("Ban da dang ki thanh cong voi tai khoan la", user_name, "co mat khau la", pass_word, "va email la", email)