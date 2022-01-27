import sys
import math
N= int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
numbers = sorted(numbers)
SUM = 0
for i in range(len(numbers)):
    SUM += sum(numbers[:i+1])
print(SUM)
