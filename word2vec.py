file = open('word2vecdata.txt', 'r')
lines = file.readlines()
file.close()
print(lines)

for i in range(len(lines)):
    lines[i] = lines[i].lower().replace('\n', '')

print(lines)

stopwords = ['the', 'is', 'in', 'and', 'to', 'of','a', 'that', 'it', 'with', 
             'as', 'for', 'was', 'on', 'are', 'by', 'this', 'be', 'or', 'from']

filtered_lines = []

for line in lines:
    temp = []
    for word in line.split():
        if word not in stopwords:
            temp.append(word)
    filtered_lines.append(temp)

print(filtered_lines)

bigram = []
#addded comments
for line in filtered_lines:
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            bigram.append([line[i], line[j]])
            bigram.append([line[j], line[i]])
print(bigram)