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
