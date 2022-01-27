import sys
N = int(sys.stdin.readline())
rope = []
for _ in range(N):
    a = int(sys.stdin.readline())
    rope.append(a)

rope.sort()
result = []
for i in range(N):
    result.append((N-i) * rope[i])

print(max(result))