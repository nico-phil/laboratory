import math

# key = "пароль"



def findIndex(c, original_string):
    index = original_string.find(c)
    return index


def encrypt(original_string:str, key: str) -> str:
    original_string = original_string.replace(" ","")
    original_string = original_string.upper()
    cols = len(key)
    rows = math.ceil(len(original_string) / cols)
    
    grid = [""] * rows
    for i in range(rows):
        grid[i] = [""] * cols
        
 
    grid = AddOriginalStringToGrid(original_string, rows, cols, grid)
   

    sortedKeyArr = sorted(key)
    encryptedResult = ""
    for ch in sortedKeyArr:
        index = findIndex(ch, key)
        result = findEncryptChars(rows, index, grid)
        encryptedResult += result

    return encryptedResult



def AddOriginalStringToGrid(original_string, rows, cols, grid):
    charIndex = 0
    
    for  i in range (rows):
        for  j in range (cols):
            if charIndex == len(original_string):
                break
            grid[i][j] = original_string[charIndex]
            charIndex += 1

    for i in range (rows):
        for j in range (cols):
            if grid[i][j] == "":
                grid[i][j] = "X"
    return grid
   

def findEncryptChars(rows, colIndex, grid):
    result = ""
    for i in range (rows):
        result += grid[i][colIndex]
    return result


print(encrypt("нельзя недооценивать противника", "пароль"))