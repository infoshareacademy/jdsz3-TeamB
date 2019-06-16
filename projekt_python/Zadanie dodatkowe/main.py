import funkcje_statystyczne as fs
import wykresy as w
from msvcrt import getch
import sys

# Menu główne
print("\n Witaj w programie Mini BI! \n -------Menu główne------- \n 1. Funkcje statystyczne \n 2. Wykresy \n 3. Wyjście")
try:
    while True:
        # Funkcje statystyczne
        key = ord(getch())
        if key == 49:
            print("\n\n ---Funkcje statystyczne---")
            print(" Wybierz jedną z funkcji: \n 1. suma \n 2. min  \n 3. max \n 4. średnia \n 5. mediana \n 6. wariancja \n 7. odchylenie standardowe")
            while True:
                key = ord(getch())
                if key == 49:
                    fs.f_sum()
                    fs.koniec()
                elif key == 50:
                    fs.f_min()
                    fs.koniec()
                elif key == 51:
                    fs.f_max()
                    fs.koniec()
                elif key == 52:
                    fs.f_mean()
                    fs.koniec()
                elif key == 53:
                    fs.f_median()
                    fs.koniec()
                elif key == 54:
                    fs.f_var()
                    fs.koniec()
                elif key == 55:
                    fs.f_std()
                    fs.koniec()

        #Wykresy
        elif key == 50:
            w.wykresy()
            fs.koniec()

        # Wyjście z programu
        elif key == 51:
            sys.exit()
except SystemExit:
    pass
except:
    print("\n Ups... coś poszło nie tak. \n")
    fs.koniec()