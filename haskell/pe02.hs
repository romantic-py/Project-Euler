make_fibonacci_n :: [Int] -> Int -> [Int]
make_fibonacci_n fib n  -- generates the list of fibonacci numbers till the first such number >= n
    | head fib > n = fib
    | otherwise = make_fibonacci_n (sum(take 2 fib) : fib) n

fib = make_fibonacci_n [2, 1] (4 * 10^6)

answer = sum $ filter even $ tail fib
main = putStrLn (show answer)
