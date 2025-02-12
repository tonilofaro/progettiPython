import pandas as pd
import json

# Carica il file JSON
with open('dashboardOnprem.tcl') as f:
    data = json.load(f)

# Converte il JSON in un DataFrame di pandas
df = pd.json_normalize(data)

# Salva il DataFrame in un file CSV
df.to_csv('dashboardOnprem.csv', index=False)
