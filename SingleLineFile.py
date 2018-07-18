f = open("List.txt", "r+")
g = open("One Line List.txt", "w+")
fcontents = f.read()
gcontents = ""
for i in range (0, len(fcontents)):
    if fcontents[i] != '\n':
        gcontents = gcontents + fcontents[i] 
g.write(gcontents)