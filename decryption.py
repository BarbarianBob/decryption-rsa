import math
import gcd



# Find the prime factors of n
n = 282751537468087
e = 65537
def pfactor(n):
    i = 2
    factor_arr = []
    while i * i <= n:
        if n % i !=0:
            i += 1
        else:
            n //= i
            factor_arr.append(i)
    if n > 1:
        factor_arr.append(n)
    return factor_arr


list_factors = pfactor(n)

        
    
    

p = list_factors[0]
q = list_factors[1]
print("n :", n)
print("e :" , e)
print("p :" , p)
print("q :", q)
# Calculate Phi n
phin = (p-1) * (q -1)
print("Phi n :", phin)


# Function to find the GCD 
def gcd(a,b):
    while b != 0:
        a, b=b, a % b
    return a

#Function that uses the Extended Euclidean Algorithm to find x
def xgcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        valgcd, x1, y1 = xgcd(b % a, a)
        return valgcd, y1 - (b // a) * x1, x1

a = e
b = phin

valgcd, x, y = xgcd(a,b)

print("GCD(65537, 282751503005160) :", valgcd)
print("x :", x)
print("y :", y)

# x < 0  | d = x + phin
d = x + phin 
print("d :", d)

# Write a function for modular exponentiation to decrypt the ciphertext (C)

def expmod(base, exponent, modulus):
    res = 1
    while exponent > 0:
        if exponent % 2 == 1: # if the exponent is odd 
            res = (res * base) % modulus
        exponent //= 2 # if the exponent is even
        base = (base * base) % modulus
    return res

base = 192311774615565
exponent = d 
modulus = n
# Decrpyt using C^d mod n formula 
res = expmod(base, exponent, modulus)
print("Ciphertext :", base)
print("Message :", res)