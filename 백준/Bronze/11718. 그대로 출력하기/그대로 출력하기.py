import sys
read = sys.stdin.readline

string= str(read())
result = []
while string != '':
    result.append(string)
    string = str(read())
    
for r in result:
    print(r.strip())