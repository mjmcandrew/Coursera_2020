def GibbsSampler(Dna, k, t, N):
    import random
    BestMotifs = []
    #Creates the empty list 'BestMotifs'.
    randomMotifs = RandomMotifs(Dna, k, t)
    #Creates random motifs from the input strings provided in 'Dna' using the
    #RandomMotifs function.
    BestMotifs = randomMotifs
    #Sets BestMotifs equal to randomMotifs generated.
    for attempt in range(N + 1):
        #Ranges through the number of attempts remaining.
        random_int = random.randint(0, t - 1)
        #Creates a random integer from 0 to the number of strings in 'Dna' (based
        #on indexing).
        reduced_motifs = []
        #Generates the empty list 'reduced_motifs'.
        for index in range(len(BestMotifs)):
            #Iterates through the motifs in 'BestMotifs'.
            if index != random_int:
                #Checks whether the index of the motif is equal to the random
                #integer.
                reduced_motifs.append(BestMotifs[index])
                #If it is not, the motif is added to the reduced_motifs.
        Profile = MotifProfileWithPseudocounts(reduced_motifs)
        #Generates a profile of the motifs (- 1) from BestMotifs.
        random_kmer = ProfileGeneratedString(Dna[random_int], Profile, k)
        #Generates a random kmer from the excluded DNA string.
        reduced_motifs.insert(random_int, random_kmer)
        #Adds this kmer to reduced_motifs at the correct index position.
        if Score(reduced_motifs) < Score(BestMotifs):
            BestMotifs = reduced_motifs
            #If the motif score of the current iteration of random_motifs is
            #better than the current score of BestMotifs, replaces BestMotifs
            #with reduced_motifs.
    return BestMotifs

# place all subroutines needed for GibbsSampler below this line
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

def WeightedDie(Probabilities):
    import random
    NormalizedProbabilities = NormalizeProbabilities(Probabilities)
    #Normalizes initial set of Probabilities.
    random_float = random.uniform(0, 1)
    #Assigns a random float value to the variable 'random_float'. This value
    #will be used to randomly select a kmer allowing for weighted probability.
    for kmer in NormalizedProbabilities:
        #Iterates through kmer keys in the normalized dictionary.
        random_float -= Probabilities[kmer]
        #Subtracts the value of the kmers probability from the value of
        #random_float.
        if random_float <= 0:
            return kmer
            #When this value reaches or goes below zero, we have selected a kmer
            #randomly with respect to probability.

def NormalizeProbabilities(Probabilities):
    NormalizedProbabilities = {}
    #Creates a new dictionary which will contain our normalized probabilities
    #for each key in Probabilities.
    total = 0
    #Initializes the 'total' variable that will keep a running sum of
    #unnormalized probabilities.
    for kmer in Probabilities:
        NormalizedProbabilities[kmer] = 0
        #Iterates through the kmers contained in Probabilities and adds them
        #as keys to our normalized dictionary with a value of 0.
    for key in Probabilities:
        total += Probabilities[key]
        #Keeps a running sum of the total probability in Probabilities.
    for key in Probabilities:
        NormalizedProbabilities[key] = Probabilities[key] / total
        #Provides the normalized probabilities by dividing each value in
        #Probabilities by the total probability.
    return NormalizedProbabilities

def ProfileGeneratedString(Text, profile, k):
    import random
    string_length = len(Text)
    #Sets string_length equal to the length of input 'Text'.
    probabilities = {}
    #Creates the empty dictionary 'probabilities'.
    for index in range(string_length - k + 1):
        #Iterates through all index positions in 'Text' allowing for length of k.
        probabilities[Text[index:index+k]] = MotifProbability(Text[index:index+k], profile)
        #Computes the probability of each kmer in 'Text' and adds those probabilities
        #as values to the dictionary probabilities where the key is the kmer.
    probabilities = NormalizeProbabilities(probabilities)
    #Normalizes the probabilities, then runs WeightedDie on probabilities to randomly select
    #a possible kmer from the intial string allowing for probability.
    return WeightedDie(probabilities)

def RandomMotifs(Dna, k, t):
    import random
    RandomMotifs = []
    #Creates the empty set 'RandomMotifs'.
    for Dna_string in Dna:
        #Iterates through the strings in 'Dna'
        random_index = random.randint(0, (len(Dna_string) - k))
        #Generates a random index that will serve as a starting point
        #allowing for the length of desired kmer.
        random_motif = Dna_string[random_index:random_index+k]
        #Generates a random motif using the random index as the starting
        #point and allows for the length of k.
        RandomMotifs.append(random_motif)
        #Adds randomly generated motif to set 'RandomMotifs'.
    return RandomMotifs

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

def Score(Motifs):
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

for i in range(20):
    m = GibbsSampler(Dna, k, t, N)
    print m
    print Score(m), Score(BestMotifs)
    if Score(m) < Score(BestMotifs):
        BestMotifs = m
        print 'New BestMotifs are:', BestMotifs

for motif in BestMotifs:
    print motif
