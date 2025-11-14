import pandas as pd
import numpy as np

df = pd.read_csv("cleaned_dataset_step1.csv")

name_col = next((c for c in df.columns if "name" in c.lower()), None)
df["Name_length"] = df[name_col].astype(str).str.len() if name_col else 0

addr_col = next((c for c in df.columns if "address" in c.lower()), None)
df["Address_length"] = df[addr_col].astype(str).str.len() if addr_col else 0

cuis_col = next((c for c in df.columns if "cuis" in c.lower()), None)
df["Cuisines_count"] = (
    df[cuis_col].astype(str).str.split(",").apply(lambda x: len([i for i in x if i.strip()]))
    if cuis_col else 0
)

table_col = next((c for c in df.columns if "table" in c.lower()), None)
del_col = next((c for c in df.columns if "online" in c.lower() or "delivery" in c.lower()), None)

def to_bool(s):
    return s.astype(str).str.lower().apply(lambda x: 1 if "yes" in x else 0)

df["Has_Table_Booking"] = to_bool(df[table_col]) if table_col else 0
df["Has_Online_Delivery"] = to_bool(df[del_col]) if del_col else 0

df.to_csv("cleaned_dataset_engineered.csv", index=False)
print("Saved cleaned_dataset_engineered.csv")
