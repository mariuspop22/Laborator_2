import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


diabetes = load_diabetes()
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df['target'] = diabetes.target

print("Primele 5 rânduri:")
print(df.head())

print("\nCaracteristici disponibile:")
print(diabetes.feature_names)

print("\nStatistici generale:")
print(df.describe())

print("\nMedia:")
print(df.mean())

print("\nDeviația standard:")
print(df.std())

print("\nValori minime:")
print(df.min())

print("\nValori maxime:")
print(df.max())


plt.figure()
plt.hist(df['bmi'], bins=20)
plt.xlabel('BMI')
plt.ylabel('Frecvență')
plt.title('Histogramă BMI')
plt.show()


plt.figure()
plt.scatter(df['bmi'], df['target'])
plt.xlabel('BMI')
plt.ylabel('Target')
plt.title('BMI vs Target')
plt.show()

plt.figure()
plt.scatter(df['age'], df['target'])
plt.xlabel('Vârstă')
plt.ylabel('Target')
plt.title('Vârstă vs Target')
plt.show()


X = df[['bmi']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.figure()
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel('BMI')
plt.ylabel('Target')
plt.title('Regresie liniară simplă')
plt.show()


mse = mean_squared_error(y_test, y_pred)
print("\nMSE (regresie simplă):", mse)


X2 = df[['bmi', 'bp']]

X2_train, X2_test, y_train, y_test = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

model2 = LinearRegression()
model2.fit(X2_train, y_train)


print("\nCoeficienți model (bmi, bp):", model2.coef_)

r2 = model2.score(X2_test, y_test)
print("R² (regresie multiplă):", r2)

