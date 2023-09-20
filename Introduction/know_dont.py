from pwn import xor

hex_bytes = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
value = hex_bytes

## convert to bytes
bytes_value = bytes.fromhex(value)
xorKey = ""
crypto = b"crypto{"
for j, crypto2 in zip(bytes_value[:7], crypto):
    # :7 sliceeeee
    # xor each individual bytes with i, the position we are in
    # zip stops when one of the iterators length ends; stops at min of 2 e.g.
    xorKey += chr((j ^ crypto2))
# partial key
print(xorKey)
# last key is usually `}`
# so get that one
lastKey = ""
for i in range(0, 256):
    t = chr(i ^ bytes_value[-1])
    #-1 start from last
    if t == "}":
        lastKey = chr(i)
key = (xorKey + lastKey)
print(key)
arr = bytes(key, 'utf-8')
soln = xor(arr,bytes_value)
print(soln)


