answer = 0
for c in range(999, 3, -1):
    if answer > 0:
        break
    for b in range(1, max(1000 - c + 1, c)):
        a = 1000 - b - c
        if a*a + b*b == c*c:
            answer = a*b*c
            break
 
print(answer)        
