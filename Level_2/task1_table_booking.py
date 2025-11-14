import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset_step1.csv")

table_col = next((c for c in df.columns if "table" in c.lower()), None)
del_col = next((c for c in df.columns if "online" in c.lower() or "delivery" in c.lower()), None)
rating_col = next((c for c in df.columns if "rating" in c.lower()), None)

def to_bool(s):
    return s.astype(str).str.lower().apply(lambda x: 1 if "yes" in x or "1" in x else 0)

df["Has_Table_Booking"] = to_bool(df[table_col]) if table_col else 0
df["Has_Online_Delivery"] = to_bool(df[del_col]) if del_col else 0

print("Table Booking %:", df["Has_Table_Booking"].mean()*100)
print("Online Delivery %:", df["Has_Online_Delivery"].mean()*100)

if rating_col:
    df.groupby("Has_Table_Booking")[rating_col].mean().plot(kind="bar", title="Avg Rating by Table Booking")
    plt.savefig("L2_T1_rating_table.png")
    plt.show()

    df.groupby("Has_Online_Delivery")[rating_col].mean().plot(kind="bar", title="Avg Rating by Online Delivery")
    plt.savefig("L2_T1_rating_online.png")
    plt.show()
