def finder(subword,lent):
    if subword[:lent] in elements:
        return ELEMENTS[subword[:lent]]
    return False

def elemental_forms(word):
    z1 = finder(word,1)
    z2 = finder(word,2)
    return [z1,z2]