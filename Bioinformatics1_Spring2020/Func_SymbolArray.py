def SymbolArray(Genome, symbol):
    #This algorithm allows a user to extend a linear string 'Genome' by a
    #length of one-half of genome-length in order to look for frequent patterns
    #which may occur in a circular genome.
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array

def PatternCount(Text, Pattern):
    #Counts the number of times input 'Pattern' appears in string 'Text'
    #by iterating through text.
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        #Iterates through each index in 'Pattern' while accounting
        #for Pattern length.
        if Text[i:i+len(Pattern)] == Pattern:
            #Assessess the string beginning with index that is of
            #the same length as Pattern.
            count = count+1
            #If the string of the same length as Pattern is equal to
            #the input Pattern, the PatternCount is increased.
    return count
