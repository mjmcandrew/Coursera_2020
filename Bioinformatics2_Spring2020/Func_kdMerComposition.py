def kdMerComposition(text, k, d):
    kdMers = []
    for index in range(len(text) - ((2 * k) + d) + 1):
        read1_start = index
        read2_start = index + k + d
        read1 = text[read1_start:read1_start + k]
        read2 = text[read2_start:read2_start + k]
        kdMers.append([read1, read2])
    return kdMers


text = 'TAATGCCATGGGATGTT'
result = kdMerComposition(text, 3, 2)
print(result)
for kdMer in result:
    print('(' + kdMer[0]+ '|' + kdMer[1] + ')')
