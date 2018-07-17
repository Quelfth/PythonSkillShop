from random import *
print("How many words would you like me to collect?")
amount = input()
words = []
for i in range (0, amount):
    words.append(raw_input())
print(words[randint(0, len(words)-1)])