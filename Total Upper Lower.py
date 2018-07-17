sentence = raw_input()
uppers = 0
lowers = 0
for i in range (0, len(sentence)):
    if sentence[i] in "abcdefghijklmnopqrstuvwxyz":
        lowers += 1
    elif sentence[i] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        uppers += 1
print("Uppers: "+str(uppers))
print("Lowers: "+str(lowers))