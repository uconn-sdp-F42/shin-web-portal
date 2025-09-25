import pandas as pd

# merfish dataframe
merfish_df = pd.read_csv('../merfish/combined_23027_section1_filtered.csv')

# RNA dataframe
rna_df = pd.read_csv('../scRNAseq/CN4_56_M_G1_filtered_transposed.csv')

# Sort merfish
sorted_cols = [merfish_df.columns[0]] + sorted(merfish_df.columns[1:])
sorted_merfish_df = merfish_df[sorted_cols]

# sort RNA
sorted_cols = [rna_df.columns[0]] + sorted(rna_df.columns[1:])
sorted_rna_df = rna_df[sorted_cols]

sorted_rna_df.to_csv('rna.csv')
sorted_merfish_df.to_csv('merfish.csv')
