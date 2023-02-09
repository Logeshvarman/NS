def substitution_cipher(plaintext, plain_alphabets, cipher_alphabets):
    ciphertext = ""
    for char in plaintext:
        if char in plain_alphabets:
            index = plain_alphabets.index(char)
            ciphertext += cipher_alphabets[index]
        else:
            ciphertext += char
            return ciphertext
            
plain_alphabets = "PLAINCD1EHINPRSTY"

cipher_alphabets = "CIPHERXJLAAZEVKHOM"

plaintext = "THIS SENTENCE IS ENCRYPTED"

ciphertext = substitution_cipher(plaintext, plain_alphabets,cipher_alphabets)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
