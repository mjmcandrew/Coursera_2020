'''def CountingPeptidesGivenMass(m):
    if m < 0:
        return 0
    if m == 0:
        return 1
    elif m < 57:
        return 0
    else:

    #CandidatePeptides = ['']
    #print('Initial candidate peptides are: ', CandidatePeptides)
    #FinalPeptides = []
    #print('Initial final peptides are: ', FinalPeptides)
    #FinalMassPeptides = []
    #print('Initial final mass peptides are: ', FinalMassPeptides)
    #while CandidatePeptides:
        #CandidatePeptides = expandPeptides(CandidatePeptides)
        #print('Candidate peptides expanded. Current candidate peptides are: ', CandidatePeptides)
        #nonMatchingPeptides = []
        #for peptide in CandidatePeptides:
            #print('current peptide is: ', peptide)
            #peptide_mass = calculateMass(peptide)
            #print('current peptide mass is: ', peptide_mass)
            #if peptide_mass == m:
                #print('peptide mass is equal to input mass! adding to FinalPeptides...')
                #FinalPeptides.append(peptide)
                #nonMatchingPeptides.append(peptide)
            #elif peptide_mass < m:
                #print('peptide mass is less than input mass! continue to consider...')
                #continue
            #else:
                #print('peptide mass is greater than input mass! discarding...')
                #nonMatchingPeptides.append(peptide)
        #CandidatePeptides = [peptide for peptide in CandidatePeptides if peptide not in nonMatchingPeptides]
        #print('new candidate peptides to expand are: ', CandidatePeptides)
    #print('FinalPeptides are: ', FinalPeptides)
    #for peptide in FinalPeptides:
        #mass_peptide = peptideToMassConverter(peptide)
        #if mass_peptide not in FinalMassPeptides:
            #FinalMassPeptides.append(mass_peptide)
    #print('FinalMassPeptides are: ', FinalMassPeptides)
    #count = len(FinalMassPeptides)
    return peptide_count'''

def expandPeptides(peptides):
    expandedPeptides = []
    for peptide in peptides:
        for key in integer_masses:
            branched_peptide = peptide + key
            expandedPeptides.append(branched_peptide)
    return expandedPeptides

def calculateMass(peptide):
    peptide_mass = 0
    for index in range(len(peptide)):
        peptide_mass += integer_masses[peptide[index]]
    return peptide_mass

def peptideToMassConverter(peptide):
    peptide_length = len(peptide)
    mass_list = []
    for index in range(peptide_length):
        aa_mass = integer_masses[peptide[index]]
        mass_list.append(str(aa_mass))
    mass_peptide = '-'.join(mass_list)
    return mass_peptide

integer_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
masslist = {}[0]
print(masslist)
m = 128

#Needs recursion and memoization (dynamic programming). Come back to this after I get to it.
#Solution:
#57-71   71-57   128
#Total: 3 possible peptides
#print(CountingPeptidesGivenMass(m))
