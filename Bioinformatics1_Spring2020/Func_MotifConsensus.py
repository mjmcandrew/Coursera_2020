def MotifCount(Motifs):
    count = {}
    #Creates an empty dictionary count that will store the answer.
    kmer_length = len(Motifs[0])
    #Determines the kmer_length based on the length of the first kmer.
    for symbol in "ACGT":
        count[symbol] = []
        #Assigns keys to "A", "C", "G", and "T" with empty list as values.
        for index in range(kmer_length):
             count[symbol].append(0)
             #Assigns a placeholder zero to each index corresponding to the
             #length of the kmers analyzed.
    motif_number = len(Motifs)
    #Determines the number of motifs being analyzed.
    for character in range(motif_number):
        #Refers to the position of a string in a list of strings. E.g. for a
        #list of strings "AAA" "AAG" "AAT", "AAA" would have the character
        #(index) 0, and the for loop below would then iterate through the
        #string "AAA". After that, the character (index) would change to 1, and
        #the for loop below would iterate through the string "AAG".
        for index in range(kmer_length):
            #Refers to the position within the string. So for the first string,
            #this would iterate through position 0, 1, and 2. But you need to
            #assign a variable to actually pick up the string this refers to.
            symbol = Motifs[character][index]
            #Calls the specific letter in the string corresponding to that
            #string (with character) and position (index).
            count[symbol][index] += 1
            #Calls the dictionary count with symbol "A" "C" "G" or "T" assigned
            #above as the key and increases the value stored within the list
            #at that index position by 1.
    return count

def MotifConsensus(Motifs):
    kmer_length = len(Motifs[0])
    #Determines the kmer_length based on the length of the first kmer.
    counts = MotifCount(Motifs)
    #Runs MotifCount on the motifs being analyzed to determine the nucleotide
    #count at each position of each motif. These values will be used to
    #determine the most frequent nucleotide at each position in order
    #to find the consensus motif.
    consensus = ""
    #Creates an empty string consensus which will be added to with the
    #nucleotide appearing most frequently in each column.
    for index in range(kmer_length):
        #Iterates through the indices of each kmer.
        max = 0
        #Sets the maximum value for each column at 0. This value will be replaced
        #with the first nonzero number encountered in the counts.
        frequentSymbol = ""
        #Initializes a string "frequentsymbol" which will be replaced with the
        #most frequent nucleotide at each position as a function of m.
        for nucleotide in "ACGT":
            #Iterates through the keys of the dictionary counts.
            if counts[nucleotide][index] > max:
                #Determines whether the count of a nucleotide at a specific
                #position is greater than the max. Since the max is set to zero
                #at the beginning of each iteration, this will be replaced by
                #the first non-zero number encountered, and subsequently by
                #any count greater than the stored value.
                max = counts[nucleotide][index]
                #Replaces the variable max with a count higher than the one
                #currently stored in max if applicable.
                frequentSymbol = nucleotide
                #Assigns the nucleotide associated with the maximum count to the
                #variable "frequentSymbol".
        consensus += frequentSymbol
        #Adds the nucleotide with the greatest count after iteration to the string
        #'consensus', which is returned as the final product.
    return consensus
