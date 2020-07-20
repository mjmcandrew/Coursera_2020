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
