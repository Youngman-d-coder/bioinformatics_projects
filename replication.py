def ReverseComplement(Pattern):
    # First, find the complement of the pattern
    complement = Complement(Pattern)
    
    # Then, reverse the complement
    rev_complement = Reverse(complement)
    
    return rev_complement

def Complement(Pattern):
    # Initialize an empty string to store the complement
    complement = ""
    
    # Iterate over the characters in Pattern
    for char in Pattern:
        # Replace each character with its complement
        if char == "A":
            complement += "T"
        elif char == "T":
            complement += "A"
        elif char == "C":
            complement += "G"
        elif char == "G":
            complement += "C"
    
    return complement

def Reverse(Pattern):
    # Initialize an empty string to store the reversed pattern
    rev = ""
    
    # Iterate over the characters in Pattern in reverse order
    for i in range(len(Pattern)-1, -1, -1):
        # Append the character to the beginning of the reversed string
        rev = rev + Pattern[i]
    
    return rev
