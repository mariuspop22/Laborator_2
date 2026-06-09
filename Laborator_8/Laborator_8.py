from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
wine = load_wine(as_frame=True)
df = wine.frame

print("\nPRIMELE 5 RANDURI")
print(df.head())

print("\nFEATURE NAMES")
print(wine.feature_names)

X_small = df[['alcohol', 'flavanoids']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X_small, y, test_size=0.2, random_state=42
)
tree_small = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_small.fit(X_train, y_train)

plt.figure(figsize=(12,6))
plot_tree(
    tree_small,
    feature_names=['alcohol', 'flavanoids'],
    class_names=wine.target_names,
    filled=True
)
plt.title("Decision Tree (max_depth=2, 2 features)")
plt.show()

X_full = df[wine.feature_names]

X_train, X_test, y_train, y_test = train_test_split(
    X_full, y, test_size=0.2, random_state=42
)

tree_full = DecisionTreeClassifier(random_state=42)
tree_full.fit(X_train, y_train)

accuracy = tree_full.score(X_test, y_test)
print("\nACCURACY FULL TREE")
print("Accuracy:", accuracy)

importances = tree_full.feature_importances_

feat_importance = pd.DataFrame({
    "feature": wine.feature_names,
    "importance": importances
}).sort_values(by="importance", ascending=False)

print("\nFEATURE IMPORTANCE")
print(feat_importance)

def gini(labels):
    values, counts = np.unique(labels, return_counts=True)
    probs = counts / len(labels)
    return 1 - np.sum(probs ** 2)

example_labels = np.array([0, 1, 1, 2, 2, 2])

values, counts = np.unique(example_labels, return_counts=True)
probs = counts / len(example_labels)

gini_root = 1 - np.sum(probs ** 2)

print("\nGINI ROOT (exemplu)")
print("Gini:", gini_root)

threshold = 13
left = df[df['alcohol'] <= threshold]['target']
right = df[df['alcohol'] > threshold]['target']
gini_left = gini(left)
gini_right = gini(right)

weighted_gini = (len(left)/len(df))*gini_left + (len(right)/len(df))*gini_right
print("\nGINI AFTER SPLIT (alcohol <= 13)")
print("Weighted Gini:", weighted_gini)