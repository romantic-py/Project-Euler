make_fib_n fib n  -- generates the list of fibonacci numbers till the first such number >= n
    | head fib > n = fib
    | otherwise = make_fib_n (sum(take 2 fib):fib) n

fib = make_fib_n [2, 1] (4*10^6)

answer = sum [x | x <- tail fib, even x]
