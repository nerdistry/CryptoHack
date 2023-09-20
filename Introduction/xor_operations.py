# Given values as hexadecimal strings
KEY1_hex = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
KEY2_xor_KEY1_hex = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
KEY2_xor_KEY3_hex = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
FLAG_xor_KEYS_hex = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

# Convert hexadecimal strings to integer values
KEY1_int = int(KEY1_hex, 16)
KEY2_xor_KEY1_int = int(KEY2_xor_KEY1_hex, 16)
KEY2_xor_KEY3_int = int(KEY2_xor_KEY3_hex, 16)
FLAG_xor_KEYS_int = int(FLAG_xor_KEYS_hex, 16)

# Calculate KEY2 using Commutative property
KEY2_int = KEY2_xor_KEY1_int ^ KEY1_int

# Calculate KEY3 using Commutative property
KEY3_int = KEY2_xor_KEY3_int ^ KEY2_int

# Calculate FLAG using Self-Inverse property
FLAG_int = FLAG_xor_KEYS_int ^ KEY1_int ^ KEY3_int ^ KEY2_int

# Convert FLAG integer to bytes
FLAG_bytes = FLAG_int.to_bytes((FLAG_int.bit_length() + 7) // 8, byteorder='big')

# Decode FLAG as utf-8
flag = FLAG_bytes.decode('utf-8')

print(flag)
