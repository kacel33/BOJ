import sys

N = int(sys.stdin.readline())
numbers = []
for _ in range(N):
    a = int(sys.stdin.readline())
    numbers.append(a)
numbers = numbers[::-1]
count = 0
for i in range(len(numbers)-1):
    if numbers[i] <= numbers[i+1]:
        count += (numbers[i + 1] - numbers[i] + 1)
        numbers[i+1] = numbers[i]-1

print(count)