import pandas as pd

# ORGANIZE MERFISH DATA
# 1. Filter out columns that are not the cell identifer and the 30 gene expressions
# 2. Sort gene expressions alphabetically 
# 3. Create new CSV file

# merfish data
df = pd.read_csv('combined_23027_section1.csv')

# PART 1 (FILTER)
# Identifiy unnecessary columns ex. section_number
to_remove = []
with open('to_remove.txt', encoding='utf-8') as f:
    to_remove = f.read().rstrip('\n').split('\n')

# delete identified unnecessary columns
df_filtered = df
for col in to_remove:
    df_filtered = df_filtered.drop(col, axis=1)

# PART 2 (SORT)
sorted_cols = [df_filtered.columns[0]] + sorted(df_filtered.columns[1:])
sorted_df = df_filtered[sorted_cols]

# PART 3 (CREATE)
# ensure that index=False so index column is not created
sorted_df.to_csv('combined_23027_section1_filtered.csv', index=False)
#df_filtered.to_csv('test.csv', index=False)
