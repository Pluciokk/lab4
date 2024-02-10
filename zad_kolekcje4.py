
x = int(input("Twój wybór(od 1 do 6 zaleznie od podpunktu: "))
if x == 1:
    imie = input("Podaj swoje imie: ")
    print("Witaj " + imie)
elif x == 2:
    wiek = input("Podaj swój wiek: ")
    print("Twoj wiek to: " + wiek)
elif x == 3:
    imie = input("Podaj swoje imie: ")
    nazwisko = input("Podaj swoje nazwisko: ")
    print("Twoje inicjały to: " + imie[0] + nazwisko[0])
elif x == 4:
    lancuch = input("Podaj łańcuch: ")
    print(5*(lancuch+"\n"))
elif x == 5:
    lancuch1 = input("Podaj łańcuch 1: ")
    print(lancuch1)
    lancuch2 = input("Podaj łańcuch 2: ")
    print(lancuch2)
    lancuch3 = lancuch1 + lancuch2
    print(lancuch3)
elif x == 6:
    lancuch1 = input("Podaj łańcuch 1: ")
    print(lancuch1)
    lancuch2 = input("Podaj łańcuch 2: ")
    print(lancuch2)
    polowa1 = len(lancuch1)//2
    polowa2 = len(lancuch2)//2
    lancuch3 = lancuch1[0: polowa1] + lancuch2[polowa2:]
    print(lancuch3)
else:
    print("Niepoprawny wybór!")