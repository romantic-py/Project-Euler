# original algorithm to generate prime list upto a certain integer.
# modified from pe7.py

primes = [2, 3, 5, 7]

def check_primality(n, int_root):
    for p in primes:
        if p > int_root:  # p > n ** 0.5
            break
        elif n % p == 0:  # n is not prime
            return False
    return True

def extend_prime_list(upto_number = 2 * 10 ** 6):
    n = 11
    last_int_root = 4
    last_int = 16  # last_int = last_int_root ** 2
    while n < upto_number:
        if last_int <= n:
            last_int_root += 1
            last_int += 2 * last_int_root - 1
        if check_primality(n, last_int_root):
            primes.append(n)
        n += 2
    return None


if __name__ == "__main__":
    extend_prime_list()
    answer = sum(primes)
    print(answer)
