import sys
import math
N= int(sys.stdin.readline())

x = math.floor(N / 5)
y = -1
for i in range(x, -1, -1):
    if (N - 5 * i)%3 ==0:
        y = (N - 5 * i)/3
        print(int(i+y))
        break
if y == -1:
    print(-1)