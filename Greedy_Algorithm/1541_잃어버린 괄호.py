import sys

string = sys.stdin.readline().strip()
string = string.split('-')
result = int(sum([int(x) for x in string[0].split('+')]))
for st in string[1:]:
    st = st.split('+')
    result -= sum([int(x) for x in st])
print(result)