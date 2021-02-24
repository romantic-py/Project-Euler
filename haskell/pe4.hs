answer = maximum [x*y | x <- [100..999], y <- [x..999], let s = show (x*y), reverse s == s]
