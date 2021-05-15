"""
Implements the idea of memoization
Memoization is a way of reducing the time complexity of
an algorithm by reducing the amount of computation required
It does it by remembering if the computation is already done
and if it is then it does not comute it else it does.
"""

# function to calculate the fibonachi nuber
def fib(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fib(number-1)+fib(number-2)

# funcrion that uses memoization to reduce time complexity
def memofib(number, memo = {}):
    # returning the 1 if the number is one or zero
    if number == 0 or number == 1:
        return 1

    # trying to get the number from the memo if it's
    # fibonachi number exists and not computing it.
    try:
        return memo[number]
    # if the number is not yet computed (in the meme) then
    # computing it and putting it into the memmo
    except KeyError:
        result = memofib(number-1)+memofib(number-2)
        memo[number] = result
        
    return result
for i in range(1000):
    print(f"FIB of {i} = {memofib(i)}")