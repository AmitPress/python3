# fibonnaci series

# the `fib()` will give us the fibonacci number on a given position

def fib(pos, memo={}):
    if(pos <= 2): return 1
    if(pos in memo): return memo[pos]
    memo[pos]=fib(pos-1,memo)+fib(pos-2,memo)
    return memo[pos]
# visualize with tree
print(fib(55))