import sys
from collections import deque
N, L = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
numbers = deque(numbers)
while len(numbers) >0:
	if L >= numbers[0]:
		L += 1
		numbers.popleft()
	else:
		break
print(L)