import pandas as pd
import folium
from folium.plugins import MarkerCluster

df = pd.read_csv("cleaned_dataset_step1.csv")

lat_col = next((c for c in df.columns if "lat" in c.lower()), None)
lon_col = next((c for c in df.columns if "lon" in c.lower() or "long" in c.lower()), None)

if not lat_col or not lon_col:
    raise ValueError("Latitude or Longitude column not found.")

df = df.dropna(subset=[lat_col, lon_col])

map_center = [df[lat_col].mean(), df[lon_col].mean()]
m = folium.Map(location=map_center, zoom_start=4)

mc = MarkerCluster()

for _, row in df.iterrows():
    mc.add_child(folium.Marker(
        [row[lat_col], row[lon_col]],
        popup=str(row.get("Restaurant Name", "")),
    ))

m.add_child(mc)
m.save("L1_T3_map.html")
print("Saved map as L1_T3_map.html")
