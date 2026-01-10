#Cipher Cesear

def caesar_char(c, k):
    #uppercase letters
    if 'A' <= c <= 'Z':
        base = ord('A')
        return chr((ord(c) - base + k) % 26 + base)
    # lowercase letters
    elif 'a' <= c <= 'z':
        base = ord('a')
        return chr((ord(c) - base + k) % 26 + base)
    #not a letter, just return c
    else:
        return c 


def caesar_encrypt(text, k):
    return ''.join(caesar_char(c, k) for c in text)


# Example
text = input("Write the text to encrypt: ")
k = int(input("Write the key(number): "))

encrypted = caesar_encrypt(text, k)
print("Ceasar cipher:", encrypted)