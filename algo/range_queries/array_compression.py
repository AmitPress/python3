s = 'My madame is so hot'

mp = { k:0 for k in 'abcdefghijklmnopqrstuvwxyz '}
s = s.lower()
for x in s:
    mp[x] += 1
print(mp['m'])


num = [-4, 12356563258625, -342, 11, 12356563258625, -342, -4, -3, -4]

mpp = { k:0 for k in num }

for x in num:
    mpp[x] += 1

print(mpp)