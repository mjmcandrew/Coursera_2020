def StringComposition(Text, k):
    #This algorithm returns all patterns of length 'k' present in input
    #'Text' sorted lexographically.
    string_length = len(Text)
    kmer_list = []
    for index in range(string_length - k + 1):
        kmer = Text[index:index + k]
        kmer_list.append(kmer)
    kmer_list.sort()
    return kmer_list
