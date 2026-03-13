import numpy as np

key_matrix = np.array(eval(input("Key matrix: ")))
plaintext = input("Plaintext: ").upper().replace(" ", "")
matrix_size = len(key_matrix)

while len(plaintext) % matrix_size:
    plaintext += 'X'

ciphertext = ""

for i in range(0, len(plaintext), matrix_size):
    plaintext_block = np.array([ord(char) - 65 for char in plaintext[i:i+matrix_size]])
    cipher_block = np.dot(key_matrix, plaintext_block) % 26
    ciphertext += ''.join(chr(num + 65) for num in cipher_block)

print("Ciphertext:", ciphertext)

adjugate_matrix = np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int)
determinant = int(round(np.linalg.det(key_matrix)))

for i in range(26):
    if (determinant * i) % 26 == 1:
        modular_inverse = i

inverse_key_matrix = (modular_inverse * adjugate_matrix) % 26

decrypted_text = ""

for i in range(0, len(ciphertext), matrix_size):
    cipher_block = np.array([ord(char) - 65 for char in ciphertext[i:i+matrix_size]])
    plaintext_block = np.dot(inverse_key_matrix, cipher_block) % 26
    decrypted_text += ''.join(chr(num + 65) for num in plaintext_block)

print("Decrypted:", decrypted_text)