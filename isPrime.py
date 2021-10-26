prime = [2]
for x in range(2, 100):
    isPrime = True
    for y in prime:
        if (x % y == 0):
            isPrime = False
            break
    if (isPrime == True):
        prime.append(x)
print(prime)