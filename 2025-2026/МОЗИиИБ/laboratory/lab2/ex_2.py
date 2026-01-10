ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def normalize(text: str) -> str:
    text = text.upper()
    return "".join(ch for ch in text if ch in ALPHABET)

def rotate90(holes, n):
    # (r, c) -> (c, n-1-r)
    return [(c, n - 1 - r) for (r, c) in holes]

def fleissner_grille_encrypt(plaintext: str, n: int, holes, pad: str = "X") -> str:
    if n % 2 != 0:
        raise ValueError("n must be even (2k).")

    pt = normalize(plaintext)
    needed = n * n
    pt = pt.ljust(needed, pad)

    grid = [["." for _ in range(n)] for _ in range(n)]

    pos = 0
    current = holes[:]

    for _ in range(4):
        for (r, c) in current:
            if grid[r][c] != ".":
                raise ValueError(
                    f"Cell ({r},{c}) already filled. Grille is not valid; some cells are used more than once."
                )
            grid[r][c] = pt[pos]
            pos += 1
        current = rotate90(current, n)

    return "".join("".join(row) for row in grid)

def print_grid(s: str, n: int):
    for i in range(0, n*n, n):
        print(s[i:i+n])


n = 4
holes_4x4 = [(0, 0), (0, 1), (0, 2), (1, 1)]  

text = "HELLOFLEISSNERGRILLE"  # will be normalized and padded/truncated to 16 chars
cipher = fleissner_grille_encrypt(text, n, holes_4x4)

print("Ciphertext (row-wise):", cipher)
print("\nGrid view:")
print_grid(cipher, n)
