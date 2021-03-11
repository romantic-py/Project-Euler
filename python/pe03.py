
number = 600851475143
root = int(number ** 0.5)

sieve_of_eratosthenes = [True] * (root + 1)
primes_till_root = []  # all the primes <= root

for n in range(2, root + 1):
    if sieve_of_eratosthenes[n]:
        primes_till_root.append(n)
        for j in range(n*n, root + 1, n):
            sieve_of_eratosthenes[j] = False

largest_prime_factor = 1
for prime in primes_till_root:
    if number % prime == 0:
        largest_prime_factor = max(largest_prime_factor, prime)
    while number % prime == 0:
        number //= prime

# After the loop ends, largest_prime_factor gives 
# the largest prime factor of number which is smaller than root.
# Now, if number != 1, then number is a prime greater than root.
# Otherwise, largest_prime_factor is the required answer.
# So, we do this...
largest_prime_factor = max(largest_prime_factor, number)

print(largest_prime_factor)

