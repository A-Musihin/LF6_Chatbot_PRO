
#Skript zum formatieren von Excel-Dateien (.xlsx) in JSON

import pandas as pd

df = pd.read_excel('KeywordAnswerList.xlsx')

df.to_json('data.json', orient='records', lines=True)

print("KeywordAnswerList.xlsx wurde formatiert = data.json")