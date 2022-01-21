# also known as 'cumulative sum' or 'inclusive scan'

# it holds the same idea that of tabulation

# why do you need prefix sum??
# ans: for Range Queries
# https://codeforces.com/blog/entry/77128
def prefixs(arr):
    n = len(arr)
    res = [0]*n # initializing
    res[0] = arr[0] # seeding

    for i in range(1, n):
        res[i] = res[i-1]+arr[i] # result er i-1 r array er current value
    return res

# find sum of 2 to 6 in [4, 1, 2, -2, 6, 8, 4, 9, 0]

# Q. can prefix sum be applied to an array which has negative value in it?

