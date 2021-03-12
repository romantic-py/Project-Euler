number = 2 ** 1000
answer = 0
while number > 0:
    last_digit = number % 10
    answer += last_digit
    number //= 10

print(answer)
