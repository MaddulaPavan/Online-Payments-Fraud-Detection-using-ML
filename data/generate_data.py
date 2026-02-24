import pandas as pd
import numpy as np
import os

# Set seed for reproducibility
np.random.seed(42)

# Define columns
columns = ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud']

# Data
n_rows = 5000
data = {
    'step': np.random.randint(1, 744, n_rows),
    'type': np.random.choice(['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER'], n_rows),
    'amount': np.random.uniform(100, 100000, n_rows),
    'nameOrig': ['C' + str(i) for i in np.random.randint(1000000, 9999999, n_rows)],
    'oldbalanceOrg': np.random.uniform(0, 200000, n_rows),
}

# Calculated columns
data['newbalanceOrig'] = np.maximum(0, np.array(data['oldbalanceOrg']) - np.array(data['amount']))
data['nameDest'] = ['C' + str(i) if np.random.rand() > 0.5 else 'M' + str(i) for i in np.random.randint(1000000, 9999999, n_rows)]
data['oldbalanceDest'] = np.random.uniform(0, 200000, n_rows)
data['newbalanceDest'] = np.array(data['oldbalanceDest']) + np.array(data['amount'])

# Fraud logic (simplified for dummy data)
# Transfers or Cash outs with large amounts are more likely to be fraud
data['isFraud'] = np.where(
    ((data['type'] == 'TRANSFER') | (data['type'] == 'CASH_OUT')) & (np.array(data['amount']) > 90000), 
    1, 0
)

# Add some randomness to isFraud
random_indices = np.random.choice(n_rows, int(n_rows * 0.05), replace=False)
data['isFraud'][random_indices] = 1

data['isFlaggedFraud'] = np.where(np.array(data['amount']) > 200000, 1, 0)

df = pd.DataFrame(data)

# Save to CSV
output_path = r'c:\Users\Pavan Maddula\Desktop\SM-Internship\online payments fraud detection\data\PS_20174392719_1491204439457_logs.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Dataset generated at {output_path}")
