def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    array[0] = PatternCount(Genome[0:n//2], symbol)
    for index in range(1, n):
        array[index] = array[index-1]
        if ExtendedGenome[index-1] == symbol:
            array[index] = array[index]-1
        if ExtendedGenome[index+(n//2)-1] == symbol:
            array[index] = array[index]+1
    return array

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))
