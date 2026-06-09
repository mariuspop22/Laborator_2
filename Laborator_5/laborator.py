
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

print("1. EXPLORAREA DATELOR\n")
df = pd.read_csv("StudentsPerformance.csv")

print("Primele 5 inregistrari:")
print(df.head())

print("\nInformatii despre dataset:")
df.info()

print("\nStatistici descriptive:")
print(df.describe())

print("\nValori lipsa:")
print(df.isnull().sum())



print("\n2. TIPURI DE VARIABILE")

categorical_cols = df.select_dtypes(include=['object']).columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

print("\nVariabile categorice:")
for col in categorical_cols:
    print(col)

print("\nVariabile numerice:")
for col in numeric_cols:
    print(col)



print("\n3. CURATAREA DATELOR")

print("\nValori lipsa inainte:")
print(df.isnull().sum())

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

print("\nValori lipsa dupa curatare:")
print(df.isnull().sum())


print("\n4. FEATURE ENGINEERING")

df["average_score"] = (
        df["math score"] +
        df["reading score"] +
        df["writing score"]
) / 3


def performance_level(score):
    if score < 50:
        return "low"
    elif score <= 70:
        return "medium"
    else:
        return "high"


df["performance_level"] = df["average_score"].apply(
    performance_level
)

df["is_prepared"] = (
        df["test preparation course"] == "completed"
).astype(int)

print(df[[
    "average_score",
    "performance_level",
    "is_prepared"
]].head())


print("\n=== 5. ENCODING ===")

le = LabelEncoder()

df["test preparation course"] = le.fit_transform(
    df["test preparation course"]
)

df = pd.get_dummies(
    df,
    columns=[
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch"
    ],
    drop_first=True
)

print("\nDataset dupa encoding:")
print(df.head())


print("\n6. FEATURE SELECTION")

constant_columns = []

for col in df.columns:

    if df[col].nunique() == 1:
        constant_columns.append(col)

print("\nColoane constante:")
print(constant_columns)

df.drop(columns=constant_columns,
        inplace=True,
        errors='ignore')

print("\nCorelatii numerice:")
print(df.corr(numeric_only=True))



print("\n7. SCALAREA DATELOR")

scaler = StandardScaler()

numeric_features = [
    "math score",
    "reading score",
    "writing score",
    "average_score"
]

print("\nValori inainte de scalare:")
print(df[numeric_features].head())

df[numeric_features] = scaler.fit_transform(
    df[numeric_features]
)

print("\nValori dupa scalare:")
print(df[numeric_features].head())



print("\n8. DATASET FINAL")

X = df.drop("performance_level", axis=1)

y = df["performance_level"]

print("\nDimensiune X:")
print(X.shape)

print("\nDimensiune y:")
print(y.shape)

print("\nPrimele randuri din X:")
print(X.head())

print("\nPrimele valori din y:")
print(y.head())


print("\n9. INTERPRETARE ===")

print("""
1. Caracteristicile cele mai importante:
   - math score
   - reading score
   - writing score
   - average_score
   - test preparation course

2. Impactul scalarii:
   - aduce toate variabilele pe aceeasi scara
   - imbunatateste performanta algoritmilor
   bazati pe distante

3. Fara feature selection:
   - risc de overfitting
   - antrenare mai lenta
   - complexitate inutila
   - performanta mai slaba
""")

