import pandas as pd

df = pd.read_csv('combined_23027_section1.csv')

to_remove = []
with open('to_remove.txt', encoding='utf-8') as f:
    to_remove = f.read().rstrip('\n').split('\n')

df_filtered = df
for col in to_remove:
    df_filtered = df_filtered.drop(col, axis=1)

df_filtered.to_csv('combined_23027_section1_filtered.csv')
