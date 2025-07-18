def NaiveAlgorithm(pattern, text):
    m = len(pattern)
    n = len(text)
    
    for i in range(n - m + 1):
        j = 0
        
        while j < m and text[i + j] == pattern[j]:
            j += 1
        
        if j == m:
            print(f"Pattern found at index {i}")
    

if __name__ == "__main__":
    # Example 1
    text1 = "AABAACAADAABAABA"
    pattern1 = "AABA"
    print("Example 1:", NaiveAlgorithm(pattern1, text1))
    
    # Example 2
    text2 = "agd"
    pattern2 = "g"
    print("\nExample 2:", NaiveAlgorithm(pattern2, text2))
    