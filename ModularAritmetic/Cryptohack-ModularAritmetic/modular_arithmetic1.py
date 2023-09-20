'''
You can do this without any code using the following property of congruence

a ≡ b mod n, means b ≡ a mod n

so 11 ≡ a mod 6 becomes: a ≡ 11 mod 6, which is 5

8146798528947 ≡ y mod 7, becomes y ≡ 8146798528947 mod 7, which from calculations is 4

Hence the answer is 4
'''

'''You can still use the code below to solve'''

print(min(11%6, 8146798528947%17))