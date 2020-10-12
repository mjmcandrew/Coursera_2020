def GreedyMotifSearchWithPseudocounts(Dna, k, t):
    BestMotifs = []
    #Initializes an empty list of the best motifs found in the list of
    #strings 'Dna'.
    for index in range(0, t):
        #Iterates through the list of strings 'Dna' (with 0 corresponding
        #to the first string and t corresponding to the total number
        #of strings).
        BestMotifs.append(Dna[index][0:k])
        #Fills the list 'BestMotifs' with the kmers of length k that occur at
        #the beginning of each DNA string. For instance, given 'Dna' =
        #'AAG', 'ATA', 'ACA', 'TGA', and 'GAT' with k = 2 and t = 5 (total
        #number of strings in Dna), 'BestMotifs' would return ['AA', 'AT', 'AC',
        #'TG', 'GA'].
    n = len(Dna[0])
    #Sets the length to range through equal to the length of the first string
    #in 'Dna'.
    for index in range(n-k+1):
        #Iterates through the first string in 'Dna'.
        Motifs = []
        #Creates the empty list 'Motifs' where potential best motifs will
        #be stored.
        Motifs.append(Dna[0][index:index+k])
        #Inserts the first kmer of length k in the first string of 'Dna'
        #into the list 'Motifs'
        for string in range(1, t):
            #Iterates through the remaining strings in 'DNA'.
            motif_profile = MotifProfileWithPseudocounts(Motifs[0:string])
            #Calls MotifProfile to create a motif profile for each of the
            #strings in 'Dna'.
            Motifs.append(ProfileMostProbableKmer(Dna[string], k, motif_profile))
            #Determines the most probable kmer of size k in each string
            #from 'Dna' based on the profile generated above.
        if MotifScore(Motifs) < MotifScore(BestMotifs):
            #Checks whether the score of the potential motifs identified above
            #is lower than the current score of BestMotifs.
            BestMotifs = Motifs
            #If this is the case, the motifs identified above replace
            #'BestMotifs'.
    return BestMotifs

def MotifProfileWithPseudocounts(Motifs):
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
    #Determines the number of motifs being analyzed. We will use this value to
    #determine the frequency of any nucleotide at a given position.
    counts = MotifCountWithPseudocounts(Motifs)
    #Runs MotifCount on the motifs being analyzed to determine the nucleotide
    #count at each position of each motif. These values will be divided by
    #motif_number in order to determine the frequency of each nucleotide.
    for nucleotide in counts:
        #Iterates through the keys "A", "C", "G", "T" in counts.
        for index in range(kmer_length):
            #Iterates through the index positions of the list of values assigned
            #to each key.
            value = float(counts[nucleotide][index])
            #Assigns a variable "value" to the actual count contained in each of
            #the lists in counts (provided by MotifCount).
            frequency = value / float((motif_number + 4))
            #Divides the count assigned above by the motif number + 4
            #(one for each nucelotide due to pseudocounts) which yields
            #the frequency of each nucleotide at that position in a given list
            #of kmer strings. Another approach would be to total the counts
            #in each column, which would require a loop that would look at
            #key1[0] + key2[0] + key3[0] + key4[0], but the 4 can be a constant
            #in this particular case. The constant would simply need to be updated
            #if the number of possible keys in the dictionary changed.
            profile[nucleotide][index] = frequency
            #Replaces the placeholder zeros in profile with the value of
            #frequency at the correct position.
    return profile

def MotifCountWithPseudocounts(Motifs):
    motif_number = len(Motifs)
    #Determines the number of motifs being analyzed.
    motif_length = len(Motifs[0])
    #Determines the motif_length based on the length of the first motif.
    count = {}
    #Creates an empty dictionary count that will store the answer.
    for symbol in "ACGT":
        count[symbol] = []
        #Assigns keys to "A", "C", "G", and "T" with empty list as values.
        for index in range(motif_length):
             count[symbol].append(1)
             #Assigns a placeholder one (for pseudocount) to each index corresponding to the
             #length of the motifs analyzed.
    for character in range(motif_number):
        #Refers to the position of a string in a list of strings. E.g. for a
        #list of strings "AAA" "AAG" "AAT", "AAA" would have the character
        #(index) 0, and the for loop below would then iterate through the
        #string "AAA". After that, the character (index) would change to 1, and
        #the for loop below would iterate through the string "AAG".
        for index in range(motif_length):
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
    counts = MotifCountWithPseudocounts(Motifs)
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

def MotifScore(Motifs):
    motif_score = 0
    #Sets motif score equal to 0.
    kmer_length = len(Motifs[0])
    #Determines the kmer_length based on the length of the first kmer.
    motif_number = len(Motifs)
    consensus = MotifConsensus(Motifs)
    #Finds consensus motif sequence using MotifConsensus algorithm.
    for character in range(motif_number):
        #Iterates through each string in the list of strings 'Motifs'.
        for index in range(len(consensus)):
            #Iterates through each index position in an individual motif.
            symbol = Motifs[character][index]
            #Identifies the nucleotide associated with the index position
            #defined above in a given string from 'Motifs'
            consensus_symbol = consensus[index]
            #Assigns the nucleotide at the corresponding position within
            #the consensus string to variable 'consensus_symbol'.
            if symbol != consensus_symbol:
                motif_score += 1
            #If the nucleotide within a given string in a set of strings
            #'Motifs' does not match the consensus nucleotide, increments
            #the motif score by 1.
    return motif_score

def MotifProbability(Text, Profile):
    probability = 1
    #Sets initial probability value equal to 1.
    for index in range(len(Text)):
        #Iterates through each index in the string provided
        #in 'Text'.
        nucleotide = Text[index]
        #Accesses the nucleotide present at a given index in
        #'Text' and assigns it to variable 'nucelotide'.
        frequency = Profile[nucleotide][index]
        #Finds the frequency value of the nucleotide at the
        #given position within 'Text' at that specific index
        #position within the dictionary 'Profile'.
        probability = probability * frequency
        #Updates the probability score by multiplying times
        #the frequency score stored in 'Profile'.
    return probability

def ProfileMostProbableKmer(text, k, profile):
    probability = 0
    #Sets initial probability value equal to 0.
    most_prob_kmer = text[0:k]
    #Sets initial most probable kmer to the first kmer occurring in text.
    #Note that a failure to do this and use empty string notation ''
    #allows for the possibility of 'text' where all kmer scores have a
    #probability of 0, and thus the output is an empty string. This step
    #prevents this possibility, though it may return a false positive.
    n = len(text)
    for index in range(n-k+1):
        #Iterates through a range the length of the text minus the size
        #of the kmer (+1 to account for zero indexing).
        Pattern = text[index:index+k]
        #Sets 'Pattern' to the appropriately sized string of nucleotides
        #from 'text' based on k.
        motif_probability = MotifProbability(Pattern, profile)
        #Calls MotifProbability to calculate the probability of a given
        #pattern based on the provided frequency profile.
        if motif_probability > probability:
            #Compares the probability of the most recent pattern to the
            #stored probability value.
            probability = motif_probability
            #If probability of the most recent pattern is greater than that
            #of the stored value, replaces probability with this value.
            most_prob_kmer = Pattern
            #If above conditions are met, 'most_prob_kmer' is replaced with
            #the current pattern being analyzed.
    return most_prob_kmer
