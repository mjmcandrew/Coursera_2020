def Motifs(Profile, Dna):
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
