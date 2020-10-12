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
