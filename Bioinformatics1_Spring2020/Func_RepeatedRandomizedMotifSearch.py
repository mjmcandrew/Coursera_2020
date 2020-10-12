import random

def RepeatedRandomizedMotifSearch(Dna, k, t, N):
    #Uses the same logic of RandomizedMotifSearch to perform the
    #RandomizedMotifSearch N times.
    BestScore = float('inf')
    BestMotifs = []
    for i in range(N + 1):
        Motifs = RandomizedMotifSearch(Dna, k, t)
        CurrentScore = MotifScore(Motifs)
        if CurrentScore < BestScore:
            BestScore = CurrentScore
            BestMotifs = Motifs
    return BestMotifs

def RandomizedMotifSearch(Dna, k, t):
    random_motifs = RandomMotifs(Dna, k, t)
    #Creates a set of random motifs taken from each string in Dna.
    BestMotifs = random_motifs
    while True:
        Profile = MotifProfileWithPseudocounts(random_motifs)
        random_motifs = MotifsFinder(Profile, Dna)
        if MotifScore(random_motifs) < MotifScore(BestMotifs):
            BestMotifs = random_motifs
        else:
            return BestMotifs

def RandomMotifs(Dna, k, t):
    import random
    RandomMotifs = []
    #Creates the empty set 'RandomMotifs'.
    for Dna_string in Dna:
        #Iterates through the strings in 'Dna'.
        random_index = random.randint(0, (len(Dna_string) - k))
        #Generates a random index that will serve as a starting point
        #allowing for the length of desired kmer.
        random_motif = Dna_string[random_index:random_index+k]
        #Generates a random motif using the random index as the starting
        #point and allows for the length of k.
        RandomMotifs.append(random_motif)
        #Adds randomly generated motif to set 'RandomMotifs'.
    return RandomMotifs

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
    motif_number = len(Motifs)
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

def MotifsFinder(Profile, Dna):
    k = len(Profile['A'])
    #Sets 'k' (which will be used in the ProfileMostProbableKmer function)
    #equal to the length of the first list (corresponding to the key 'A')
    #in the provided profile
    Motifs = []
    #Creates the empty list Motifs that will store our profile most
    #probable kmers for each of the strings in 'Dna'.
    for Dna_string in Dna:
        #Iterates through the strings in 'Dna'.
        most_probable_kmer = ProfileMostProbableKmer(Dna_string, k, Profile)
        #Determines the most probable kmer from each string based on the
        #profile provided.
        Motifs.append(most_probable_kmer)
        #Appends the most probable kmer to the list 'Motifs'.
    return Motifs

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
