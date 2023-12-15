
#Skript zum formatieren von Excel-Dateien (.xlsx) in JSON

import pandas as pd

df = pd.read_excel('KeyPairList.xlsx')

df.to_json('KeyPairList.json', orient='records', lines=True)

print("KeyPairList.xlsx wurde formatiert = KeyPairList.json")