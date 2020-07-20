def OverlapGraph(Patterns):
    overlapGraph = {}
    #Creates the empty dictionary 'overlapGraph'
    for pattern in Patterns:
        #Iterates through each of the patterns in the input 'Patterns'.
        overlapGraph[pattern] = []
        #Assigns each pattern as a key in the overlapGraph dictionary and
        #assigns an empty list as the value of that key.
    for key in overlapGraph:
        #Iterates through the keys in overlapGraph.
        key_k = len(key)
        #Determines the length of each key.
        prefix = key[0:key_k-1]
        #Assigns the first n characters of each key/pattern to the variable
        #'prefix', where n is the length of the key minus 1.
        for pattern in Patterns:
            #Iterates through through the input 'Patterns'.
            pattern_k = len(pattern)
            #Determines the length of each pattern.
            suffix = pattern[1:pattern_k]
            #Assigns the final n characters of each pattern to the variable
            #'suffix'.
            if prefix == suffix:
                #Checks to see whether the 'prefix' from the overlapGraph
                #dictionary matches the suffix from a pattern in 'Patterns'.
                overlapGraph[pattern] = key
                #If the prefix matches the suffix, the entry for the pattern
                #is given a value equal to the key from overlapGraph.
    return overlapGraph



patternList = ['GCGA, CAAG, AAGA, GCCG, ACAA, AGTA, TAGG, AGTA, ACGT, AGCC, TTCG, AGTT, AGTA, CGTA, GCGC, GCGA, GGTC, GCAT, AAGC, TAGA, ACAG, TAGA, TCCT, CCCC, GCGC, ATCC, AGTA, AAGA, GCGA, CGTA']
overlapList = OverlapGraph(patternList)
for key in sorted(overlapList):
    # initialize place holder of suffixes (call it text)
    text = ""
    # go through the suffixes stored for each prefix
    for l in overlapList[key]:
    # identifying if you have 1 or more results (and thus if you need a comma)
        if text == "":
            text = text + l
        else:
            text = text + "" + l
    # concatenate this bad girl
    text = key + " -> " + text
    print(text)
