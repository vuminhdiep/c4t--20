import random
items = ["Sports", "LOL", "BTS", "Death Note", "Netflix"]
chosen_word = random.choice(items)
print(chosen_word)
characters = list(chosen_word)
print(characters)
import random
print("".join(random.sample(characters,len(characters))))
while True:
    guess_word = input("What is the word: ")
    if chosen_word == guess_word:
        print("Correct")
        break
    else:
         print("Try again")