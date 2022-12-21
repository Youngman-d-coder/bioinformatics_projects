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
    
    # Find the k-mer with the highest count
    most_frequent_kmer = max(kmer_counts, key=kmer_counts.get)
    
    return most_frequent_kmer
