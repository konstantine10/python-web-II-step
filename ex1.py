f = open("ex1.txt", "r")

n = int(f.readline())

word_count = {}

for i in range(n):
    word = f.readline().strip()
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1

print(len(word_count));

for word in word_count:
    print(word_count[word], end=" ")
