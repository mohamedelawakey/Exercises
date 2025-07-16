def build_shift_table(pattern):
    m = len(pattern)
    D = {}
    
    for i in range(256):
        D[chr(i)] = m
    
    for i in range(m - 1):
        D[pattern[i]] = m - i - 1
    
    return D

def BMH(text, pattern):
    n = len(text)
    m = len(pattern)
    D = build_shift_table(pattern)
    pos = 0
    
    while pos <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[pos + j]:
            j -= 1
        
        if j < 0:
            print(f"Occurrence found at position {pos}")
            pos += 1
        else:
            shift_char = text[pos + m - 1]
            pos += D.get(shift_char, m)

text = "Haystackwithaneedleinahighstack"
pattern = "needle"
BMH(text, pattern)