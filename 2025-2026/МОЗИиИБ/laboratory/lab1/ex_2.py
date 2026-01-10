#Cipher Atbash

def atbash_char(c):
    # uppercase letters
    if 'A' <= c <= 'Z':
        return chr(ord('Z') - (ord(c) - ord('A')))
    # lowercase letters
    elif 'a' <= c <= 'z':
        return chr(ord('z') - (ord(c) - ord('a')))
    else:
        return c


def atbash_encrypt(text):
    return ''.join(atbash_char(c) for c in text)


# Example
text = input("Enter the text to  incrypt: ")
encrypted = atbash_encrypt(text)
print("Atbash cipher:", encrypted)