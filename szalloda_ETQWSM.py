from abc import ABC, abstractmethod
from datetime import datetime

class Szoba(ABC):
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

    @abstractmethod
    def get_tipus(self):
        pass

class EgyagyasSzoba(Szoba):
    def get_tipus(self):
        return "Egyágyas"

class KetagyasSzoba(Szoba):
    def get_tipus(self):
        return "Kétágyas"

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                self.foglalasok.append(Foglalas(szoba, datum))
                return szoba.ar
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def listaz_foglalasok(self):
        for foglalas in self.foglalasok:
            print(f"Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")

def main_menu():
    print("1. Foglalás")
    print("2. Lemondás")
    print("3. Foglalások listázása")
    print("0. Kilépés")

def foglalas_menu():
    print("Foglalás")
    szobaszam = input("Adja meg a szobaszámot: ")
    datum = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
    return szobaszam, datum

def lemondas_menu():
    print("Lemondás")
    index = int(input("Adja meg a lemondani kívánt foglalás sorszámát: "))
    return index

def main():
    print("Szálloda foglalási rendszer")
    print("---------------------------")
    
    # Teszt adatok
    szalloda = Szalloda("Teszt Szálloda")
    szalloda.add_szoba(EgyagyasSzoba("101", 50))
    szalloda.add_szoba(EgyagyasSzoba("102", 60))
    szalloda.add_szoba(KetagyasSzoba("201", 80))
    szalloda.add_szoba(KetagyasSzoba("202", 90))
    szalloda.add_szoba(KetagyasSzoba("203", 100))
    szalloda.foglalas("101", datetime(2024, 5, 16))
    szalloda.foglalas("201", datetime(2024, 5, 17))
    szalloda.foglalas("202", datetime(2024, 5, 18))
    szalloda.foglalas("101", datetime(2024, 5, 19))
    szalloda.foglalas("203", datetime(2024, 5, 20))

    while True:
        main_menu()
        choice = input("Válasszon egy műveletet (0-3): ")

        if choice == "1":
            szobaszam, datum = foglalas_menu()
            try:
                datum = datetime.strptime(datum, "%Y-%m-%d")
                if datum < datetime.now():
                    print("Hibás dátum: A foglalás csak jövőbeli dátumra lehetséges!")
                    continue
                ar = szalloda.foglalas(szobaszam, datum)
                if ar is not None:
                    print(f"Foglalás sikeres! Ár: {ar} Ft")
                else:
                    print("A megadott szobaszám nem létezik vagy foglalt!")
            except ValueError:
                print("Hibás dátum formátum!")
        elif choice == "2":
            index = lemondas_menu()
            if 0 < index <= len(szalloda.foglalasok):
                szalloda.lemondas(szalloda.foglalasok[index - 1])
                print("Foglalás sikeresen törölve!")
            else:
                print("Hibás sorszám!")
        elif choice == "3":
            print("Összes foglalás:")
            szalloda.listaz_foglalasok()
        elif choice == "0":
            print("Kilépés...")
            break
        else:
            print("Hibás választás! Kérem válasszon 0 és 3 közötti számot!")

if __name__ == "__main__":
    main()