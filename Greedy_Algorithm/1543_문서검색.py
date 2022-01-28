import sys

file = str(sys.stdin.readline()).strip()
word = str(sys.stdin.readline()).strip()
result = file.replace(word,'*')
print(result.count("*"))