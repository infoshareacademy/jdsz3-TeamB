import pandas as pd
#import numpy as np
#import scipy as sc
#import statmodels as sm
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv", delimiter=",")

#print(df)
#lista = df.columns
#print(lista)


# Licznie sumy
def f_sum (dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    sum = df_tab.groupby(dimension).agg(['sum'])
    print(sum)

# Licznie maxa
def f_max (dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    max = df_tab.groupby(dimension).agg(['max'])
    print(max)

# Licznie min
def f_min (dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    min = df_tab.groupby(dimension).agg(['min'])
    print(min)

# Liczenie średniej
def f_mean(dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    mean = df_tab.groupby(dimension).agg(['mean'])
    print(mean)

# Liczenie mediany
def f_median(dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    median = df_tab.groupby(dimension).agg(['median'])
    print(median)

# Licznie wariancji
def f_var (dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    var = df_tab.groupby(dimension).agg(['var'])
    print(var)

# Licznie odchylenia standardowego
def f_std (dimension, measure):
    print("Dostępne wymiary to: 'Age', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus'")
    print("Dostępne miary to: 'MonthlyIncome', 'JobSatisfaction', 'JobInvolvement' ")
    dimension = input("Podaj nazwę wymiaru: ")
    measure = input("Podaj nazwę miary: ")
    df_tab = df[[dimension, measure]]
    std = df_tab.groupby(dimension).agg(['std'])
    print(std)

