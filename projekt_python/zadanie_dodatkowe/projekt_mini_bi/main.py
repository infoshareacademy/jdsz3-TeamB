import funkcje_statystyczne as fs

# Menu główne
print("Witaj w programie Mini BI! \n -------Menu główne------- \n 1. Wybór zbioru danych \n 2. Funkcje statystyczne \n 3. Wykresy \n 4. Wyjście")
try:
    x = int(input("Wybierz numer modułu: "))

    # Menu modułu

    # Wydobywanie rekordów z tabeli
    if x == 1:
        print("Jesteś w module 'Wybór zbioru danych'")

    # Funkcje statystyczne
    elif x == 2:
        print("Jesteś w module 'Funkcje statystyczne'")
        print("Dostępne funkcje to \n 1. suma \n 2. min  \n 3. max \n 4. średnia \n 5. mediana \n 6. wariancja \n 7. odchylenie standardowe")
        try:
            y = int(input("Wybierz numer funkcji aby wykonać obliczenia: "))
            if y == 1:
                fs.f_sum("dimension","measure")
            elif y == 2:
                fs.f_min("dimension","measure")
            elif y == 3:
                fs.f_max("dimension","measure")
            elif y == 4:
                fs.f_mean("dimension","measure")
            elif y == 5:
                fs.f_median("dimension","measure")
            elif y == 6:
                fs.f_var("dimension","measure")
            elif y == 7:
                fs.f_std("dimension","measure")
            else:
                print("Nie ma takiego modułu. Zakończyłeś pracę w programie.")
        except ValueError:
            print("To nie jest poprawna wartość. Spróbuj jeszcze raz wpisująć cyfrę od 1 do 3")

    # Wykresy
    elif x == 3:
        print("Jesteś w module 'Wykresy'")

    # Wyjście z programu
    else:
        print("Zakończyłeś pracę w programie.")

except ValueError:
    print("To nie jest poprawna wartość. Spróbuj jeszcze raz wpisująć cyfrę od 1 do 3")