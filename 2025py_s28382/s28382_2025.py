import random
import matplotlib.pyplot as plt


def generuj_sekwencje(dlugosc, imie):
    nukleotydy = ['A', 'C', 'G', 'T']
    sekwencja = ''.join(random.choice(nukleotydy) for _ in range(dlugosc))

    index = random.randint(0, dlugosc - 1)
    sekwencja = sekwencja[:index] + imie + sekwencja[index + len(imie):]

    return sekwencja


def oblicz_statystyki(sekwencja):
    a_count = sekwencja.count('A')
    c_count = sekwencja.count('C')
    g_count = sekwencja.count('G')
    t_count = sekwencja.count('T')

    dlugosc = len(sekwencja)

    a_percentage = (a_count / dlugosc) * 100
    c_percentage = (c_count / dlugosc) * 100
    g_percentage = (g_count / dlugosc) * 100
    t_percentage = (t_count / dlugosc) * 100

    cg_ratio = ((c_count + g_count) / (a_count + t_count)) * 100 if (a_count + t_count) != 0 else 0

    return a_percentage, c_percentage, g_percentage, t_percentage, cg_ratio


def zapisz_do_pliku(id_sekwencji, opis, sekwencja):
    nazwa_pliku = f"{id_sekwencji}.fasta"
    with open(nazwa_pliku, 'w') as f:
        f.write(f">{id_sekwencji} {opis}\n")
        f.write(sekwencja + "\n")


# ORIGINAL:
#
# MODIFIED (Przechowywanie logiki w metodzie pozwala zachowac czytelnosc kodu):
def wprowadz_dlugosc_jako_liczbe(dlugosc):
    integer = False
    while not integer:
        try:
            dlugosc = int(dlugosc)
            integer = True
        except ValueError:
            print(f"{integer} nie jest liczbą")
            dlugosc = input("Podaj długość sekwencji: ")
    return dlugosc


# ORIGINAL:
#
# MODIFIED (Utworzenie dodatkowej funkcji dla wyswietlania wykresu kolowego zachowuje czytelnosc kodu):
def wykres_kolowy(a_percentage, c_percentage, g_percentage, t_percentage):
    labels = ['A', 'C', 'G', 'T']
    sizes = [a_percentage, c_percentage, g_percentage, t_percentage]
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("Zawartość nukleotydów A, C, G, T w sekwencji DNA")
    plt.show()


def main():
    # ORIGINAL:
    # dlugosc = input("Podaj długość sekwencji: ")
    # MODIFIED (Dodanie sprawdzania czy jest podana wartosc liczba pozawala na korzystanie programu bez bledow):
    dlugosc = wprowadz_dlugosc_jako_liczbe(input("Podaj długość sekwencji: "))
    id_sekwencji = input("Podaj ID sekwencji: ")
    opis = input("Podaj opis sekwencji: ")
    imie = input("Podaj imię: ")

    sekwencja = generuj_sekwencje(dlugosc, imie)

    zapisz_do_pliku(id_sekwencji, opis, sekwencja)

    a_percentage, c_percentage, g_percentage, t_percentage, cg_ratio = oblicz_statystyki(sekwencja)

    # ORIGINAL:
    #
    # MODIFIED (Zapisywanie danych jako wykres kolowy robi ich bardziej czytelnymi):
    wykres_kolowy(a_percentage, c_percentage, g_percentage, t_percentage)
    # zrob zapisywanie
    print("\n")
    print(f"Sekwencja została zapisana do pliku {id_sekwencji}.fasta")
    print("Statystyki sekwencji:")
    print(f"A: {a_percentage:.2f}%")
    print(f"C: {c_percentage:.2f}%")
    print(f"G: {g_percentage:.2f}%")
    print(f"T: {t_percentage:.2f}%")
    print(f"%CG: {cg_ratio:.2f}")


if __name__ == "__main__":
    main()
