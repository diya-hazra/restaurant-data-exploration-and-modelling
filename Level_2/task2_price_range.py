import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_dataset_step1.csv")

price_col = next((c for c in df.columns if "price" in c.lower()), None)
rating_col = next((c for c in df.columns if "rating" in c.lower()), None)

if not price_col:
    raise ValueError("Price range column not found.")

print("Most common price range:", df[price_col].mode()[0])

if rating_col:
    avg = df.groupby(price_col)[rating_col].mean()
    avg.plot(kind="bar", title="Average Rating by Price Range")
    plt.savefig("L2_T2_avg_rating_price.png")
    plt.show()
