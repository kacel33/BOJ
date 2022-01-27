import sys
N, M = map(int, sys.stdin.readline().split())
moneys = []
for i in range(N):
    a = int(sys.stdin.readline())
    moneys.append(a)

count = 0
for money in reversed(moneys):
    while True:
        if M - money >= 0:
            M -= money
            count += 1
        else:
            break
print(count)