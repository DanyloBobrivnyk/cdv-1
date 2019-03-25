print("cdv")
print(2)

#potęga
potega = 2 ** 10
print(potega)


tekst="CDV"
print(tekst*2)

#pobieranie danych z klawiatury
imie = input()
print("Twoje imie z klawiatury :"+imie)

nazwisko = input()
print("Twoje imie "+imie+" twoje nazwisko :"+nazwisko)

dlugosc = len(nazwisko)
print(type(nazwisko))#string
print(type(dlugosc))#int
#1sposob
print("dlugosc nazwiska = ",dlugosc)
#2sposob
dlugosc = str(dlugosc) #konwersja danych
print("dlugosc nazwiska = "+dlugosc)
print()

#user pobiera z klawiatury swój wiek
#wyświetl dane w formacie Twój wiek : ... lat
print("\nPodaj swój wiek :", end="")
wiek = input()
wiek = str(wiek)
print("Twój wiek = "+wiek+" lat")

#pierwszyZnakDrugiTrzeci <<< camelcase

nazwisko = "Kowalski"

print(nazwisko[0])
print(nazwisko[len(nazwisko)-1])

#konwersja
x="5"
x=int(x)

y=4
y=y/2 #float
print(y)
print(nazwisko[0:3]) #Kow
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwlk
