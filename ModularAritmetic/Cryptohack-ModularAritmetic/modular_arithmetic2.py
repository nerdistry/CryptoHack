'''
Read on Fermat's little problem first then come back, Wikipedia's article should suffice
'''

'''
You didn't skip the part above. Did you? (Draws knife)jk

The challenge gives an example of 3^17 mod 17 which equals 3.
5^17 mod 17 = 5.

This follows the theorem a^p ≡ a (mod p)

For 7^16 mod 17, the answer is 1, since a^p-1 ≡ 1 (mod p)

Our challenge follows the same principle as this since 65536-1 = 65537, hence the answer is 1 (no calculator needed)

'''

def fermats_little_theorem(base, exp, prime):
    if (exp == prime):
        return base
    #the base has to be a coprime of the prime: not divisible by the prime
    #why tf does py use 'and' not '&&'
    elif (exp + 1 == prime and base % prime != 0):
        return 1
    else:
        return -1

result = fermats_little_theorem(273246787654,65536, 65537)

print(result)