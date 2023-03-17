f = open("ex2.txt", "r")


def lexicographical_order(s):
    s = list(s)

    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1

    if i < 0:
        return "no answer"

    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1

    tmp = s[j]
    s[j] = s[i]
    s[i] = tmp

    return ''.join(s)


n = int(f.readline())

for _ in range(n):
    word = f.readline().strip()
    print(lexicographical_order(word))
