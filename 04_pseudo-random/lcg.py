import sys
import time as t
MICRO = 1000*1000

m = 3141592653589771 # Módulo m
c = 2718281828459051 # Incremento c
a = 2718281828459051 # Multiplicaor a
seed = 2             # Semente X0
random = 0            
x = []                

bits = int(sys.argv[1]) + 1

start = t.time() # Tempo de início da execução.

x.append(seed) # x[0] := seed.

for i in range(1, bits):
    # x[n] = (a * X[n-1] + c) mod m
    x.append( ( a * x[i-1] + c ) % m)
    random = (random << 1) | (x[i] & 1)
    
end = t.time()  # Tempo de término da execução.
total_time = (end - start) * MICRO

print("Random value = " + str(random))
print("%.2f" %total_time + " microssegundos")
