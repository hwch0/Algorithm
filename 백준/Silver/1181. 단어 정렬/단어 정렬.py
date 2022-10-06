N = int(input())

text = []
for n in range(N):
    i = input()
    if i not in text:
        text.append(i)

text.sort()
text.sort(key=len)

for t in text:
    print(t)