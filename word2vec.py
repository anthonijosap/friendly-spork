file = open('word2vecdata.txt', 'r')
lines = file.readlines()
file.close()
print(lines)

for i in range(len(lines)):
    lines[i] = lines[i].lower().replace('\n', '')

print(lines)