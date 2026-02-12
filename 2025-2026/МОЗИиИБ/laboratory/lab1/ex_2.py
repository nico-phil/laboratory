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
    result = ""
    for c in text:
        result += atbash_char(c)
    return result



def atbash_decrypt_char(c):
    # uppercase letters
    if 'A' <= c <= 'Z':
        return chr(ord('Z') + (ord(c) - ord('A')))
    # lowercase letters
    elif 'a' <= c <= 'z':
        return chr(ord('z') + (ord(c) - ord('a')))
    else:
        return c


def atbash_decrypt(text):
    result = ""
    for c in text:
        result += atbash_char(c)
    return result

print(atbash_encrypt("veni vidi vici"))
print(atbash_decrypt("evmr erwr erxr"))
