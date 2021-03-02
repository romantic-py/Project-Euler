
def jaa_jeele_apni_zindagi():
    # ignore the name of the function
    current_n = 2
    next_n = 3
    divs_cur_n = number_of_divisors(current_n)
    divs_nxt_n = number_of_divisors(next_n)
    ans = 2
    while True:
        divs_twice_tri_n = divs_cur_n * divs_nxt_n
        # we know that n and n+1 are co-prime for all n,
        # and if two numbers are co-prime, 
        # number of divisors of the product = the product of the numbers of divisors.
        m = current_n
        if current_n % 2 != 0:
            m = next_n
        # m is the even of the two, current_n and next_n
        power_of_2 = 0  # highest power of 2 that divides m
        while m % 2 == 0:
            m //= 2
            power_of_2 += 1
        divs_tri_n = divs_twice_tri_n // (power_of_2 + 1) * power_of_2
        if divs_tri_n >= 500:
            ans = current_n * next_n // 2  # current_n th triangle number
            break
        current_n, next_n = next_n, next_n + 1
        divs_cur_n, divs_nxt_n = divs_nxt_n, number_of_divisors(next_n)
    
    return ans


def number_of_divisors(n):
    divs = 2
    for x in range(2, n):
        if n % x == 0:
            y = n // x
            if y == x:
                divs += 1
            if y <= x:
                break
            divs += 2
    return divs


if __name__ == "__main__":
    answer = jaa_jeele_apni_zindagi()
    print(answer)
