imiona = ["Szymon","Kamil","Kasia","Ala"]

#a
print(imiona)
sort = sorted(imiona)
#b
sort.append("Basia")
sort.append("Michał")
print(sort)
sort.pop()
print(sort)
#c
sort.insert(3, "Ola")
print(sort)
#d
sort.reverse()
print(sort)
lista = sort*2
print(lista)
lista.sort()
print(lista)