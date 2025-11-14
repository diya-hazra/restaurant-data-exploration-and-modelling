import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned_dataset_step1.csv")

num_cols = df.select_dtypes(include=['int64', 'float64']).columns
cat_cols = df.select_dtypes(include=['object']).columns

print("\nNumeric Stats:\n", df[num_cols].describe())

city_col = next((c for c in df.columns if "city" in c.lower()), None)
cuis_col = next((c for c in df.columns if "cuis" in c.lower()), None)

if city_col:
    top_cities = df[city_col].value_counts().head(15)
    top_cities.plot(kind='bar', figsize=(10,5), title="Top Cities")
    plt.savefig("L1_T2_top_cities.png")
    plt.show()

if cuis_col:
    cuisines = df[cuis_col].astype(str).str.split(',').explode().str.strip()
    top_cuis = cuisines.value_counts().head(15)
    top_cuis.plot(kind="bar", figsize=(10,5), title="Top Cuisines")
    plt.savefig("L1_T2_top_cuisines.png")
    plt.show()

if len(num_cols) > 1:
    plt.figure(figsize=(8,5))
    sns.heatmap(df[num_cols].corr(), annot=True)
    plt.savefig("L1_T2_correlation.png")
    plt.show()
