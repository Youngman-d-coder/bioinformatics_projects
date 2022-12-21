def Complement(Pattern):
    # your code here
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
