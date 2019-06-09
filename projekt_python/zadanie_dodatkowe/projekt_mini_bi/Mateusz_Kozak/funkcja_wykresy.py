import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


data_1 =np.random.normal(0,1,500)
data_2 =np.random.normal(0,1.1,500)
data_3 = np.random.gamma(0,1.1,500)
data_4 = np.random.uniform(0,1.1,500)

bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
bars3 = [29, 3, 24, 25, 17]
bars4 = [5,15,21,13,6]
bars5 = [10,15,20,15,10]
bars6 = [3,5,13,17,14]
bars7 = [1,10,100,50,150]
bars8 = [2,20,40,80,160]

### probny data_set dla wykresu 1 i 9

data_set = [data_1, [[[bars1,bars2, bars3], [bars4, bars5,bars6]], [bars7, bars8]]]

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

def bar_plot (x_label_list, y_data_list, variable_label_list=False,**kwargs):
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
        else:
            procent=False
    plt.pie(sizes, labels=labels, autopct=procent,explode=explode, shadow=True, startangle=270)

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
lista = [data_1, data_2, data_1, [[data_2, data_1, data_3, data_4], data_1]]

#print([i for i in range(len(lista))])

def wykresy(data_set, **kwargs):
    print("""
    1 - subploty (wykresy łączone) lub wykres pojedynczy
    0- Koniec programu""")
    wybieracz = input("Wybierz odpowiednią opcję: \n")
    while str(int(wybieracz)) == "1":
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

            graph_loop = 0
            while graph_loop == 0:
                print("""
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
                wybieracz2 = input("\n Wybierz wykres jaki chcesz narysować:\n")
                if wybieracz2 == "1":
                    plot_hist(data_set[i], color= colors_list[i], bins="rice", rwidth=0.9)
                    first_value =int(plot_hist(data_set[i], color= colors_list[i], bins="rice", rwidth=0.9)[1][0]-2)
                    last_value=int(plot_hist(data_set[i], color= colors_list[i], bins="rice", rwidth=0.9)[1][-1]+2)
                    plt.xticks(range(first_value,last_value))
                    plt.ylabel(f"Liczba rekordów wykresu {str(i+1)}")
                    plt.grid()
                    if i>len((data_set)):
                        colors_list.append("r")
                graph_loop +=1
                if str(int(wybieracz2)) == "2":
                    plot_sb_hist(data_set[i], color= colors_list[i])
                    plt.ylabel(f"Liczba rekordów wykresu {str(i + 1)}")
                    plt.grid()
                    if i>len((data_set)):
                        colors_list.append("r")
                if wybieracz2 == "3":
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
                graph_loop +=1
                if str(abs(int(wybieracz2))) == "4":
                    #[[data_2, data_1], data_1]
                    lista_legend =[]
                    for j in range(len(data_set[i][0])):
                        scatter_plot(data_set[i][0][j], data_set[i][-1], color=colors_list[j], marker=marker_list[j])
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
                graph_loop += 1
                if str(abs(int(wybieracz2))) == "5":
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
                if str(abs(int(wybieracz2))) == "6":
                    pie_chart(data_set[i][0], data_set[i][1])
                graph_loop += 1
                if str(abs(int(wybieracz2))) == "7":
                    os_x = input("Podaj nazwę osi x: \n")
                    os_y = input("Podaj nazwę osi y: \n")
                    pytanie_wyglad = input("Czy chcesz aby wykres wyglądał normalnie(n) czy bajerancko(t)? (t/n): \n")
                    if pytanie_wyglad == "n":
                        hist_2D(data_set[i][0], data_set[i][1], annot_kws=dict(stat="r"),
                                marginal_kws=dict(bins=15, rug=True),
                                s=35, edgecolor="w", linewidth=1).set_axis_labels(os_x, os_y)
                    elif pytanie_wyglad =="t":
                        cmap = sb.cubehelix_palette(as_cmap=True, dark=0, light=1, reverse=False)
                        sb.kdeplot(data_2, data_3, cmap=cmap, n_levels=60, shade=True).set_axis_labels(os_x, os_y)
                if str(abs(int(wybieracz2))) == "8":
                    pair_plot(data_set[i])
                graph_loop += 1
                if str(abs(int(wybieracz2))) == "9":
                    lista_legend_2 = []
                    try:
                        for z in range(len(data_set[-1][i])):
                            print(f"data_Set[i]: {data_set[i]}")
                            print(f"data_set [i][-1]: {data_set[-1][i]}")
                            marker_list_2 = ['o', 'x', ',', '+', 'd', 'v', '^', '<', '>', 's', '.']
                            marker_from_list = marker_list_2[z]
                            size_maker = data_set[i][-1][z]
                            for j in range(len(data_set[i][0][0])):
                                print(f"len: {len(data_set[i][0])}")
                                print(f"loop {j}")
                                print(f"data_set x: {data_set[i][0][0][j]}")
                                print(f"data_set y: {data_set[i][0][-1][j]}")
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
                graph_loop += 1
            plt.title(f"Wykres {i+1}")
        plt.show()
        #graph_loop_init += 1
        print("""
            1 - Histogram matplotlib
            2 - Histogram seborn
            3 - Wykres pudełkowy
            4 - Wykres punktowy (należy podać dane w postaci data = [data1--> os x,data2--> os y]
            5 - Wykres słupkowy ( format danych -> [x_labels, y_lista_wartosci])
            6 - Wykres kołowy (format danych data[i][0] = labels, data[i][1] = wartosci)
            7 - Histogram 2D (format danych -> data_set[i] = [x= data_set[i][0]  , y= data_set[i][1]])
            8 - Pair Plot (do pokazania korelacji miedzy podanymi danymi) data_set[i] = [data1, data2, data3 ...]
            9 - Wykres bąbelkowy -> [[[x1 -> lista, x2-->lista , x3-->lista], y --> lista], rozmiar kulek -->lista]
            0 - Koniec programu""")
        wybieracz = input("\nJeżeli chcesz dalej ysować wykresy, wcisnij  opowiednia opcję: \n")

plots = wykresy(data_set)
input("\nAby zakonczyc program wcisnij ENTER \n")