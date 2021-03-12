from math import factorial as fac

# Let us denote vertical (down) arrow as 1 and horizontal (right) arrow as 0.
# For N x N grid, we must take N down steps and N right steps.
# So, the number of ways = number of strings with N 0's and N 1's
# which is just (N + N)! / (N! * N!)

N = 20
answer = fac(N + N) // fac(N) // fac(N)  # for N x N grid
print(answer)
