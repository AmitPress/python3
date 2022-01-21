import sys
input = raw_input
N = list(map(int, list(input()).split()))
st = []
for n in N:
    st.append(n**0.5)

while len(st):
    print(format(st.pop(), '.4f'), end='')
    if not len(st) is 0:
        print(' ',end='')
    else:
        print()