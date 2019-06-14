user_name = input("Nhap ten dang nhap vao day")

while True:
    pass_word_1 = input("Nhap mat khau vao day")
    pass_word_2 = input("Nhap lai mat khau vao day")
    print(pass_word_1)
    print(pass_word_2)
    if pass_word_1 == pass_word_2:
        print("Done")
        break
    else:
        print("Again")
email = input("Nhap email vao day")
print("Ban da dang ki thanh cong voi tai khoan la", user_name, "co mat khau la", pass_word, "va email la", email)