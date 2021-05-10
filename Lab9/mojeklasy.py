def testy():
    #Zadanie 1:
    print("Zadanie 1")
    p1=Student("Mateusz", "Zalewski", 19291, "Informatyka")
    print(p1.imie)
    print(p1.nazwisko)
    #print(p1.__nr_indeksu)
    print(p1.kierunek)
    print(p1)
    
    #Zadanie 2:
    print("\nZadanie 2")
    p2=Student("Tomasz", "Bęc", 51251, "Ekonomia")
    print(p1.__lt__(p2))
    print(p1.__eq__(p2))
    
    #Zadanie 3:
    print("\nZadanie 3")
    p3=Student("Patryk", "Ratajski", 63145, "Budownictwo")
    print("Licznik: %s"%(p3.getLicznik()))
    
    #Zadanie 4:
    print("\nZadanie 4")
    p4=StudentInformatyki("Paulina", "Olecka", 13412, "Informatyka", "Programowanie")
    print(p4)
    print("specjalność:", p4.specjalnosc)
    pass

class Student():
    __licznik = 0
    
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek):
        Student.__licznik+=1
        self.imie=imie
        self.nazwisko=nazwisko
        self.__nr_indeksu=nr_indeksu
        self.kierunek=kierunek
        
    def getLicznik(self):
        return self.__licznik
        
    def __lt__(self,other):
        if self.nazwisko<other.nazwisko:
            return True
        else:
            return False
        
    def __eq__(self,other):
        if self.nazwisko==other.nazwisko:
            return True
        else:
            return False
    
    def __str__(self):
        return "Imie: %s, nazwisko: %s, nr ideksu: %s, kierunek: %s"%(self.imie, self.nazwisko, self.__nr_indeksu, self.kierunek)

class StudentInformatyki(Student):
    def __init__(self, imie, nazwisko, nr_indeksu, kierunek, specjalnosc):
        super(StudentInformatyki,self).__init__(imie, nazwisko, nr_indeksu, kierunek)
        self.kierunek = "Informatyka"
        self.specjalnosc = specjalnosc

if __name__ == "__main__":
    testy()