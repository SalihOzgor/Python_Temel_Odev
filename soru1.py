def list_flatter(liste):
    new_liste = []

    for a in liste:
        if type(a) != list:
            new_liste.append(a)
        else:
            for b in list_flatter(a):
                new_liste.append(b)
                
    
    return new_liste


liste1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

print(list_flatter(liste1))