import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv")

# zamiana wartości na numeryczne
df2 = pd.get_dummies(df["Gender"])
df["GenderNumeric"] = df2["Male"]
df2 = pd.get_dummies(df["OverTime"])
df["OverTimeNumeric"] = df2["Yes"]

#kolumny = df.columns
kolumny = [x for x in df.columns]
#print(kolumny)
#print(df[input("Wybierz kolumnę wpisując odpiewdnią nazwę: \n")])


def data_extractor(dataset):
    data_loop = 1
    lista_wykresow = []
    data_set = []
    while data_loop != 0:
        print("""
                        INSTRUKCJA
                        1 - Histogram matplotlib -> inaczej od seborna wygląda
                        2 - Histogram seborn
                        3 - Wykres pudełkowy (można kilka na jednym zrobić!! Pytać Kozaka jak :))
                        4 - Wykres punktowy (należy podać dane w postaci data = [data1--> os x,data2--> os y]
                        5 - Wykres słupkowy (format danych -> x = [["a"],["b"]], y = [[xa, ya],[xb,yb]], nazwy = [])
                        6 - Wykres kołowy (format danych data[i][0] = labels, data[i][1] = wartosci)
                        7 - Histogram 2D (format danych -> data_set[i] = [x= data_set[i][0]  , y= data_set[i][1]])
                        8 - Pair Plot (do pokazania korelacji miedzy podanymi danymi) data_set[i] = [data1, data2, data3 ...]
                        9 - Wykres bąbelkowy -> [[[x1 -> lista, x2-->lista , x3-->lista], y --> lista], rozmiar kulek -->lista]
                        0 - Koniec programu""")

        data_wybieracz = str(input("\n Wybierz dla którego wykresu chcesz wystawić dane:\n"))
        if data_wybieracz == "1":
            print("Histogram Matplotlib")
            print(f"Dostępne tagi to: \n {kolumny}")
            dana = None
            while dana not in kolumny:
                dana = input("Wpisz tag kolumny: \n")
            data_set.append(dataset[dana])
            lista_wykresow.append(int(data_wybieracz))
        data_loop +=1

        if data_wybieracz == "2":
            print("Histogram Seaborn")
            print(f"Dostępne tagi to: \n {kolumny}")
            dana = None
            while dana not in kolumny:
                dana = input("Wpisz tag kolumny: \n")
            data_set.append(dataset[dana])
            lista_wykresow.append(int(data_wybieracz))
        data_loop +=1

        if data_wybieracz == "3":
            print("Wykres Pudełkowy")
            x3_data_loop = 0
            box_plot_list = []
            while x3_data_loop != "0":
                print("""
                            1 - dodaj dane
                            0 - zakończ
                            """)
                x3_data_loop = input("Podaj numer odpowiedniej czynnosci: \n")
                if x3_data_loop == "1":
                    print(f"Dostępne tagi to: \n {kolumny}")
                    dana = None
                    while dana not in kolumny:
                        dana = input("Wpisz tag kolumny: \n")
                    box_plot_list.append(dataset[dana])
                lista_wykresow.append(int(data_wybieracz))
            data_set.append(box_plot_list)
        data_loop +=1

        if data_wybieracz == "4":
            print("Wykres Punktowy")
            wykres_punktowy_lista = []
            dane_serii_x = []
            print(f"Dostępne tagi to: \n {kolumny}")
            dana_y = None
            ile_x = int(input("Ile serii danych dla jendnej osi y?: \n"))
            for i in range(ile_x):
                dana_x = None
                while dana_x not in kolumny:
                    dana_x = input("Wpisz tag kolumny dla osi x: \n")
                    dane_serii_x.append(dataset[dana_x])
            while dana_y not in kolumny:
                dana_y = input("Wpisz tag kolumny dla osi y: \n")
            y = dataset[dana_y]
            wykres_punktowy_lista.append(dane_serii_x)
            wykres_punktowy_lista.append(y)
            data_set.append(wykres_punktowy_lista)
            lista_wykresow.append(int(data_wybieracz))
        data_loop += 1

        if data_wybieracz == "5":
            print("Wykres slupkowy")
            seria_x = []
            seria_y_main = []
            seria_nazwy = []
            ilosc_slupkow = int(input("Podaj ilosć słupków w serii: \n"))
            for i in range(ilosc_slupkow):
                print(f"Dostępne tagi to: \n {kolumny}")
                x_labels = input("Wpisz tag kolumny dla osi x: \n")
                seria_x.append(x_labels)
            for serie in range(len(seria_x)):
                print("""
                1 - Minimum
                2 - Maksimum
                3 - Srednia
                4 - Mediana
                5 - Odchylenie Standardowe
                6 - Wariancja
                7 - Suma
                8 - Zliczenie 
                            """)
                wybieracz_funkcji = input("Podaj numer odpowiedniej czynnosci: \n")

                if wybieracz_funkcji == "1":
                    print("Wybrales opcję minimum")
                    nazwa = "Minimum"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].min()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "2":
                    print("Wybrales opcję maksimum")
                    nazwa = "Maksimum"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].max()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "3":
                    print("Wybrales opcję srednia")
                    nazwa = "srednia"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].max()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "4":
                    print("Wybrales opcję Mediana ")
                    nazwa = "Mediana"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].median()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "5":
                    print("Wybrales opcję Odchylenie Standardowe")
                    nazwa = "Odchylenie Standardowe"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].std()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "6":
                    print("Wybrales opcję Wariancja")
                    nazwa = "Wariancja"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].var()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "7":
                    print("Wybrales opcję Suma")
                    nazwa = "Suma"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].sum()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)

                if wybieracz_funkcji == "8":
                    print("Wybrales opcję Zliczanie")
                    nazwa = "Zliczanie"
                    seria_y = []
                    for i in range(len(seria_x)):
                        seria_y_iter = dataset[seria_x[i]].size()
                        seria_y.append(seria_y_iter)
                    seria_y_main.append(seria_y)
                    seria_nazwy.append(nazwa)
            wykres_slupkowy_lista = [seria_x, seria_y_main, seria_nazwy]
            data_set.append(wykres_slupkowy_lista)
            lista_wykresow.append(int(data_wybieracz))
        data_loop += 1

        if data_wybieracz == "6":
            print("Pie Plot")
            pie_plot_set =[]
            pie_y_seria =[]
            pie_labels_seria = []
            ilosc_kawalkow = int(input("Podaj ilosć kawałków dla wykresu: \n"))
            print("""
                1 - Minimum
                2 - Maksimum
                3 - Srednia
                4 - Mediana
                5 - Odchylenie Standardowe
                6 - Wariancja
                7 - Suma
                8 - Zliczenie 
                            """)
            wybieracz_funkcji_pie = input("Podaj numer odpowiedniej czynnosci: \n")
            for it in range(ilosc_kawalkow):
                if wybieracz_funkcji_pie =="1":
                    print("Wybrales opcję minimum")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].min()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie =="2":
                    print("Wybrales opcję Maksimum")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].max()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie =="3":
                    print("Wybrales opcję srednia")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].mean()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie == "4":
                    print("Wybrales opcję mediana")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].median()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie == "5":
                    print("Wybrales opcję odchylenie standardowe")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].std()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie == "6":
                    print("Wybrales opcję wariancja")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].var()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie == "7":
                    print("Wybrales opcję suma")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].sum()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

                if wybieracz_funkcji_pie == "8":
                    print("Wybrales opcję zliczanie")
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_label_pie = input(f"Wpisz tag kolumny kawałka nr{it}: \n")
                    y_data_pie = dataset[x_label_pie].size()
                    pie_labels_seria.append(x_label_pie)
                    pie_y_seria.append(y_data_pie)

            pie_plot_set.append(pie_labels_seria)
            pie_plot_set.append(pie_y_seria)


            data_set.append(pie_plot_set)
            lista_wykresow.append(int(data_wybieracz))
        data_loop += 1

        if data_wybieracz == "7":
            print("Histogram 2D")
            print(f"Dostępne tagi to: \n {kolumny}")
            tagi_hist_1 = None
            tagi_hist_2 = None
            while tagi_hist_1 not in kolumny:
                tagi_hist_1 = input("Podaj odpowiedni tag dla 1 setu danych: \n")
            while tagi_hist_2 not in kolumny:
                tagi_hist_2 = input("Podaj odpowiedni tag dla 2 setu danych: \n")

            x_data = dataset[tagi_hist_1]
            y_data = dataset[tagi_hist_2]
            hist_data = [x_data, y_data]
            data_set.append(hist_data)
            lista_wykresow.append(int(data_wybieracz))

        if data_wybieracz == "8":
            print("Pair Plot")
            pair_plot_loop = 0
            pair_plot_list =[]
            while pair_plot_loop != "0":
                print("""
                    1 - dodaj serię danych
                    0 - zakończ
                                """)
                print(f"Dane do {len(pair_plot_list)+1} wykresu ")
                pair_plot_loop = input("Podaj numer odpowiedniej czynnosci: \n")
                if pair_plot_loop == "1":
                    print(f"Dostępne tagi to: \n {kolumny}")
                    dana_x_pair = None
                    while dana_x_pair not in kolumny:
                        dana_x_pair = input("Wpisz tag kolumny dla osi x: \n")
                        pair_plot_list.append(dataset[dana_x_pair])

            data_set.append(pair_plot_list)
            lista_wykresow.append((int(data_wybieracz)))
        data_loop += 1

        if data_wybieracz == "9":
            #[[[bars1, bars2, bars3], [bars4, bars5, bars6]], [bars7, bars8]]]
            print("Wykres Babelkowy")
            seria_punktow_x = []
            seria_punktow_y = []
            size_makers =[]
            ilosc_serii = int(input("Podaj ilosc serii (par x/y): \n"))
            for serie in range(ilosc_serii):
                print(f"Seria nr: {serie+1}")
                x_dane = None
                y_dane = None
                while x_dane not in kolumny:
                    print(f"Dostępne tagi to: \n {kolumny}")
                    x_dane = input("Podaj tag dla danych osi x: \n")
                    x_dane_punkty = dataset[x_dane]
                    seria_punktow_x.append(x_dane_punkty)
                while y_dane not in kolumny:
                    print(f"Dostępne tagi to: \n {kolumny}")
                    y_dane = input("Podaj tag dla danych osi y: \n")
                    y_dane_punkty = dataset[y_dane]
                    seria_punktow_y.append(y_dane_punkty)


            ilosc_size = int(input("Podaj ilosc setów danych różnicujących wielkosc babelkow : \n"))
            for size in range(ilosc_size):
                print(f"Size maker nr: {size + 1}")
                dane_size = None
                while dane_size not in kolumny:
                    print(f"Dostępne tagi to: \n {kolumny}")
                    dane_size = input("Podaj tag kolumny dla size_makera: \n")
                    size_maker_data = dataset[dane_size]
                    size_makers.append(size_maker_data)

            babelkowy_plot = [[seria_punktow_x, seria_punktow_y], size_makers]
            data_set.append(babelkowy_plot)
            lista_wykresow.append(int(data_wybieracz))
        data_loop += 1

        if data_wybieracz =="0":
            print("Koniec doddawania danych")
            data_loop = 0

    return [data_set, lista_wykresow]

