def CyclopeptideSequencing(Spectrum):
    #This algorithm generates the sequence of a cyclic peptide given
    #its theoretical spectrum output from a mass spectrometer.
    CandidatePeptides = ['']
    FinalPeptides = []
    FinalMassPeptides = []
    #The above initializes an empty peptide (CandidatePeptides = ['']) which will
    #be continuously expanded and pruned as well as two empty lists which will
    #be used to store peptides which match the input spectrum.
    while CandidatePeptides:
        #Initializes a while loop that will run as long as there are candidate
        #peptides to test.
        CandidatePeptides = expandPeptides(CandidatePeptides, Spectrum)
        #Utilizes expandPeptides to add a single amino acid to current
        #candidate peptides.
        nonMatchingPeptides = []
        #Initializes the new list 'nonMatchingPeptides', which will be used
        #to store peptides not meeting the below criteria. This prevents modification
        #of the CandidatePeptides list as we are iterating through it.
        for peptide in CandidatePeptides:
            #Iterates through candidate peptides.
            peptide_mass = calculateMass(peptide)
            #Utilizes calculateMass to find the mass of current candidate.
            if peptide_mass in Spectrum:
                if peptide_mass == Spectrum[-1]:
                    #The above lines first check whether the mass of the candidate
                    #is present in the input spectrum. If so, it next checks
                    #whether the mass is equal to the parent mass (the total mass of
                    #the peptide represented by input spectrum).
                    candidate_spectrum = CyclicSpectrum(peptide)
                    #Generates the cyclic spectrum of the candidate peptide.
                    if candidate_spectrum == Spectrum and peptide not in FinalPeptides:
                        #If the cyclic spectrum matches the input spectrum, and the
                        #peptide has not already been marked as a match, it is added
                        #to FinalPeptides and removed from further consideration
                        #by its addition to nonMatchingPeptides.
                        FinalPeptides.append(peptide)
                        nonMatchingPeptides.append(peptide)
            else:
                #If the peptide's mass is not present in the input spectrum,
                #the peptide is added to nonMatchingPeptides to remove it from
                #further consideration.
                nonMatchingPeptides.append(peptide)
        CandidatePeptides = [peptide for peptide in CandidatePeptides if peptide not in nonMatchingPeptides]
        #At the conclusion of testing of each round of new candidate peptides,
        #candidate peptides is pruned to remove any peptides which were added
        #to nonMatchingPeptides. Note that this step is probably very inefficient
        #and could probably be replaced by something more clever.
    for peptide in FinalPeptides:
        #Since there are two pairs of amino acids which have the same mass,
        #we only want to consider the mass identity of matching peptides and not
        #their symbolic representations. This final portion converts each
        #peptide symbol string into a string of masses and returns them. Note
        #that this step is inefficient as well, since we will have a number of
        #duplicates (in terms of mass) present in FinalPeptides, if these peptides
        #contain I/L or K/Q. It would be more efficient to simply produce the
        #peptides as strings of masses from the start, but it would make
        #formatting and checks in the above algorithm more difficult.
        mass_peptide = peptideToMassConverter(peptide)
        if mass_peptide not in FinalMassPeptides:
            FinalMassPeptides.append(mass_peptide)
    return FinalMassPeptides

def expandPeptides(peptides, spectrum):
    #This algorithm expands a list of candidate peptides by adding an amino
    #acid to the final position in the string. Note that, with no restrictions,
    #input of 'A' would result in output 'AG', 'AA', 'AS', etc. However,
    #this algorithm first determines whether the mass of the single amino acid
    #being added is present in the input spectrum. If the mass is not present
    #in the spectrum, it must not be present in the final peptide, and thus
    #it should not be present in a candidate peptide.
    expandedPeptides = []
    #Initializes the empty list 'expandedPeptides'.
    for peptide in peptides:
        #Iterates through input peptides.
        for key in integer_masses:
            #Iterates through amino acids present in the 'integer_masses'
            #dictionary.
            if integer_masses[key] in spectrum:
                branched_peptide = peptide + key
                expandedPeptides.append(branched_peptide)
                #As described above, if the mass of the amino acid is present in
                #spectrum, this amino acid is added to the candidate peptide,
                #and this new peptide is added to expandedPeptides.
    return expandedPeptides

def calculateMass(peptide):
    #This algorithm computes the mass of a given peptide based on
    #the mass in daltons of its component amino acids. Note: requires
    #the dictionary 'integer_masses' which stores each of the symbols
    #for the 20 amino acids with mass in daltons as the value for that key.
    peptide_mass = 0
    for index in range(len(peptide)):
        peptide_mass += integer_masses[peptide[index]]
    return peptide_mass

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

def CyclicSpectrum(Peptide):
    #Computes the possible cyclic spectrum of a peptide after mass
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
    peptideMass = PrefixMass[peptide_length]
    CyclicSpectrum = [0]
    for index in range(peptide_length):
        #Iterates through indices in the range of peptide_length.
        for iterable in range(index + 1, len(PrefixMass)):
            #Iterates through index + 1 through the length of PrefixMass
            #in order to generate all possible subpeptide masses that
            #can be generated from input 'Peptide'.
            CyclicSpectrum.append(PrefixMass[iterable] - PrefixMass[index])
            #Appends the difference of the PrefixMass of iterable minus
            #the PrefixMass of index to the list 'LinearSpectrum'.
            if index > 0 and iterable < peptide_length:
                CyclicSpectrum.append(peptideMass - (PrefixMass[iterable] - PrefixMass[index]))
    CyclicSpectrum = sorted(CyclicSpectrum)
    return CyclicSpectrum

def peptideToMassConverter(peptide):
    #This algorithm takes a symbolic peptide string (e.g. 'GAS') and returns
    #its representation as a string of masses (i.e. '57-71-87').
    peptide_length = len(peptide)
    #Determines the length of the input peptide.
    mass_list = []
    #Initializes an empty list 'mass_list'.
    for index in range(peptide_length):
        #Iterates through the peptide string.
        aa_mass = integer_masses[peptide[index]]
        #Finds the mass of the amino acid present at the current index.
        mass_list.append(str(aa_mass))
        #Adds the string representation of this integer mass to mass_list.
    mass_peptide = '-'.join(mass_list)
    #Uses join to convert the mass_list (e.g. ['57', '71', '87']) to a string
    #of masses (e.g. '57-71-87').
    return mass_peptide

integer_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}


spectrum = [0, 71, 101, 113, 131, 184, 202, 214, 232, 285, 303, 315, 345, 416]

result = CyclopeptideSequencing(spectrum)
print(' '.join(result))
