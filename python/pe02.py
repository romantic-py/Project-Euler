fib = [1, 1]
answer = 0
while fib[1] < 4 * 10 ** 6:
    fib = [fib[1], fib[0] + fib[1]]
    # we just need the last two terms to generate the next term.
    # so we discard the first element of fib and append the next term.
    if fib[1] % 2 == 0:
        # even
        answer += fib[1]
        
print(answer)
