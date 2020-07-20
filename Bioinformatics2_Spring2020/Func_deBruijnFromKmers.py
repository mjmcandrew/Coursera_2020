def deBruijnFromKmers(Patterns):
    deBruijnGraph = {}
    #Creates the empty dictionary deBruijnGraph.
    for pattern in Patterns:
        #Iterates through patterns in the input 'Patterns'.
        k_length = len(pattern)
        #Sets k_length equal to the length of the pattern.
        suffix = pattern[1:]
        #Sets the variable 'suffix' equal to the second through final character in the string 'pattern'.
        prefix = pattern[0: k_length - 1]
        #Sets the variable 'prefix' equal to the first through the penultimate character in the string
        #'pattern'.
        if prefix not in deBruijnGraph:
            deBruijnGraph[prefix] = []
            #Creates an empty list as a value assigned to the key for the specified prefix.
            deBruijnGraph[prefix].append(suffix)
            #Adds the pattern's suffix to the list value associated with this prefix key.
        else:
            deBruijnGraph[prefix].append(suffix)
            #If the prefix key already exists in the dictionary, this simply appends the suffix that follows.
    return deBruijnGraph

#import sys
#if __name__ == "__main__":
    #Input = sys.stdin.readlines()
    #patterns = [pattern.strip() for pattern in Input]
patterns = []
deBruijnResult = deBruijnFromKmers(patterns)
for key, value in deBruijnResult.items():
    print key + ' -> ' + ','.join(map(str, value))
#for key, value in deBruijnResult.items():
    #print key
    #print(key + ' -> ' + ','.join(map(str, value)))
