answer = head [a*b*c | a <- [3..333], b <- [a+1 .. 499], let cSquare = a^2 + b^2, let c = 1000 - a - b, c^2 == cSquare]
main = print answer
