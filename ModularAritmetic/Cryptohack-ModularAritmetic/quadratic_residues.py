'''
Youtube is your friend

https://www.youtube.com/watch?v=aBn7BaRxu2g&list=PL22w63XsKjqwn36stOtD07VMfcCT-HRLc
https://www.youtube.com/watch?v=M6gDsFhQugM

'''

p = 29
ints = [14, 6, 11]


#pow(x, y, z) => (x^y)%z
qr = [x for x in range(p) if pow(x,2,p) in ints]

print(min(qr))

