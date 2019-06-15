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
    print(" Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")

# Licznie sumy
def f_sum ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            wymiary_cala()
            #print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input(" Podaj nazwę wymiaru: ")
            #measure = input(" Podaj nazwę miary: ")
            #df_tab = df[[dimension, measure]]
            df_tab = df[dimension]
            sum = df_tab.agg(['sum'])
            #for row in sum.itertuples():
                #print(" Suma dla wymiaru", dimension, "o wartości", row.Index, "miara", measure, "wynosi:", row._1)
            print(" Suma dla wymiaru '", dimension, "' wynosi:", sum.values)
            break
        elif key == 50:
            wymiary_wycinek()
            kolumna2 = input(" Podaj nazwę wymiaru: ")
            test_str = str((df.iloc[0][kolumna2]))
            regex = r"[a-zA-Z]"
            matches = re.search(regex, test_str)
            if matches:
                print(" Dostępne wartości to:", df[kolumna2].drop_duplicates().values.tolist())
            val = input(" Podaj wartość wymiaru: ")
            if matches:
                wartosc = val
            else:
                wartosc = int(val)
            miary_wycinek()
            measure = input(" Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            sum = df_tab.groupby(kolumna2).agg(['sum'])
            wartosc2 = (df_tab[kolumna2].drop_duplicates().values.tolist())
            print(" Suma dla wartości '", wartosc2[0], "' z kolumny '", kolumna2, "' wynosi:", sum.values)
            break

# Licznie maxa
def f_max ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
            print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input("Podaj nazwę wymiaru: ")
            measure = input("Podaj nazwę miary: ")
            df_tab = df[[dimension, measure]]
            max = df_tab.groupby(dimension).agg(['max'])
            print("Max dla", measure, "wynosi:", max.values)
            break
        elif key == 50:
            kolumna2 = input('Podaj kolumnę: ')
            wartosc = int(input('Podaj wartość: '))
            measure = input("Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            max = df_tab.groupby(kolumna2).agg(['max'])
            print("Max dla wartości", wartosc, "z kolumny", kolumna2, "wynosi:", max.values)
            break

# Licznie min
def f_min ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
            print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input("Podaj nazwę wymiaru: ")
            measure = input("Podaj nazwę miary: ")
            df_tab = df[[dimension, measure]]
            min = df_tab.groupby(dimension).agg(['min'])
            print("Min dla", measure, "wynosi:", min.values)
            break
        elif key == 50:
            kolumna2 = input('Podaj kolumnę: ')
            wartosc = int(input('Podaj wartość: '))
            measure = input("Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            min = df_tab.groupby(kolumna2).agg(['min'])
            print("Min dla wartości", wartosc, "z kolumny", kolumna2, "wynosi:", min.values)
            break

# Liczenie średniej
def f_mean():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
            print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input("Podaj nazwę wymiaru: ")
            measure = input("Podaj nazwę miary: ")
            df_tab = df[[dimension, measure]]
            mean = df_tab.groupby(dimension).agg(['mean'])
            print("Średnia dla", measure, "wynosi:", mean.values)
            break
        elif key == 50:
            kolumna2 = input('Podaj kolumnę: ')
            wartosc = int(input('Podaj wartość: '))
            measure = input("Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            mean = df_tab.groupby(kolumna2).agg(['mean'])
            print("Średnia dla wartości", wartosc, "z kolumny", kolumna2, "wynosi:", mean.values)
            break

# Liczenie mediany
def f_median():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
            print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input("Podaj nazwę wymiaru: ")
            measure = input("Podaj nazwę miary: ")
            df_tab = df[[dimension, measure]]
            median = df_tab.groupby(dimension).agg(['median'])
            print("Mediana dla", measure, "wynosi:", median.values)
            break
        elif key == 50:
            kolumna2 = input('Podaj kolumnę: ')
            wartosc = int(input('Podaj wartość: '))
            measure = input("Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            median = df_tab.groupby(kolumna2).agg(['median'])
            print("Mediana dla wartości", wartosc, "z kolumny", kolumna2, "wynosi:", median.values)
            break

# Licznie wariancji
def f_var ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
            print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input("Podaj nazwę wymiaru: ")
            measure = input("Podaj nazwę miary: ")
            df_tab = df[[dimension, measure]]
            var = df_tab.groupby(dimension).agg(['var'])
            print("Wariancja dla", measure, "wynosi:", var.values)
            break
        elif key == 50:
            kolumna2 = input('Podaj kolumnę: ')
            wartosc = int(input('Podaj wartość: '))
            measure = input("Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            var = df_tab.groupby(kolumna2).agg(['var'])
            print("Wariancja dla wartości", wartosc, "z kolumny", kolumna2, "wynosi:", var.values)
            break

# Licznie odchylenia standardowego
def f_std ():
    print("\n Dostepne źródła danych: \n 1. Cała tabela \n 2. Wybrany fragment tabeli")
    while True:
        key = ord(getch())
        if key == 49:
            print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
            print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
            dimension = input("Podaj nazwę wymiaru: ")
            measure = input("Podaj nazwę miary: ")
            df_tab = df[[dimension, measure]]
            std = df_tab.groupby(dimension).agg(['std'])
            print("Odchylenie standardowe dla", measure, "wynosi:", std.values)
            break
        elif key == 50:
            kolumna2 = input('Podaj kolumnę: ')
            wartosc = int(input('Podaj wartość: '))
            measure = input("Podaj nazwę miary: ")
            df3 = df
            df3['Count'] = df.groupby(kolumna2)[kolumna2].transform(len)
            try:
                df4 = df3[df[kolumna2] == wartosc]
                if len(df4.index) == 0:
                    raise ValueError
            except ValueError:
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:1]]
                zakres = df4['Count'].values[0]
                df4 = df3.iloc[(df[kolumna2] - wartosc).abs().argsort()[:zakres]]
            df_row = df4.drop('Count', axis=1)
            df_tab = df_row[[kolumna2, measure]]
            std = df_tab.groupby(kolumna2).agg(['std'])
            print("Odchylenie standardowe dla wartości", wartosc, "z kolumny", kolumna2, "wynosi:", std.values)
            break

