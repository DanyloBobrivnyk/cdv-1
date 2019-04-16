#listy
imiona = ['Julia','Anna','Krystyna']
print(type(imiona))
imiona.append('Janusz')
len = len(imiona)
print(f'ilość imion :{len}')

#tuple
nazwisko = ('kowalski','nowak')
print(type(nazwisko))
#tuple są szybsze niż listy, ale nie można nic dodawać
print(nazwisko)

#słowniki
osoba = {
    'imie':'Julia',
    'nazwisko':'Nowak',
    'wiek':23
}
print(osoba)
print(type(osoba))
print(osoba['nazwisko'])
print(osoba.keys())
print(osoba.get('wzrost','brak danych'))
print(osoba.get('imie','brak danych'))
