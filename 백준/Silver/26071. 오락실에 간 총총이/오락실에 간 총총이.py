import sys

read= sys.stdin.readline

n = int(read())

vertex = [(0,0), (0,(n-1)),((n-1),0),((n-1),(n-1))]
graph = []
distance=[]

for i in range(n):
    j = 0
    for gom in read():
        if gom =='G':
            graph.append((i,j))
        j+=1

if len(graph) ==1 :
    print(0)
elif len(set([x[0] for x in graph]))==1:
    for i,v in enumerate(vertex):
        w = [abs(v[1] - g[1]) for g in graph]
        distance.append((max(w)))
    print(min(distance))
elif len(set([x[1] for x in graph]))==1:
    for i,v in enumerate(vertex):
            h = [abs(v[0] - g[0]) for g in graph]
            distance.append((max(h)))
    print(min(distance))
else: 
    for i,v in enumerate(vertex):
        w = [abs(v[1] - g[1]) for g in graph]
        h = [abs(v[0] - g[0]) for g in graph]
        distance.append((max(w)+max(h)))
    print(min(distance))