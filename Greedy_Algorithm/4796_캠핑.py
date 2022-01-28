import sys
L, P, V = [], [], []
while True:
	l, p, v = map(int, sys.stdin.readline().split())
	if l == 0 and p == 0 and v == 0:
		break	
	L.append(l)
	P.append(p)
	V.append(v)
for i, (l, p, v) in enumerate(zip(L, P, V)):
	if v%p <= l:
		result = (v//p) * l + v%p
	else:
		result = (v//p) * l + l
	print("Case {}: {}".format(i+1,result))
    