def Reverse(Pattern):
    reverse = ''
    for character in Pattern:
        reverse = character + reverse
    return reverse
