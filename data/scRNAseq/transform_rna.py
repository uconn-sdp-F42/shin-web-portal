import pandas as pd

# ORGANIZE RNA DATA
# 1. Filter out all other genes besides the 30 genes from merfish
# 2. Tranpose data (swap rows and columns)
# 3. Sort gene expressions alphabetically
# 4. Create new CSV file

df = pd.read_csv('CN4_56_M_G1.csv', index_col=False)

to_keep = []
with open('keep.txt', encoding='utf-8') as f:
    to_keep = f.read().rstrip('\n').split('\n')

filtered_df = df[df['Gene'].isin(to_keep)].set_index('Gene').T.reset_index(names='adjusted_cell_id')


sorted_cols = [filtered_df.columns[0]] + sorted(filtered_df.columns[1:])
sorted_df = filtered_df[sorted_cols]

sorted_df.to_csv('CN4_56_M_G1_filtered_transposed.csv', index=False)