def plot_hist(data, ax=None, **kwargs):
    ax = ax or plt.gca()
    return ax.hist(data, **kwargs)

def plot_sb_hist(data, **kwargs):
    kde_on_off = input("Czy chcesz wyswietlic funkcje KDE?(t/n) \n")
    if kde_on_off == "t":
        kde_triger = True
    else:
        kde_triger = False
    bins_zapytanie = input("Czy chcesz zmienić domyslną ilosć słupków?(t/n) \n")
    if bins_zapytanie == "t":
        bin_number = int(input("Podaj ilosc słupków: \n"))
    else:
        bin_number = "rice"
        print(f"Ilosc slupków -> metoda {bin_number}")
    ax = sb.distplot(data, kde=kde_triger , bins=bin_number,**kwargs)
    return ax

def box_plot_subplot(data, **kwargs):
    ax = plt.boxplot(data, bootstrap=10000, **kwargs)
    return ax

def scatter_plot (x, y, **kwargs):
    ax = plt.scatter(x, y, **kwargs)
    return ax

def bar_plot(x_label_list, y_data_list, variable_label_list=False,**kwargs):
    szerokosc_slupka =0.25
    r_1 = np.arange(len(y_data_list[0]))
    r_list =[r_1]
    for i in range(1, len(y_data_list)):
        r = [x+szerokosc_slupka for x in r_list[i-1]]
        r_list.append((r))
    for dane in range(len(y_data_list)):
        plt.bar(r_list[dane], y_data_list[dane], width=szerokosc_slupka, edgecolor='white',
                label=variable_label_list[dane] if variable_label_list else f"Var {str(dane)}")
        plt.xticks([r+szerokosc_slupka for r in range(len(r_1))], x_label_list)
    plt.legend(loc=2)
    plt.show()

