from Crypto.Util.number import long_to_bytes

# The given integer
integer_value = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer back to bytes
message_bytes = long_to_bytes(integer_value)

# Convert the bytes to a string
message = message_bytes.decode('utf-8')

print(message)
