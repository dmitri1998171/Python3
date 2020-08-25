import random

N = int(input("rows: "))
M = int(input("columns: "))

s = []

for i in range(N):
   s.append([random.randint(0,9) for _ in range(M)])


for i in range(N):
    for j in range(M):
        print(s[i][j], end='')
    print()
