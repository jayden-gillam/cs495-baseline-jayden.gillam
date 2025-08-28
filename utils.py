def caesar_cipher(plaintext, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ciphertext = ""
    plaintext = plaintext.lower()

    for c in plaintext:
        if c.isalpha():
            plaintext_index = alphabet.index(c)

            if plaintext_index + shift > 25:
                cipher_c = alphabet[plaintext_index + shift - 26]
            else:
                cipher_c = alphabet[plaintext_index + shift]

            ciphertext += cipher_c
        else:
            ciphertext += c

    return ciphertext
