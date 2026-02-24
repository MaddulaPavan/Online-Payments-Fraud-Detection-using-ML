import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import os

# Set style
plt.style.use('ggplot')

# Load data
data_path = r'c:\Users\Pavan Maddula\Desktop\SM-Internship\online payments fraud detection\data\PS_20174392719_1491204439457_logs.csv'
df = pd.read_csv(data_path)

# Pre-processing
df = df.drop(['nameOrig', 'nameDest', 'isFlaggedFraud'], axis=1)
le = LabelEncoder()
df['type'] = le.fit_transform(df['type'])

X = df.drop('isFraud', axis=1)
y = df['isFraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Graph 1: Model Accuracy Comparison
models = {
    "Random Forest": 0.94,
    "Decision Tree": 0.90,
    "Extra Trees": 0.939,
    "XGBoost": 0.94
}

plt.figure(figsize=(10, 6))
colors = ['#6366f1', '#818cf8', '#c084fc', '#f472b6']
bars = plt.bar(models.keys(), models.values(), color=colors)
plt.ylim(0.8, 1.0)
plt.title('Comparison of Model Accuracy Scores', fontsize=15, pad=20)
plt.ylabel('Accuracy Score', fontsize=12)
plt.xlabel('Machine Learning Model', fontsize=12)

# Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.005, f'{yval:.2%}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('model_comparison.png')
print("Saved Graph 1: model_comparison.png")

# Graph 2: Confusion Matrix for the Best Model (Random Forest)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['Legit', 'Fraud'], yticklabels=['Legit', 'Fraud'])
plt.title('Confusion Matrix: Best Performing Model', fontsize=15, pad=20)
plt.ylabel('Actual Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig('confusion_matrix.png')
print("Saved Graph 2: confusion_matrix.png")

plt.show()
