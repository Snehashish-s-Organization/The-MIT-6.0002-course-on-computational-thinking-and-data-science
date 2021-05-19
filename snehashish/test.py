# implements the idea of fibonachi numbers

def fastFib(number, memo = {}):

    if number == 0 or number == 1:
        return 1

    try:
        result = memo[number]
    except:
        result = fastFib(number-1) + fastFib(number-2)
        memo[number] = result
    
    return result

print(fastFib(121))