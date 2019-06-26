import csv, os
import pandas as pd




# the file names
f1 = "FINAL.csv"
f2 = "transfermarktValue.csv"
out_f = "2.csv"

# read the files
df1 = pd.read_csv(f1)
df2 = pd.read_csv(f2)

# get the keys
keys1 = list(df1)
keys2 = list(df2)

# merge both files
for idx, row in df2.iterrows():
    data = df1[df1['Name'] == row['Name']]

    # if row with such id does not exist, add the whole row
    if data.empty:
        next_idx = len(df1)
        for key in keys2:
            df1.at[next_idx, key] = df2.at[idx, key]

    # if row with such id exists, add only the missing keys with their values
    else:
        i = int(data.index[0])
        for key in keys2:
            if key not in keys1:
                df1.at[i, key] = df2.at[idx, key]

# save the merged files
df1.to_csv(out_f, index=False, encoding='utf-8', quotechar="", quoting=csv.QUOTE_NONE)