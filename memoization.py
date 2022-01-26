def rec_fib(n):
    #base case
    if n < 2:
        return n
    #memo case
    if n in fib_memo:
        return fib_memo[n]
    new_value = rec_fib(n-1) + rec_fib(n-2)
    fib_memo[n] = new_value
    return new_value
