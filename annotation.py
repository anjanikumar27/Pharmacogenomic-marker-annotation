import pandas as pd
# Load pharmacogenomic markers
pgx_df = pd.read_csv("pgx1_markers.txt", sep="\t")
# Load .bim file
bim_cols = ['Chr', 'BIM_rsID', 'Genetic_dist', 'Position', 'Allele1', 'Allele2']
bim_df = pd.read_csv("sample.bim", sep=" ", header=None, names=bim_cols)
# Convert Chr and Position to integers in both DataFrames as system read it as string
pgx_df['Chr'] = pgx_df['Chr'].astype(int)
pgx_df['Position'] = pgx_df['Position'].astype(int)
bim_df['Chr'] = bim_df['Chr'].astype(int)
bim_df['Position'] = bim_df['Position'].astype(int)
# Merge on Chr and Position
merged = pd.merge(pgx_df, bim_df, on=['Chr', 'Position'])
# Create annotated DataFrame
annotated_df = merged[['Gene', 'rsID', 'BIM_rsID', 'Chr', 'Position', 'Drug_Class', 'Allele1', 'Allele2']]
annotated_df = annotated_df.rename(columns={
'rsID': 'Original_rsID',
'Allele1': 'Allele_A',
'Allele2': 'Allele_B'
})
# Write to output
annotated_df.to_csv("Annotated_pgx.txt", sep="\t", index=False)
# Summary
found = len(annotated_df)
total = len(pgx_df)
print(f"Found {found} out of {total} pharmacogenomic markers in the BIM file")
