word = input("Enter a word: ")
characters = list(word)
print(characters)
import random
print("".join(random.sample(characters,len(characters))))