def pie_chart(labels, sizes, **kwargs):
    explode = [0 for label in range(len(labels))]
    exlode_range = np.arange((len(explode))) + 1
    explode_indeks_list =[]
    pytanie = input("Czy chcesz wysnąć którąs częsć wykesu?(t/n): \n").lower()
    if pytanie == "t":
        print("""
        1 - wybor czesci
        0 - wyjscie z petli""")
        z = [i for i in range(len(labels))]
        x_list = [label for label in labels]
        wybor_czesci = input("Wybierz opcję: \n")
        while wybor_czesci != "0":
            print(f"Częsci do wysunięcia: {x_list}")
            print(f"Indeksy czesci: {z}")
            czesc = int(input("Podaj indeks czesci ktorą chcesz wysunąć: \n"))
            explode_indeks_list.append(czesc)
            del (x_list[(z.index(int(czesc)))])
            z.remove(czesc)
            print("""
                    1 - wybor czesci
                    0 - wyjscie z petli""")
            wybor_czesci = input("Wybierz opcję: \n")
            print("explode_indeks_list: ", explode_indeks_list)
            for i in explode_indeks_list:
                explode[i]=0.15
        pytanie2 = input("czy dane mają być zaprezentowane w sposób procentowy? (t/n) \n:").lower()
        if pytanie2 == "t":
            procent = '%1.1f%%'
            plt.pie(sizes, labels=labels, autopct=procent, explode=explode, shadow=True, startangle=270, **kwargs)
        else:
            plt.pie(sizes, labels=labels, explode=explode, shadow=True, startangle=270, **kwargs)


