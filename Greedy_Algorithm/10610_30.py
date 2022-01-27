import sys
N = list((sys.stdin.readline()))
del N[-1]
N = [int(x) for x in N]
N.sort(reverse=True)
if N[-1] !=0 or sum(N) % 3 != 0:
    print(-1)
else:
    a = str()
    for i in range(len(N)):
        a += str(N[i])
    print(int(a))