# Główne zastosowania czynnikowych technik analitycznych to: (1) redukcja liczby zmiennych oraz
# (2) wykrywanie struktury w związkach między zmiennymi, to znaczy klasyfikacja zmiennych.


import pandas as pd
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt
from factor_analyzer.factor_analyzer import calculate_kmo
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
import seaborn as sns

# wczytanie pliku
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv")

# zamiana wartości na numeryczne
df2 = pd.get_dummies(df["Gender"])
df["GenderNumeric"] = df2["Male"]
df2 = pd.get_dummies(df["OverTime"])
df["OverTimeNumeric"] = df2["Yes"]
df3 = pd.get_dummies((df["EducationField"]))
print(df3)


# wgląd w dane i wybór zmiennych
print("-----wgląd w dane-----\n")
df.info()

print(df[["EducationField", "JobRole"]])
print(df["EducationField"])
print(df["JobRole"])
print(df["Department"])
# usunięcie zmiennych nieliczbowych
df.drop(['BusinessTravel', 'Department', 'EducationField',  'JobRole',
         'MaritalStatus', 'OverTime', 'Gender'], axis=1, inplace=True)

# Ocena zestawu danych - czy możemy znaleźć czynniki na podstawie zmiennych?

# Test sferyczności Bartletta sprawdza, czy obserwowane zmienne w ogóle korelują
# Wynik 0 dla p value oznacza, że test był istotny statystycznie, wskazując,
# że obserwowana macierz korelacji nie jest macierzą jednostkową (tożsamości).
print("\n-----Test Bartletta-----\n")
chi_square_value, p_value = calculate_bartlett_sphericity(df)
print("chi_square_value =", chi_square_value, ", p_value =",  p_value)


# Test Kaiser-Meyer-Olkin (KMO) mierzy przydatność danych do analizy czynnikowej.
# Wartość KMO mniejsza niż 0,6 jest uważana za niewystarczającą, bo poniżej redukcja zmiennych będzie nieznaczna.
print("\n-----Test Kaiser-Meyer-Olkin-----\n")
kmo_all, kmo_model = calculate_kmo(df)
print("KMO =", kmo_model)


# Wartość własna to wariancja nowych kolejno wyodrębnionych czynników. Na podstawie wartości własnych wybieramy
# tylko te najistotniejsze czynniki.

# Ile czynników pozostawić ? - Kryterium Kaisera. Czynniki, które mają wartości własne większe niż 1,
# bo jeśli czynnik nie wyodrębnia przynajmniej tyle, ile jedna zmienna oryginalna, to go odrzucamy.

# Utworzenie factor analysis object i wykonanie factor analysis

print("\n-----Wartość własna - wariancja kolejnych czynników-----\n")
fa = FactorAnalyzer()
fa.analyze(df, 20, rotation=None)

ev, v = fa.get_eigenvalues()
print(ev)

# wychodzi że 8 czynników (składowych głównych) ma wartość większą niż 1


# Test osypiska. Test osypiska zaproponowany przez Cattella.
# Cattell sugeruje, by znaleźć miejsce, od którego na prawo występuje łagodny spadek wartości własnych.
# Na prawo od tego punktu przypuszczalnie znajduje się tylko "osypisko czynnikowe";
print("\n-----Test osypiska-----\n")
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

print("\n-----Wyniki skumulowanej wariancji w zależności od ilości czynników-----\n")

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
load_choose = fa.loadings
print(load_choose)
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

sns.set(font_scale=1.6)
fig, (ax) = plt.subplots(figsize=(20, 15))
matrix = sns.heatmap(load_choose, ax=ax, center=0, vmin=-1, vmax=1, cmap=sns.diverging_palette(50, 200, as_cmap=True),
                     annot=True, fmt='.2f', annot_kws={"size": 24}, linewidths=.05)
plt.show()

# Opis dla wyznaczonych przez analize czynnikową czynników,
# dla czynników ukrytych przyjęto czynniki dominujący (reprezentanta)
df_grouped = df[["JobLevel", "MonthlyIncome"]].groupby(by=["JobLevel"]).describe()
print(df_grouped)

df_grouped = df[["YearsAtCompany", "MonthlyIncome"]].groupby(by=["YearsAtCompany"]).describe()
print(df_grouped)

df_grouped = df[["OverTimeNumeric", "MonthlyIncome"]].groupby(by=["OverTimeNumeric"]).describe()
print(df_grouped)

df_grouped = df[["NumCompaniesWorked", "MonthlyIncome"]].groupby(by=["NumCompaniesWorked"]).describe()
print(df_grouped)

df_grouped = df[["Age", "MonthlyIncome"]].groupby(by=["Age"]).describe()
print(df_grouped)

