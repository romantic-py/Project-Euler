# original algorithm to generate prime list of desired length

primes = [2, 3, 5, 7]

def check_primality(n, int_root):
    for p in primes:
        if p > int_root:  # p > n ** 0.5
            break
        elif n % p == 0:  # n is not prime
            return False
    return True

def extend_prime_list(length = 10001):
    current_length = 4
    n = 11
    last_int_root = 4
    while current_length < length:
        if last_int_root * last_int_root <= n:
            last_int_root += 1
        if check_primality(n, last_int_root):
            primes.append(n)
            current_length += 1
        n += 2
    return primes[-1]

print(extend_prime_list())
