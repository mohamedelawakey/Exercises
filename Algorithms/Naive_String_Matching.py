def NaiveStringMatching(pattern, text):
    m = len(pattern)
    n = len(text)
    pos = 0
    
    while pos <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[pos + j]:
            j -= 1
        
        if j < 0:
            print(f"Pattern found at position {pos}")

        pos += 1

text = "Haystack with a needle"
pattern = "days"

NaiveStringMatching(text, pattern)