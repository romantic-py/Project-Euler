extendPrimeList :: Integer -> [Integer] -> Integer -> Integer -> [Integer]
extendPrimeList n primes intRoot lim
    | lim <= n = primes
    | intRoot * intRoot <= n = extendPrimeList n primes (intRoot + 1) lim
    | null [k | k <- takeWhile (<= intRoot) primes, mod n k == 0] = extendPrimeList (n + 2) (primes ++ [n]) intRoot lim
    | otherwise = extendPrimeList (n+2) primes intRoot lim
    
-- answer = sum $ extendPrimeList 11 [2,3,5,7] 4 2000000
-- this is slow af.

intSqrt n = round $ sqrt n

isPrime :: Integral a => a -> Bool
isPrime n = null [k | k <- [2 .. intSqrt $ fromIntegral n], mod n k == 0]

tillN = 2 * 10^6 :: Integer
answer :: Integer
answer = sum $ filter isPrime [2 .. tillN]
-- this is also slow :(
-- need to figure out a way of fast generation of primes in Haskell

main :: IO ()
main = print answer
