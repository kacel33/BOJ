import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
	a = int(sys.stdin.readline())
	numbers.append(a)
numbers.sort(reverse=True)
for i in range(len(numbers)):
	numbers[i] = numbers[i] - i
	if numbers[i] < 0:
		numbers[i] = 0
print(sum(numbers))