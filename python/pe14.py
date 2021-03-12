chain = {1:0}

def chain_length(n):
    if n in chain:
        pass
    elif n % 2 == 0:
        chain[n] = 1 + chain_length(n // 2)
    else:
        chain[n] = 2 + chain_length((3*n + 1) // 2)
    return chain[n]

answer = None
cap = 10 ** 6
max_chain_length = 0
for n in range(2, cap):
    cur_chain_length = chain_length(n)
    if max_chain_length < cur_chain_length:
        max_chain_length = cur_chain_length
        answer = n

print(answer)
