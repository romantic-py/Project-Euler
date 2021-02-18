fib = [1, 1]
answer = 0
while fib[1] < 4 * 10 ** 6:
    fib = [fib[1], fib[0] + fib[1]]
    if fib[1] % 2 == 0:
        answer += fib[1]
        
print(answer)
