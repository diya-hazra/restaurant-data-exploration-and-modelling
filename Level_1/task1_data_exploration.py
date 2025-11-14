import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('dataset/dataset.csv')


print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nInfo:")
print(df.info())

print("\nMissing values:\n", df.isnull().sum())

num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].median())

cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    if df[col].isnull().any():
        df[col] = df[col].fillna(df[col].mode()[0])
rating_col = None

for c in ['Aggregate rating', 'Aggregate_rating', 'Rating']:
    if c in df.columns:
        rating_col = c
        break

if rating_col:
    plt.figure(figsize=(6,4))
    df[rating_col].hist(bins=20)
    plt.title(f"Distribution of {rating_col}")
    plt.savefig("L1_T1_rating_distribution.png")
    plt.show()

df.to_csv("cleaned_dataset_step1.csv", index=False)
print("\nSaved cleaned dataset as cleaned_dataset_step1.csv")
