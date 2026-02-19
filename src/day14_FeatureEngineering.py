#task1

import pandas as pd

data={
      'Name':["A","B","C","D","E","F"],
      'Transmission':['Automatic','Automatic','Manual','Manual','Manual','Automatic'],
      'Color':['Red','Blue','Red','Green','Blue','Green']
      }
df = pd.DataFrame(data)
df['Transmission'] = df['Transmission'].map({'Automatic': 0,'Normal': 1})

df = pd.get_dummies(df, columns=['Color'], drop_first=True)

print(df)

#task2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler, MinMaxScaler
sns.set(style="whitegrid")

np.random.seed(0)

df = pd.DataFrame({
    'Age': np.random.randint(20, 60, 10),
    'Salary': np.random.randint(20000, 120000, 10)
})

print("Original Data:\n")
print(df)
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data (Mean=0, Std=1):\n")
print(df_standardized)
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data (0 to 1 range):\n")
print(df_normalized)