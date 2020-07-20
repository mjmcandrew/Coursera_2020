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

def MotifProfile(Motifs):
    profile = {}
    #Creates an empty dictionary profile that will store the counts determined
    #by MotifCount by the total kmer count, which should give the frequency
    #of each nucleotide at a given position.
    kmer_length = len(Motifs[0])
    #Determines the kmer_length based on the length of the first kmer.
    for symbol in "ACGT":
        profile[symbol] = []
        #Assigns keys to "A", "C", "G", and "T" with empty list as values.
        for index in range(kmer_length):
             profile[symbol].append(0)
             #Assigns a placeholder zero to each index corresponding to the
             #length of the kmers analyzed.
    motif_number = float(len(Motifs))
    print 'motif_number is', motif_number
    #Determines the number of motifs being analyzed. We will use this value to
    #determine the frequency of any nucleotide at a given position.
    counts = MotifCount(Motifs)
    print 'counts are', counts
    #Runs MotifCount on the motifs being analyzed to determine the nucleotide
    #count at each position of each motif. These values will be divided by
    #motif_number in order to determine the frequency of each nucleotide.
    for nucleotide in counts:
        print "nucleotide is", nucleotide
        #Iterates through the keys "A", "C", "G", "T" in counts.
        for index in range(kmer_length):
            print 'index is', index
            #Iterates through the index positions of the list of values assigned
            #to each key.
            value = float(counts[nucleotide][index])
            print 'value is', value
            #Assigns a variable "value" to the actual count contained in each of
            #the lists in counts (provided by MotifCount).
            frequency = value / motif_number
            print 'frequency is', frequency
            #Divides the count assigned above by the motif number, which yields
            #the frequency of each nucleotide at that position in a given list
            #of kmer strings.
            profile[nucleotide][index] = frequency
            print profile[nucleotide][index]
            #Replaces the placeholder zeros in profile with the value of
            #frequency at the correct position.
    return profile

print MotifProfile(['TGA', 'GTT', 'GAA', 'TGT'])
