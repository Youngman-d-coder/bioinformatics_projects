def find_most_frequent_kmer(string, k):
    # Initialize a dictionary to store the k-mers and their counts
    kmer_counts = {}
    
    # Split the string into k-mers by sliding a window of size k along the string
    for i in range(len(string) - k + 1):
        kmer = string[i:i+k]
        
        # Increment the count for the k-mer in the dictionary
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
    
    # Initialize a list to store the k-mers and their counts
    kmer_list = []
    
    # Iterate over the k-mer counts dictionary and append each k-mer and count to the list
    for kmer, count in kmer_counts.items():
        kmer_list.append((kmer, count))
    
    # Sort the list by the counts in descending order
    kmer_list.sort(key=lambda x: x[1], reverse=True)
    
    return kmer_list
