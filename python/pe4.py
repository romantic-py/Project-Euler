
answer = 0
for i in range(100, 1000):
    for j in range(i, 1000):
        p = i * j
        if p >= 10 ** 6: 
            break
        sp = str(p)
        if p == 906609:
            print(i,j)
        if sp == ''.join(reversed(sp)):
            answer = max(answer, p)

print(answer)
