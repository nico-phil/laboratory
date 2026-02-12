#Cipher Cesear

# def caesar_char(c, k):
#     #uppercase letters
#     if 'A' <= c <= 'Z':
#         base = ord('A')
#         return chr((ord(c) - base + k) % 26 + base)
#     # lowercase letters
#     elif 'a' <= c <= 'z':
#         base = ord('a')
#         return chr((ord(c) - base + k) % 26 + base)
#     #not a letter, just return c
#     else:
#         return c 


# def caesar_encrypt(text, k):
#     return ''.join(caesar_char(c, k) for c in text)


# # Example
# text = input("Write the text to encrypt: ")
# k = int(input("Write the key(number): "))

# encrypted = caesar_encrypt(text, k)
# print("Ceasar cipher:", encrypted)

def caesar_char(char, k):
     #uppercase letters
    if 'A' <= char <= 'Z':
        base = ord('A')
        return chr((ord(char) - base + k) % 26 + base)
    # lowercase letters
    elif 'a' <= char <= 'z':
        base = ord('a')
        return chr((ord(char) - base + k) % 26 + base)
    #not a letter, just return the letter
    else:
        return char


def caesar_encrypt(text, k):
    encrypted_result = ""
    for c in text:
         encrypted_result += caesar_char(c, k) 
    return encrypted_result



def caesar_decrypt_char(encrypted_char, k):
    if 'A' <= encrypted_char <= 'Z':
        base = ord('A')
        return chr((ord(encrypted_char) - base - k) % 26 + base)
    elif 'a' <= encrypted_char <= 'z':
        base = ord('a')
        return chr((ord(encrypted_char) - base - k) % 26 + base)
    else:
        return encrypted_char


def caesar_decrypt(encrypted_text, k):
    decrypted_result = ""
    for c in encrypted_text:
         decrypted_result += caesar_decrypt_char(c, k) 
    return decrypted_result

    



print(caesar_encrypt("Veni vidi vici", 3))

print(caesar_decrypt("Yhql ylgl ylfl", 3))