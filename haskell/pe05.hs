list_lcm :: [Int] -> Int
list_lcm [a] = a
list_lcm [a,b] = lcm a b
list_lcm (r : s : rs) = list_lcm $ lcm r s : rs

answer = list_lcm [1..20]
main = putStrLn (show answer)
