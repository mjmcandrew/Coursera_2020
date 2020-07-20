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