fig, (ax) = plt.subplots(figsize=(30, 12))
df_grouped = df[["YearsAtCompany", "MonthlyIncome"]].groupby(by=["YearsAtCompany"]).mean().reset_index()
ax = sns.barplot(x="YearsAtCompany", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
plt.show()

fig, (ax) = plt.subplots(figsize=(20, 12))
df_grouped = df[["JobLevel", "MonthlyIncome"]].groupby(by=["JobLevel"]).mean().reset_index()
ax = sns.barplot(x="JobLevel", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
plt.show()


fig, (ax) = plt.subplots(figsize=(15, 15))
df_grouped = df[["OverTimeNumeric", "MonthlyIncome"]].groupby(by=["OverTimeNumeric"]).mean().reset_index()
ax = sns.barplot(x="OverTimeNumeric", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
plt.show()


fig, (ax) = plt.subplots(figsize=(20, 12))
df_grouped = df[["NumCompaniesWorked", "MonthlyIncome"]].groupby(by=["NumCompaniesWorked"]).mean().reset_index()
ax = sns.barplot(x="NumCompaniesWorked", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
plt.show()


fig, (ax) = plt.subplots(figsize=(30, 12))
ax.set_xlim(0,42)
df_grouped = df[["Age", "MonthlyIncome"]].groupby(by=["Age"]).mean().reset_index()
ax = sns.barplot(x="Age", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped, ax =ax)
plt.show()


""" można się kiedyś pobawić
sns.set(font_scale=1.9)
fig, (ax) = plt.subplots(figsize=(30, 12))
ax.set_xlim(0,40)
df_grouped = df[["YearsAtCompany", "MonthlyIncome"]].groupby(by=["YearsAtCompany"]).mean().reset_index()
df_grouped2 = df[["YearsAtCompany", "MonthlyIncome"]].groupby(by=["YearsAtCompany"]).min().reset_index()
df_grouped3 = df[["YearsAtCompany", "MonthlyIncome"]].groupby(by=["YearsAtCompany"]).max().reset_index()
ax = sns.barplot(x="YearsAtCompany", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
ax = sns.lineplot(x="YearsAtCompany", y="MonthlyIncome", color='Green', data=df_grouped2)
ax = sns.lineplot(x="YearsAtCompany", y="MonthlyIncome", color='Red', data=df_grouped3)
plt.show()


fig, (ax) = plt.subplots(figsize=(20, 12))
ax.set_xlim(0,5)
df_grouped = df[["JobLevel", "MonthlyIncome"]].groupby(by=["JobLevel"]).mean().reset_index()
df_grouped2 = df[["JobLevel", "MonthlyIncome"]].groupby(by=["JobLevel"]).min().reset_index()
df_grouped3 = df[["JobLevel", "MonthlyIncome"]].groupby(by=["JobLevel"]).max().reset_index()
ax = sns.barplot(x="JobLevel", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
ax = sns.lineplot(x="JobLevel", y="MonthlyIncome", color='Green', data=df_grouped2)
ax = sns.lineplot(x="JobLevel", y="MonthlyIncome", color='Red', data=df_grouped3)
plt.show()


fig, (ax) = plt.subplots(figsize=(15, 15))
ax.set_xlim(0,1)
df_grouped = df[["OverTimeNumeric", "MonthlyIncome"]].groupby(by=["OverTimeNumeric"]).mean().reset_index()
df_grouped2 = df[["OverTimeNumeric", "MonthlyIncome"]].groupby(by=["OverTimeNumeric"]).min().reset_index()
df_grouped3 = df[["OverTimeNumeric", "MonthlyIncome"]].groupby(by=["OverTimeNumeric"]).max().reset_index()
ax = sns.barplot(x="OverTimeNumeric", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
ax = sns.lineplot(x="OverTimeNumeric", y="MonthlyIncome", color='Green', data=df_grouped2)
ax = sns.lineplot(x="OverTimeNumeric", y="MonthlyIncome", color='Red', data=df_grouped3)
plt.show()

sns.set(font_scale=1.9)
fig, (ax) = plt.subplots(figsize=(20, 12))
ax.set_xlim(0,9)
df_grouped = df[["NumCompaniesWorked", "MonthlyIncome"]].groupby(by=["NumCompaniesWorked"]).mean().reset_index()
df_grouped2 = df[["NumCompaniesWorked", "MonthlyIncome"]].groupby(by=["NumCompaniesWorked"]).min().reset_index()
df_grouped3 = df[["NumCompaniesWorked", "MonthlyIncome"]].groupby(by=["NumCompaniesWorked"]).max().reset_index()
ax = sns.barplot(x="NumCompaniesWorked", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped)
ax = sns.lineplot(x="NumCompaniesWorked", y="MonthlyIncome", color='Green', data=df_grouped2)
ax = sns.lineplot(x="NumCompaniesWorked", y="MonthlyIncome", color='Red', data=df_grouped3)
plt.show()


sns.set(font_scale=1.9)
fig, (ax) = plt.subplots(figsize=(30, 12))
ax.set_xlim(0,42)
df_grouped = df[["Age", "MonthlyIncome"]].groupby(by=["Age"]).mean().reset_index()
df_grouped2 = df[["Age", "MonthlyIncome"]].groupby(by=["Age"]).min().reset_index()
df_grouped3 = df[["Age", "MonthlyIncome"]].groupby(by=["Age"]).max().reset_index()
ax = sns.barplot(x="Age", y="MonthlyIncome", palette='Blues', capsize=10, data=df_grouped, ax =ax)
ax = sns.lineplot(x="Age", y="MonthlyIncome", color='Green', data=df_grouped2, ax =ax)
ax = sns.lineplot(x="Age", y="MonthlyIncome", color='Red', data=df_grouped3, ax =ax)
plt.show()

"""