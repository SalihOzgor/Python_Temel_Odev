def list_reverser(liste):
    for a in liste:
        if type(a) == list:
            list_reverser(a)
    return(liste.reverse())

liste1 = [[1, 2], [3, 4], [5, 6, 7]]

list_reverser(liste1)

print(liste1)