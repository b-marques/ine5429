import random 
import sys
import time as t

MICRO = 1000000

def fermat(n, k=40):
# Casos <= 4
    if (n <= 1):     return False
    if (n <= 3):     return True
    if (n == 4):     return False
    if (n % 2 == 0): return False

    for _ in range(k):
        a = random.randrange(2, n-1)

        if pow(a, n-1, n) != 1:
            return False

    return True

nbits = int(sys.argv[1]) # Número de bits, definido pelo usuário

start = t.time() # Tempo de início da execução.
while True:
    # Número aleatório com N bits
    n = random.getrandbits(nbits) 
    if fermat(n) == True:
        break
end = t.time()  # Tempo de término da execução.

total_time = (end - start) * MICRO

print("Random value = " + str( n ))
print("%.2f" % total_time + " microssegundos")
