import sys
import time as t
MICRO = 1000*1000

p = 3141592653589771  # Número primo p congruente a 3 (mod 4).
q = 2718281828459051  # Número primo q congruente a 3 (mod 4).
seed = 2              # Semente aleatória entre [1, n-1].
random = 0            # Número aleatório que será gerado.
x = []                # Array dos valores de x.

n = p * q

bits = int(sys.argv[1]) + 1

start = t.time() # Tempo de início da execução.

x.append(seed*seed % n) # x[0] := seed^2 mod n.

for i in range(1, bits):
    # xi:= x[i-1]^2 mod n
    x.append( ( x[i-1]*x[i-1] ) % n)

    # Extração do bit de paridade fazendo um AND
    # lógico e concatenação com o resultado de saída
    # após fazer um deslocamento a esquerda.
    random = (random << 1) | (x[i] & 1)

end = t.time()  # Tempo de término da execução.
total_time = (end - start) * MICRO

print("Random value = " + str(random))
print("%.2f" %total_time + " microssegundos")