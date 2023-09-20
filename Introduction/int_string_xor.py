from pwn import xor

text = 'label'
key = 13
encoded_text = text.encode('utf-8')  # Convert the text to bytes
result = xor(encoded_text, key).decode('utf-8')  # Perform XOR and then decode

print(result)
