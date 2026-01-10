ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
M = len(ALPHABET)

def normalize(text: str) -> str:
    """
    Keep only letters A-Z and make uppercase.
    Used for the KEY (and optionally for plaintext if you want).
    """
    text = text.upper()
    return "".join(ch for ch in text if ch in ALPHABET)

def vigenere_encrypt(plaintext: str, key: str) -> str:
    key = normalize(key)
    if not key:
        raise ValueError("Key must not be empty (must contain A-Z letters).")

    out = []
    j = 0  # index in key (only advances when we encrypt a letter)

    for ch in plaintext:
        up = ch.upper()
        if up in ALPHABET:
            p = ALPHABET.index(up)
            k = ALPHABET.index(key[j % len(key)])
            c = ALPHABET[(p + k) % M]
            out.append(c if ch.isupper() else c.lower())
            j += 1
        else:
            out.append(ch)  # keep punctuation/spaces

    return "".join(out)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    key = normalize(key)
    if not key:
        raise ValueError("Key must not be empty (must contain A-Z letters).")

    out = []
    j = 0

    for ch in ciphertext:
        up = ch.upper()
        if up in ALPHABET:
            c = ALPHABET.index(up)
            k = ALPHABET.index(key[j % len(key)])
            p = ALPHABET[(c - k) % M]
            out.append(p if ch.isupper() else p.lower())
            j += 1
        else:
            out.append(ch)

    return "".join(out)


text = "CRYPTOGRAPHY IS SERIOUS SCIENCE!"
key = "MATHEMATICS"

enc = vigenere_encrypt(text, key)
dec = vigenere_decrypt(enc, key)

print("Plain :", text)
print("Key   :", key)
print("Enc   :", enc)
print("Dec   :", dec)
