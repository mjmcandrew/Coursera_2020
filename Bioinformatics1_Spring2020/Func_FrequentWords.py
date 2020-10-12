def FrequentWords(Text, k):
    #Utilizes the FrequencyMap to find the pattern(s) of length 'k' which
    #appears most frequently in the string 'Text'.
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    #Finds maximum value(s) in FrequencyMap.
    for Pattern in freq:
        if freq[Pattern] == m:
            words.append(Pattern)
        #Appends patterns with a count equal to the maximum to the list
        #'words'. Note that multiple patterns may be returned if they have
        #a count equal to maximum.
    return words

def FrequencyMap(Text, k):
    #Returns a dictionary containing patterns of length 'k' as keys, with
    #the number of times the pattern appears in 'Text' as values.
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        #Iterates through indices in 'Text' while accounting for the length
        #of 'k'.
        Pattern = Text[i:i+k]
        if Pattern not in freq:
            #If a new pattern is discovered, it is added to dictionary 'freq'
            #with count 1.
            freq[Pattern] = 1
        else:
            #If a previously added pattern is encountered, its count is
            #increased by 1.
            freq[Pattern] += 1
    return freq
