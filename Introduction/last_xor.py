hex_bytes = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
for i in range(0, 256):

    value = hex_bytes

    ## convert to bytes
    bytes_value = bytes.fromhex(value)
    # print(len(bytes_value))
    reconstructed = ""
    for j in bytes_value:
        # xor each individual bytes with i, the position we are in
        reconstructed += chr((j ^ i))
    if reconstructed.startswith("crypto"):
        # in case we have found it, print it and exit
        print(reconstructed)
        break
