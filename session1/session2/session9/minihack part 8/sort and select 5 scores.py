highscore = [45, 67, 56, 78]
highscore.sort(reverse = True)
print(highscore)
new = input("Enter your new highscore: ")
highscore.append(int(new))
highscore.sort(reverse = True)
print(highscore)
new_score = input("Enter your new highscore: ")
highscore.append(int(new_score))
highscore.sort(reverse = True)
print(*highscore[0:5], sep=", ")
