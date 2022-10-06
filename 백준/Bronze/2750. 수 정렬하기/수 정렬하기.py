N = input()
new = []
for a in range(int(N)):
    n = input()
    new.append(int(n))
new.sort()

for n in new:
    print(n)