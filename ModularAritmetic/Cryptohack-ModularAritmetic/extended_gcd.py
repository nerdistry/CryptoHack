def xgcd(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1
    while b > 0:
        q = a//b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return (a, prevx, prevy)


#Take input
a = 26513
b = 32321

result = xgcd(a, b)
print(f"gcd(a,b)=ua+vb:\n {result[0]}={result[1]}*{a}+{result[2]}*{b}")

print(f"gcd(a,b)={result[0]} \nu = {result[1]} \nv = {result[2]}")
