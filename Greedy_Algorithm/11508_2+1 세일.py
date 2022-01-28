import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
	a = int(sys.stdin.readline())
	numbers.append(a)
numbers.sort(reverse=True)

for i in range(len(numbers)):
	if (i+1)%3 == 0:
		numbers[i]=0
result = sum(numbers)

print(result)