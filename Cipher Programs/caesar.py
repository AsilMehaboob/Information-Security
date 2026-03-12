def caesar_encrypt(text,key):
    result = ""
    for char in text:
        if char.isalpha():
            char=char.upper()
            result +=chr((ord(char) +key - 65) % 26 + 65)
        else:
            result += char
    return result

def caesar_decrypt(text,key):
    result = ""
    for char in text:
        if char.isalpha():
            char=char.upper()
            result +=chr((ord(char) -key - 65) % 26 + 65)
        else:
            result += char
    return result


message = "Hello, World!"
key = 3
encrypted_message = caesar_encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = caesar_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)