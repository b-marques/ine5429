import random 
import sys
import time as t

MICRO = 1000000

def miller_rabin(n, k=10):
    # Casos <= 4
    if (n <= 1):     return False
    if (n <= 3):     return True
    if (n == 4):     return False
    if (n % 2 == 0): return False

    # Encontre inteiros s, d, com s > 0, d ímpar, de modo que (n – 1 = 2^s * d);
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2;
        s += 1     

    # Laço responsável por realizar k testes
    for _ in range(k):
        # Selecione um inteiro aleatório a, tal que 1 < a < n – 1;
        a = random.randrange(2, n-1)

        # if a^d mod n = 1 then return(“inconclusive”);
        x = pow(a, d, n)
        if x == 1 or x == n-1:
            return True

        # Laço que irá executar 's-1' vezes.
        for _ in range(s-1):
            x = pow(x,2,n)
            if x == 1:
                return False
            if x == n-1:
                return True

    return False

nbits = int(sys.argv[1]) # Número de bits, definido pelo usuário

start = t.time() # Tempo de início da execução.
while True:
    # Número aleatório com N bits
    n = random.getrandbits(nbits) 
    if miller_rabin(n) == True:
        break
end = t.time()  # Tempo de término da execução.

total_time = (end - start) * MICRO

print("Random value = " + str( n ))
print("%.2f" % total_time + " microssegundos")
