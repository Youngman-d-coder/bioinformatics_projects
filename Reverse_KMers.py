# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    # Initialize an empty string to store the reversed pattern
    rev = ""
    
    # Iterate over the characters in Pattern in reverse order
    for i in range(len(Pattern)-1, -1, -1):
        # Append the character to the beginning of the reversed string
        rev = rev + Pattern[i]
    
    return rev
