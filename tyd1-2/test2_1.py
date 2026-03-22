from zad2_1 import Ksiazka, Biblioteka

bib = Biblioteka("Moja Biblioteka")

bib.dodaj(Ksiazka("Władca Pierścieni", "Tolkien", 1954, "978-0-123"))
bib.dodaj(Ksiazka("Hobbit", "Tolkien", 1937, "978-0-456"))

print(len(bib))  

wyniki = bib.szukaj("Tolkien")
print(wyniki)    

bib.usun("978-0-456")
print(len(bib))  
