def StringComposition(Text, k):
    string_length = len(Text)
    kmer_list = []
    for index in range(string_length - k + 1):
        kmer = Text[index:index + k]
        kmer_list.append(kmer)
    kmer_list.sort()
    return kmer_list

k = int(input())
Text = input()
List = StringComposition(Text,k)
for i in List:
    print(i)
