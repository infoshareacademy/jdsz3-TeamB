# Główne zastosowania czynnikowych technik analitycznych to: (1) redukcja liczby zmiennych oraz
# (2) wykrywanie struktury w związkach między zmiennymi, to znaczy klasyfikacja zmiennych.


# Połączenie dwóch zmiennych w jeden czynnik
# Analiza składowych głównych.


import pandas as pd
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity

# wczytanie pliku
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv")

# zamiana wartości na numeryczne
df2 = pd.get_dummies(df["Gender"])
df["GenderNumeric"] = df2["Male"]
df2 = pd.get_dummies(df["OverTime"])
df["OverTimeNumeric"] = df2["Yes"]

# wgląd w dane i wybór zmiennych
df.info()

# usunięcie zmiennych nieliczbowych
df.drop(['BusinessTravel', 'Department', 'EducationField',  'JobRole',
         'MaritalStatus', 'OverTime', 'Gender'], axis=1, inplace=True)  # 'Age',

# Ocena zestawu danych - czy możemy znaleźć czynniki na podstawie zmiennych?

# Test sferyczności Bartletta sprawdza, czy obserwowane zmienne w ogóle korelują
# Wynik 0 dla p value oznacza, że test był istotny statystycznie, wskazując,
# że obserwowana macierz korelacji nie jest macierzą tożsamości.
chi_square_value, p_value = calculate_bartlett_sphericity(df)
print(chi_square_value, ",",  p_value)


# Test Kaiser-Meyer-Olkin (KMO) mierzy przydatność danych do analizy czynnikowej.
# Wartość KMO mniejsza niż 0,6 jest uważana za niewystarczającą.
kmo_all, kmo_model = calculate_kmo(df)
print(kmo_model)


# Wartość własna to wariancja nowych kolejno wyodrębnionych czynników. Na podstawie wartości własnych wybieramy
# tylko te najistotniejsze czynniki.

# Ile czynników pozostawić ? - Kryterium Kaisera. Czynniki, które mają wartości własne większe niż 1,
# bo jeśli czynnik nie wyodrębnia przynajmniej tyle, ile jedna zmienna oryginalna, to go odrzucamy.

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 20, rotation=None)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
print(ev)

# wychodzi że 8 czynników (składowych głównych) ma wartość większą niż 1


# Test osypiska. Test osypiska zaproponowany przez Cattella.
# Cattell sugeruje, by znaleźć miejsce, od którego na prawo występuje łagodny spadek wartości własnych.
# Na prawo od tego punktu przypuszczalnie znajduje się tylko "osypisko czynnikowe";
plt.scatter(range(1, df.shape[1]+1), ev)
plt.plot(range(1, df.shape[1]+1), ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

# wychodzi że 3 czynniki schodzą ostro, a na czwartym jest juz łagodny spadek

# Poniżej wyniki skumulowanej wariancji w zależności od liczby czynnków --> wybór 5 czynników ze wzgledu na:
# wysoki wynik przy mniejszej ilosci czynników

# Łączna 45% skumulowana wariancja wyjaśniona wartościami 8 czynników
fa = FactorAnalyzer()
fa.analyze(df, 8, rotation="varimax")
load = fa.loadings
print(load)
gfv = fa.get_factor_variance()
print(gfv)

# Łączna 40% skumulowana wariancja wyjaśniona wartościami 7 czynników
fa = FactorAnalyzer()
fa.analyze(df, 7, rotation="varimax")
load = fa.loadings
print(load)
gfv = fa.get_factor_variance()
print(gfv)

# Łączna 40% skumulowana wariancja wyjaśniona wartościami 6 czynników
fa = FactorAnalyzer()
fa.analyze(df, 6, rotation="varimax")
load = fa.loadings
print(load)
gfv = fa.get_factor_variance()
print(gfv)

# Łączna 41% skumulowana wariancja wyjaśniona wartościami 5 czynników
fa = FactorAnalyzer()
fa.analyze(df, 5, rotation="varimax")
load = fa.loadings
print(load)
gfv = fa.get_factor_variance()
print(gfv)

# Łączna 37% skumulowana wariancja wyjaśniona wartościami 4 czynników
fa = FactorAnalyzer()
fa.analyze(df, 4, rotation="varimax")
load = fa.loadings
print(load)
gfv = fa.get_factor_variance()
print(gfv)


# Łączna 32% skumulowana wariancja wyjaśniona wartościami 3 czynników
fa = FactorAnalyzer()
fa.analyze(df, 3, rotation="varimax")
load = fa.loadings
print(load)
gfv = fa.get_factor_variance()
print(gfv)

# Analiza czynnikowa redukuje obserwowane zmienne do kilku niezauważalnych zmiennych lub identyfikuje
# grupy zmiennych powiązanych

