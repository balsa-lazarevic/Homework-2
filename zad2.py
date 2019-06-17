def moja_mapa(funkcija, elementi):
    vrati = []
    
    for el in elementi:
        vrati.append(funkcija(el))
    
    return vrati

def dupliraj(n):
  return n*2

print( moja_mapa(dupliraj, (20, 'abc', 'hello world', (1,2,3))) )

def moj_filter(funkcija, elementi):
    vrati = []
    
    for el in elementi:
        if funkcija(el):
            vrati.append(el)
    
    return vrati

def ima_ostatak(n):
    
    return bool(n % 2)

print( moj_filter(ima_ostatak, (1, 2, 3, 4, 5, 6)))

def moj_reduce(funkcija, elementi):    
    duzina_el = len(elementi)
    #pozovi prvi put
    zadnja_vrijednost = funkcija(elementi[0], elementi[1])
    #pozovi sve ostale
    for index, el in enumerate(elementi):
        if index + 1 < duzina_el and index > 0:
            zadnja_vrijednost = funkcija(zadnja_vrijednost, elementi[index + 1])
    
    return zadnja_vrijednost

def faktorijal(x, y):
    return x * y
    
def spoji(x, y):
    return x + y

print( moj_reduce(faktorijal, (1, 2, 3, 4, 5, 6)))
print( moj_reduce(spoji, ('a', 'b', 'c', 'd', 'e', 'f')))