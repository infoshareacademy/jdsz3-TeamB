import pandas as pd
from sklearn.datasets import load_iris
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt

df=pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition_v2.csv")

col = df.columns
print(col)

df.drop(['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole',
         'MaritalStatus', 'OverTime','Age'],axis=1,inplace=True)

#df.dropna(inplace=True)

df.info()


from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value=calculate_bartlett_sphericity(df)
print(chi_square_value, ",",  p_value)

from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)

print(kmo_model)

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer()
fa.analyze(df, 17, rotation=None)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
print(ev)


plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

fa = FactorAnalyzer()
fa.analyze(df, 6, rotation="varimax")

load = fa.loadings

print(load)

"""
fa = FactorAnalyzer()
fa.analyze(df, 4, rotation="varimax")
fa.loadings
"""

gfv = fa.get_factor_variance()

print(gfv)

