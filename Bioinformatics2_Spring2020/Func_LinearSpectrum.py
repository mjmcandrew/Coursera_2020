def LinearSpectrum(Peptide):
    #Computes the possible linear spectrum of a peptide after mass
    #spectrometry analysis.
    PrefixMass = [0]
    #Initiates the list 'PrefixMass' with a value of 0 at index 0.
    peptide_length = len(Peptide)
    #Sets the variable 'peptide_length' equal to the length of the
    #input 'Peptide'.
    for index in range(peptide_length):
        #Iterates through indices in the range of peptide_length.
        for key in integer_masses:
            #Iterates through keys in the dictionary 'integer_masses'.
            if key == Peptide[index]:
                PrefixMass.append((PrefixMass[index] + integer_masses[key]))
                #Assigns the weight of the peptide up to index to the
                #position index + 1 in PrefixMass (due to the initial
                #0 representing 'no peptide').
    LinearSpectrum = [0]
    #Initiates the list 'LinearSpectrum' with a value of 0 at index 0
    #representing 'no peptide'.
    for index in range(peptide_length):
        #Iterates through indices in the range of peptide_length.
        for iterable in range(index + 1, len(PrefixMass)):
            #Iterates through index + 1 through the length of PrefixMass
            #in order to generate all possible subpeptide masses that
            #can be generated from input 'Peptide'.
            LinearSpectrum.append(PrefixMass[iterable] - PrefixMass[index])
            #Appends the difference of the PrefixMass of iterable minus
            #the PrefixMass of index to the list 'LinearSpectrum'.
    LinearSpectrum = sorted(LinearSpectrum)
    #Sorts the LinearSpectrum data.
    return LinearSpectrum

integer_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}

peptide = 'AQV'

result = LinearSpectrum(peptide)
new_result = []
for value in result:
    new_result.append(str(value))
print(' '.join(new_result))
#result = [0, 71, 99, 101, 103, 128, 129, 199, 200, 204, 227, 230, 231, 298, 303, 328, 330, 332, 333]
#Sample output: 0 113 114 128 129 242 242 257 370 371 484
