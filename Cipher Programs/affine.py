def mod_inverse(a,m):
    for i in range(1,n):
        if (a*i) % m == 1:
            return i
    return None

def affine_encrypt(plain_text, a, b):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            char = char.upper()
            cipher_char = chr((a*ord(char) + b - 65) % 26 + 65)
            cipher_text += cipher_char
    return cipher_text

def affine_decrypt(cipher_text, a, b):
    plain_text = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Inverse does not exist, choose a different 'a' value.")
    for char in cipher_text:
        if char.isalpha():
            char=char.upper()
            plain_char = chr((a_inv * (ord(char) - b - 65)) % 26 + 65)
            plain_text += plain_char
    return plain_text

message = "MATH"
a = 5
b = 8
encrypted_message = affine_encrypt(message, a, b)
print("Encrypted message:", encrypted_message)
decrypted_message = affine_decrypt(encrypted_message, a, b)
print("Decrypted message:", decrypted_message)