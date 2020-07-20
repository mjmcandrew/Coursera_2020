def NumberToPattern(index, kLength):
    base4string = {}       # This creates the dictionary that will be used to convert
    base4string[0] = 'A'   # a base 4 number to a DNA string.
    base4string[1] = 'C'
    base4string[2] = 'G'
    base4string[3] = 'T'
    remainder = 0
    base4pattern = ''
    count = 0
    while count < kLength:
        quotient = int(index / 4)
        remainder = int(index % 4)
        base4pattern = base4string[remainder] + base4pattern
        count += 1
        index = quotient
    return base4pattern
