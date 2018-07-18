f = open("List.txt", "r+")
lst = f.read().split()
f.close()
print(lst)