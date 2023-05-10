score = int(input())

result = "A" if score>=90 and score<=100 else "B" if score>=80 and score<=89 else "C" if score>=70 and score<=79 else "D" if score>=60 and score<=69 else "F"

print(result)