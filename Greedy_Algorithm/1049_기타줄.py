import sys

N, M = map(int, sys.stdin.readline().split())
package_list = []
one_list = []
for _ in range(M):
	a, b = map(int,sys.stdin.readline().split())
	package_list.append(a)
	one_list.append(b)

cheap_package = min(package_list)
cheap_one = min(one_list)
result = min(N//6 * cheap_package, (N//6)*6*cheap_one ) + min(cheap_package, N%6 * cheap_one) 
print(result)