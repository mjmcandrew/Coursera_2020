def NumberToPattern(index, kLength):
    base4string = {}
    base4string[0] = 'A'
    base4string[1] = 'C'
    base4string[2] = 'G'
    base4string[3] = 'T'
    #The above lines create a dictionary that will be used to convert
    #numbers to DNA strings.
    remainder = 0
    base4pattern = ''
    count = 0
    while count < kLength:
        quotient = int(index / 4)
        remainder = int(index % 4)
        base4pattern = base4string[remainder] + base4pattern
        count += 1
        index = quotient
    #The above portion of the algorithm iteratively divides the number
    #representing a pattern by 4 and adds the character represented by
    #the remainder to the pattern string. In essence, this is algorithm
    #converts a base4 number back to a string of nucleotides.
    return base4pattern
