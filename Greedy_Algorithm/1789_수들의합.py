import sys
import math
N = int(sys.stdin.readline())

result = math.floor((2*N+1/4)**0.5-1/2)

print(result)