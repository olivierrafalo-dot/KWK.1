import random

def generuj_postac():
    postac = {
        "imie": random.choice(["Legolas", "Aragorn", "Gandalf", "Frodo"]),
        "rasa": random.choice(["Człowiek", "Czarodziej", "Elf", "Hobbit"]),
        "sila": random.randint(10, 20), "zrecznosc": random.randint(5, 15),
        "mana": random.randint(50, 100), "inteligencja": random.randint(12, 18),
    }
    
    print("TWOJA POSTAĆ RPG")
    for klucz, wartosc in postac.items():
        print(f"{klucz.capitalize()}: {wartosc}")
