'''
Khan academy: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/modular-inverses


The solution can be obtaibed without any code.

3 * d ≡ 1 mod 13
----------------
3 * 1 ≡ 3 ≡ 3 mod 13
3 * 2 ≡ 6 ≡ 6 mod 13
3 * 3 ≡ 9 ≡ 4 mod 13
3 * 4 ≡ 12 ≡ 12 mod 13
3 * 5 ≡ 15 ≡ 2 mod 13
3 * 6 ≡ 18 ≡ 5 mod 13
3 * 7 ≡ 21 ≡ 8 mod 13
3 * 8 ≡ 24 ≡ 11 mod 13
3 * 9 ≡ 27 ≡ 1 mod 13 --> bingo

d = 9

Though this is quite some work
'''

d = 0

while(3 * d) % 13 !=1 :
    d += 1

print(d)
