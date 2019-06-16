import pandas as pd
from msvcrt import getch
import os
import sys
import re

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv", delimiter=",")

def koniec():
    while True:
        print("\n Enter - powrót do głównego menu \n Esc - wyjście \n")
        key = ord(getch())
        if key == 13:
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif key == 27:
            sys.exit()

def wymiary_cala():
    print("\n Dostępne wymiary to: 'Age', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',"
          "\n                      'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome',"
          "\n                      'NumCompaniesWorked', 'PerformanceRating', 'RelationshipSatisfaction', 'TotalWorkingYears',"
          "\n                      'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',"
          "\n                      'YearsSinceLastPromotion', 'YearsWithCurrManager'")

def wymiary_wycinek():
    print("\n Dostępne wymiary to: 'Age', 'BusinessTravel', 'Department', 'DistanceFromHome',"
          "\n                      'Education', 'EducationField', 'EnvironmentSatisfaction', 'Gender',"
          "\n                      'JobInvolvement', 'JobLevel', 'JobRole', 'JobSatisfaction',"
          "\n                      'MaritalStatus', 'MonthlyIncome', 'NumCompaniesWorked', 'OverTime',"
          "\n                      'PerformanceRating', 'RelationshipSatisfaction', 'TotalWorkingYears', 'TrainingTimesLastYear',"
          "\n                      'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion',"
          "\n                      'YearsWithCurrManager'")

def miary_wycinek():
    print("\n Dostępne miary to: 'Age', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction',"
          "\n                    'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome',"
          "\n                    'NumCompaniesWorked', 'PerformanceRating', 'RelationshipSatisfaction', 'TotalWorkingYears',"
          "\n                    'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',"
          "\n                    'YearsSinceLastPromotion', 'YearsWithCurrManager'")

# Licznie sumy
def f_sum ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            sum = df_tab.agg(['sum'])
            print("\n Suma dla wymiaru [", dimension, "] wynosi: [", sum.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to: [", col_val[0], "]")
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0],col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                sum = df_tab.groupby(col).agg(['sum'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Suma miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", sum.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break

# Licznie maxa
def f_max ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            max = df_tab.agg(['max'])
            print("\n Maksimum dla wymiaru [", dimension, "] wynosi: [", max.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to:", col_val)
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0], col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                max = df_tab.groupby(col).agg(['max'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Maksimum miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", max.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break

# Licznie min
def f_min ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            min = df_tab.agg(['min'])
            print("\n Minimum dla wymiaru [", dimension, "] wynosi: [", min.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to:", col_val)
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0],col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                min = df_tab.groupby(col).agg(['min'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Minimum miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", min.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break

# Liczenie średniej
def f_mean():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            mean = df_tab.agg(['mean'])
            print("\n Średnia dla wymiaru [", dimension, "] wynosi: [", mean.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to:", col_val)
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0],col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                mean = df_tab.groupby(col).agg(['mean'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Średnia miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", mean.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break

# Liczenie mediany
def f_median():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            median = df_tab.agg(['median'])
            print("\n Mediana dla wymiaru [", dimension, "] wynosi: [", median.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to:", col_val)
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0],col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                median = df_tab.groupby(col).agg(['median'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Mediana miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", median.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break

# Licznie wariancji
def f_var ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            var = df_tab.agg(['var'])
            print("\n Wariancja dla wymiaru [", dimension, "] wynosi: [", var.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to:", col_val)
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0],col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                var = df_tab.groupby(col).agg(['var'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Wariancja miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", var.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break

# Licznie odchylenia standardowego
def f_std ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            dimension = input(" Podaj nazwę wymiaru: ")
            df_tab = df[dimension]
            std = df_tab.agg(['std'])
            print("\n Odchylenie standardowe dla wymiaru [", dimension, "] wynosi: [", std.values[0], "]")
            break
        elif key == 50:
            wymiary_wycinek()
            col = input(" Podaj nazwę wymiaru: ")
            print(" ")
            test_str = str((df.iloc[0][col]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[col].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            print(" ")
            if measure != col:
                df['Count'] = df.groupby(col)[col].transform(len)
                try:
                    df2 = df[df[col] == wartosc]
                    if len(df2.index) == 0:
                        print(" Brak rekordów dla wartości: [", val, "]")
                        raise ValueError
                except ValueError:
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:1]]
                    col_val = df2[col].values
                    zakres = df2['Count'].values[0]
                    df2 = df.iloc[(df[col] - wartosc).abs().argsort()[:zakres]]
                    print(" Najbliższa pasująca wartość to:", col_val)
                print(" Liczba rekordów dla wartości [", df2.at[df2.index[0],col], "] wynosi: [", len(df2.index), "]")
                df_row = df2.drop('Count', axis=1)
                df_tab = df_row[[col, measure]]
                std = df_tab.groupby(col).agg(['std'])
                col_value = (df_tab[col].drop_duplicates().values.tolist())
                print("\n Odchylenie standardowe miary [", measure, "] dla wartości [", col_value[0], "] z wymiaru [", col, "] wynosi: [", std.values[0, 0], "]")
                break
            else:
                print("\n Wymiar oraz miara nie mogą być takie same!")
                break