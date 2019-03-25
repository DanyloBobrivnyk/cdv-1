tekst = "Anna, Paweł, Tomek"
tab = tekst.split(", ")
print(tab)
print(tekst)
print(type(tab)) #list
imie1 = tab[0]
print(imie1)

imieDuze = imie1.upper()
print(imieDuze)

print(imie1.lower())
#sprawdzenie zawartości
nazwisko = "sebek"
zawartosc = nazwisko.isalpha()
print(zawartosc)

imie = "Julia"
print("\nDane usera \nMasz na imie", imie)

text1 = "Jan\n"
text2 = "Jan"
print(text1+text2)

text1 = text1.rstrip() #usuwanie biaych znaków
print(text1 + text2)
print(text1 + " " + text2)

#wyświetlanie łańcucha znaków

#wszystkie wersje pythona
text = "%s, Java i %s" % ("PHP","Python")
print(text)

#nowsze wersje pythona
text = "{1},Java i {0}".format("PHP","Java")
print(text)

new = text.replace("PHP", "C#")
print(new)

#wypisywanie danych
rok = 2019
miesiac = "Marzec"
dzien = 25
print("Data: ", end="")
print(dzien,miesiac,rok, sep="-")
