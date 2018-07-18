f = open(raw_input(), "r+")
lst = f.read().split()
f.close()
word = raw_input()
count = 0
for i in range (0, len(lst)):
    if word == lst[i]:
        count += 1
print(count)