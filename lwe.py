import random
import numpy as np
import sympy
import math

public_key_A = []
public_key_B = []
e = []
prime_number_q = sympy.randprime(1000, 10000000)


for i in range(10):
    public_key_A.append(random.randrange(0, prime_number_q))


secret_key = random.randrange(0, prime_number_q)
"""has to be an odd number"""
while (secret_key%2 != 1): 
    secret_key = random.randrange(0, prime_number_q)

for x in range(len(public_key_A)):
    e.append(random.randrange(1,5))
    public_key_B.append((public_key_A[x]*secret_key+e[x])%prime_number_q)

sample = random.sample(range(9), len(public_key_A)//2)

message = int(input("0 or 1?: "))

print("q:",prime_number_q, "\n")
print("A:",public_key_A, "\n")
print("B:",public_key_B, "\n")
print("secret key:",secret_key, "\n")
print("error:",e, "\n")
print("message:", message, "\n")
print("sample:", sample, "\n")

u = 0
v = 0

for x in range(0, len(sample)):
    print("[",public_key_A[sample[x]],public_key_B[sample[x]],"]", ' ')
    u=u+(public_key_A[sample[x]])
    v= v+public_key_B[sample[x]]
v = v+math.floor(prime_number_q//2)*message
v = v%prime_number_q
u = u%prime_number_q

print("v:", v)
print("u:", u)

res=(v-secret_key*u) % prime_number_q

if (res>prime_number_q/2):
	print("Message is a 1")
else:
	print("Message is a 0")
