# pandas is a Python library for working with tables of data (spreadsheet-like data).
# We import it and give it the nickname pd.
# We import it because we want to work with raw DES dataset whcih is in .csv file format 
# which is a table-like file format.
import pandas as pd

# Reading DES's raw dataset file in .csv file format.
# NOTE that:- it has many columns with DES's own internal naming conventions 
# (zHD, MU, MUERR_FINAL, and others we're not using).
# pd.read_csv(...) reads a CSV file into a table-like object (pandas calls this a "DataFrame" 
# - think of it like a spreadsheet loaded into memory, with rows and named columns). 
# We store that whole table in a variable named raw_DES_dataset - "raw_DES_dataset" because it's the unprocessed, 
# full-of-extra-columns version, straight from DES.
raw_DES_dataset = pd.read_csv("DES-SN5YR_HD.csv")

#Taking only the columns that we want to work with from raw DES dataset .csv file format file
# because out of the full table (DES's file has many more columns we don't need).
# and renaming them to our convenience , in the same left-to-right order as we selected them above.
# .copy() - makes a genuinely separate, independent table 
# (without this, editing the  "our_new_custom_DES_dataset" variable later could sometimes accidentally also change the "raw_DES_dataset" variable, 
# since without .copy() pandas might just be pointing at the same underlying data rather than duplicating it 
# - this is a pandas-specific safety habit).
# We store this smaller, selected table in a variable named our_new_custom_DES_dataset 
# - "our_new_custom_DES_dataset" because it's what we're going to output/write to a new file.
our_new_custom_DES_dataset = raw_DES_dataset[['zHD', 'MU', 'MUERR_FINAL']].copy()
our_new_custom_DES_dataset.columns = ['z', 'mu', 'mu_err']

# Creating new .csv file containing only our selected columns, 
# with having our given simplified names, 
# so that, our actual package code never has to know DES's specific 
# column-naming conventions.
# index=False tells pandas not to add an extra unnamed column of row numbers (0, 1, 2, 3...) 
# - without this, pandas adds one by default, which we don't want cluttering our clean output file.
our_new_custom_DES_dataset.to_csv("our_new_custom_DES_SN5yr_dataset.csv", index=False)


# Now we just print a confirmation message with the actual count filled in, 
# so you can see it worked and how much data you got.
# len(our_new_custom_DES_dataset) counts how many rows are in the table — i.e., how many supernovae. 
# The f"..." is an f-string (a way to insert a variable's value directly into a printed sentence).
print(f"Done. Wrote our_new_custom_DES_SN5yr_dataset.csv with {len(our_new_custom_DES_dataset)} supernovae")