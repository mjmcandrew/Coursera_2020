import random

def WeightedDie(Probabilities):
    NormalizedProbabilities = Normalize(Probabilities)
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
