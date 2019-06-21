highscore = [45, 67, 56, 78]
highscore.sort(reverse = True)
print(highscore)
new = input("Enter your new highscore: ")
highscore.append(int(new))
print(highscore)