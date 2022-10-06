N = input()
num = [int(n) for n in N]
num = [str(n) for n in N]
num.sort(reverse=True)
new = ''.join(num)
print(new)