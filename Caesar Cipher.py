def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext += shift_char
        else:
            ciphertext += char
    return ciphertext
                
plaintext = "CAESAR"
shift = 10
ciphertext = caesar_cipher(plaintext, shift)
print("Ciphertext: ", ciphertext)
