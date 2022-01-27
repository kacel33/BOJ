import sys
N = int(sys.stdin.readline())
first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

SUM = 0
first.sort()
second.sort(reverse=True)
for a, b in zip(first, second):
    SUM += a * b

print(SUM)