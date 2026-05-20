import random

def generuj_postac():
    postac = {
        "imie": random.choice(["Legolas", "Aragorn", "Gandalf", "Frodo"]),
        "rasa": random.choice(["Człowiek", "Czarodziej", "Elf", "Hobbit"]),
	"sila":random.randint(10,20),"zrecznosc":random.randint5,15)
}

def pokaz_bohatera():
    print("--- TWOJA POSTAĆ RPG ---")
    print("Siła: 15")  # <-- To jest Twoja dopisana linijka
    print("Klasa: Mag")

if __name__ == "__main__":
    pokaz_bohatera()
    
    print("TWOJA POSTAĆ RPG")
    for klucz, wartosc in postac.items():
        print(f"{klucz.capitalize()}: {wartosc}")

if __name__ == "__main__":
    generuj_postac()
