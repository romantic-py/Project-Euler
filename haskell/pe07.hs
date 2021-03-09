sieve (x : xs) = x : sieve [y | y <- xs, mod y x /= 0]
primes = sieve [2 ..]  -- infinite list of primes!
answer = primes !! 10000
main = putStrLn (show answer)
