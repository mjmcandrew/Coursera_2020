def LeaderboardCyclopeptideSequencing(Spectrum, N):
    Leaderboard = ['']
    LeaderPeptide = ''
    while Leaderboard:
        Leaderboard = Expand(Leaderboard)
        for peptide in Leaderboard:
            peptide_mass = calculateMass(peptide)
            if peptide_mass == Spectrum[-1]:
                if
    Leaderboard ← set containing only the empty peptide
    LeaderPeptide ← empty peptide
    while Leaderboard is non-empty
        Leaderboard ← Expand(Leaderboard)
        for each Peptide in Leaderboard
            if Mass(Peptide) = ParentMass(Spectrum)
                if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                    LeaderPeptide ← Peptide
            else if Mass(Peptide) > ParentMass(Spectrum)
                remove Peptide from Leaderboard
        Leaderboard ← Trim(Leaderboard, Spectrum, N)
    output LeaderPeptide


def expandPeptides(peptides, spectrum):
    expandedPeptides = []
    for peptide in peptides:
        for key in integer_masses:
            if integer_masses[key] in spectrum:
                branched_peptide = peptide + key
                expandedPeptides.append(branched_peptide)
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

def CyclopeptideScoring(Peptide, Spectrum):
    theoretical_spectrum = CyclicSpectrum(peptide)
    #Calculates the theoretical cyclic spectrum of the input peptide.
    score = 0
    #Initializes score to 0.
    for mass in theoretical_spectrum:
        #Iterates through the masses in the list 'theoretical_spectrum'.
        if mass in Spectrum:
            #If the mass is in the input 'Spectrum', the score is inremented
            #by 1, and the mass is removed from the input 'Spectrum' in order
            #to properly account for multiplicity of masses.
            score += 1
            Spectrum.remove(mass)
    return score

integer_masses = {'G': 57, 'A': 71, 'S': 87, 'P': 97, 'V': 99, 'T': 101, 'C': 103, 'I': 113, 'L': 113, 'N': 114, 'D': 115, 'K': 128, 'Q': 128, 'E': 129, 'M': 131, 'H': 137, 'F': 147, 'R': 156, 'Y': 163, 'W': 186}