def hist_2D(data, **kwargs):
    ax = sb.jointplot(data[0], data[1], **kwargs)
    return ax

def pair_plot(data):
    data_x = data
    column_names = []
    for i in range(len(data)):
        x = input(f"Podaj nazwę {i+1} setu danych: \n")
        column_names.append(x)
    data_transpose = np.array(data_x).T
    data_pandas = pd.DataFrame(data_transpose, columns=[i for i in column_names])
    ax = sb.pairplot(data_pandas)
    return ax

wybieracz = None

def wykresy(data_set, wybieracze, **kwargs):
    #graph_loop_init = 0
    #while graph_loop_init == 0:
    plt.figure(figsize=(15,15))
    colors_list = ["r", "b", "g", "y", "c", "k", "m"]
    marker_list = ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']
    x = input("Czy chcesz sam ustawić ilosc kolumn czy zostawić wartosci domyslne? (t/n): \n" )
    if x =="t":
        wiersze_1 = int(input("Podaj ilosć wierszy: \n"))
        kolumny_1 = int(input("Podaj ilosc kolumn: \n"))
    else:
        if len(data_set)==1:
            wiersze_1 = 1
            kolumny_1 = 1
        else:
            print("Wartosci domyslne")
            wiersze_1 = int(len(data_set) / 2)
            kolumny_1 = int(len(data_set) / 2)
    for i in range(len(data_set)):
        plt.subplot(wiersze_1, kolumny_1, i+1, **kwargs)
        print("\n\nRysujesz wykres nr: ", i+1,"\n")
        print(f"Zastało ci jeszcze {len(data_set)-i} wykresów do narysowania!!")

        if wybieracze[i]== 1:
            plot_hist(data_set[i], color= colors_list[i], bins="rice", rwidth=0.9)
            first_value =int(plot_hist(data_set[i], color= colors_list[i], bins="rice", rwidth=0.9)[1][0]-2)
            last_value=int(plot_hist(data_set[i], color= colors_list[i], bins="rice", rwidth=0.9)[1][-1]+2)
            plt.xticks(range(first_value,last_value))
            plt.ylabel(f"Liczba rekordów wykresu {str(i+1)}")
            plt.grid()
            if i>len((data_set)):
                colors_list.append("r")

        if wybieracze[i] == 2:
            plot_sb_hist(data_set[i], color= colors_list[i])
            plt.ylabel(f"Liczba rekordów wykresu {str(i + 1)}")
            plt.grid()
            if i>len((data_set)):
                colors_list.append("r")

        if wybieracze[i] == 3:
            colors_list_box = ["#A52A2A", "#FF6103","#00008B","#66CD00", "#DC143C", "#68228B", "#00CED1", "	#006400", "	#EEAD0E",
                                       "#3D9140", "	#000000", "#E3CF57", "#A52A2A", "#FF6103","#00008B","#66CD00", "#DC143C", "#68228B",
                                       "#3D9140", "	#000000", "#E3CF57", "#00CED1", "#006400", "#EEAD0E"]
            bp = box_plot_subplot(data_set[i], notch=True)
            for whisker in bp["whiskers"]:
                whisker.set(color=colors_list_box[i], linewidth=2)
            for cap in bp["caps"]:
                cap.set(color=colors_list_box[i], linewidth=2)
            for median in bp['medians']:
                median.set(color=colors_list_box[i], linewidth=2)
            for flier in bp['fliers']:
                flier.set(marker='o', color=colors_list_box[i], alpha=0.5)
            for box in bp['boxes']:
                box.set(color=colors_list_box[i], linewidth=2)
            try:
                plt.xlabel(data_set.columns)
            except AttributeError:
                print("Dana wejsciowa musi/może być tabelą Pandas")
                plt.xlabel(input("Podaj nazwę dla osi x samodzielnie: \n"))

        if wybieracze[i] == 4:
            #[[data_2, data_1], data_1]
            lista_legend =[]
            print(f"dlugosc x: {len(data_set[i][0])}")
            print(f"dlugosc y: {len(data_set[i][1])}")

            for j in range(len(data_set[i][0])):
                scatter_plot(data_set[i][0][j], data_set[i][1], color=colors_list[j], marker=marker_list[j])
                try:
                    plt.legend(input(data_set[i][0][j].columns), loc=2)
                except AttributeError:
                    lista_legend.append(input("Podaj nazwę serii: \n"))
            try:
                plt.xlabel(data_set[i][0].columns)
                plt.ylabel(data_set[i][1].columns)
            except AttributeError:
                print("podaj własne oznaczenia osi: \n")
                plt.xlabel(input("Podaj nazwę dla osi x: \n"))
                plt.ylabel(input("Podaj nazwę dla osi y: \n"))
            plt.title(input("Podaj nazwę wykresu: \n"))
            plt.legend(lista_legend,loc=2)
            plt.grid()

        if wybieracze[i] == 5:
            try:
                bar_plot(data_set[i][0], data_set[i][1])
            except ValueError:
                print("Podales zly typ danej wejsciowej!")
                print(""" Poprawny typ:
                          data[i] = [xlabel_list, y_data_list, nazwy_zmiennych]  
                          x_label_list -> nazwy na osi x np. ["cos1", "cos2", "cos3"] -> data[i][0]
                          y_data_list np. [[15, 10],[5,8],[4,3]] -> data[i][1]
                          nazwy_zmiennych(opcjonalnie) -> nazwy do legendy, ["var1", "var2"]\n
                """)
                continue
        if wybieracze[i] == 6:
            pie_chart(data_set[i][0], data_set[i][1])

        if wybieracze[i] == 7:
            os_x = input("Podaj nazwę osi x: \n")
            os_y = input("Podaj nazwę osi y: \n")
            pytanie_wyglad = input("Czy chcesz aby wykres wyglądał normalnie(n) czy bajerancko(t)? (t/n): \n")
            if pytanie_wyglad == "n":
                hist_2D(data_set[i], annot_kws=dict(stat="r"),
                        marginal_kws=dict(bins=15, rug=True),
                        s=35, edgecolor="w", linewidth=1).set_axis_labels(os_x, os_y)
            elif pytanie_wyglad =="t":
                cmap = sb.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=False)
                sb.kdeplot(data_set[i][0], data_set[i][1], cmap=cmap, n_levels=60, shade=True)#.set_axis_labels(os_x, os_y)

        if wybieracze[i] == 8:
            pair_plot(data_set[i])

        if wybieracze[i] == 9:
            lista_legend_2 = []
            try:
                for z in range(len(data_set[-1][i])):
                    marker_list_2 = ['o', 'x', ',', '+', 'd', 'v', '^', '<', '>', 's', '.']
                    marker_from_list = marker_list_2[z]
                    size_maker = data_set[i][-1][z]
                    for j in range(len(data_set[i][0][0])):
                        print(f"size_maker: {size_maker}")
                        print(f"marker: {marker_from_list}")
                        scatter_plot(data_set[i][0][0][j], data_set[i][0][-1][j], color=colors_list[j], marker=marker_from_list,
                                     s=size_maker*100, alpha=0.5)
                        try:
                            plt.legend(input(data_set[i][0][0][j].columns), loc=2)
                        except AttributeError:
                                lista_legend_2.append(input("Podaj nazwę serii: \n"))
                                print(f"lista_legend: {lista_legend_2}")
                try:
                    plt.xlabel(data_set[i][0][0].columns)
                    plt.ylabel(data_set[i][0][-1].columns)
                except AttributeError:
                    print("podaj własne oznaczenia osi: \n")
                    plt.xlabel(input("Podaj nazwę dla osi x: \n"))
                    plt.ylabel(input("Podaj nazwę dla osi y: \n"))
                    plt.title(input("Podaj nazwę wykresu: \n"))
                    plt.legend(lista_legend_2, loc=2)
                    plt.grid()
            except:
                print("Podałes zly rozmiar danych!! Lista X musi sie rownac Y")
                print("Koniec programu")

        plt.title(f"Wykres {i+1}")
    plt.show()

def main():
    x = data_extractor(df)
    wykresy(x[0], x[1])
main()


