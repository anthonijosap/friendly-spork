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
    for word in line.split():
        if word not in stopwords:
            filtered_lines.append(word)

print(filtered_lines)