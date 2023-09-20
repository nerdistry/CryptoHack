import sys
import base64

hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Convert hex string to bytes
flag = bytes.fromhex(hex_string)

# Encode the bytes as base64
base = base64.b64encode(flag)
base = base.decode('utf-8')

print("Here is my flag:")
print(base)
