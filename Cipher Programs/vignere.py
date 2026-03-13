def vignere_encrypt(plaintext,key):
    ciphertext = ""
    key=key.upper()
    key_index = 0
    plaintext=plaintext.upper()
    for char in plaintext:
        if char.isalpha():
            shift=ord(key[key_index%len(key)]) -65
            ciphertext+=chr((ord(char) +shift -65)%26 +65)
            key_index+=1
        else:
            ciphertext+=char
    return ciphertext

def vignere_decrypt(ciphertext, key):
    plaintext = ""
    key=key.upper()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index%len(key)]) - 65
            decrypted_char = chr((ord(char) - shift - 65) % 26 + 65)
            plaintext += decrypted_char
            key_index += 1
        else:
            plaintext += char
    return plaintext


message = input("Enter the message to encrypt: ")
key = "deceptive"
encrypted_message = vignere_encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = vignere_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)