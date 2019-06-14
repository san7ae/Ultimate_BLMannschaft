import csv, os
import pandas as pd




# the file names
f1 = "abgefangeneBaelle.csv"
f2 = "abgewehrteElfmeter.csv"
out_f = "1.csv"

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




# the file names
f1 = "1.csv"
f2 = "abgewehrteSchuesse.csv"
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




# the file names
f1 = "2.csv"
f2 = "balleroberungen.csv"
out_f = "3.csv"

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




# the file names
f1 = "3.csv"
f2 = "ballverluste.csv"
out_f = "4.csv"

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




# the file names
f1 = "4.csv"
f2 = "begangeneFouls.csv"
out_f = "5.csv"

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





# the file names
f1 = "5.csv"
f2 = "cleanSheet.csv"
out_f = "6.csv"

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





# the file names
f1 = "6.csv"
f2 = "erfolgreicheDribblings.csv"
out_f = "7.csv"

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






# the file names
f1 = "7.csv"
f2 = "error.csv"
out_f = "8.csv"

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






# the file names
f1 = "8.csv"
f2 = "flanken.csv"
out_f = "9.csv"

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






# the file names
f1 = "9.csv"
f2 = "geblockteBaelle.csv"
out_f = "10.csv"

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






# the file names
f1 = "10.csv"
f2 = "geklaerteBaelle.csv"
out_f = "11.csv"

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






# the file names
f1 = "11.csv"
f2 = "grosschancenKreiert.csv"
out_f = "12.csv"

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







# the file names
f1 = "12.csv"
f2 = "grosschancenPariert.csv"
out_f = "13.csv"

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







# the file names
f1 = "13.csv"
f2 = "luftkampf.csv"
out_f = "14.csv"

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







# the file names
f1 = "14.csv"
f2 = "paraden.csv"
out_f = "15.csv"

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





# the file names
f1 = "15.csv"
f2 = "passquote.csv"
out_f = "16.csv"

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





# the file names
f1 = "16.csv"
f2 = "schussgenauigkeit.csv"
out_f = "17.csv"

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




# the file names
f1 = "17.csv"
f2 = "shotOnTarget.csv"
out_f = "18.csv"

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




# the file names
f1 = "18.csv"
f2 = "tackling.csv"
out_f = "19.csv"

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




# the file names
f1 = "19.csv"
f2 = "torschussvorlagen.csv"
out_f = "20.csv"

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




# the file names
f1 = "20.csv"
f2 = "transfermarkt.csv"
out_f = "21.csv"

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




# the file names
f1 = "21.csv"
f2 = "zweikampf.csv"
out_f = "22.csv"

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


os.remove('1.csv')
os.remove('2.csv')
os.remove('3.csv')
os.remove('4.csv')
os.remove('5.csv')
os.remove('6.csv')
os.remove('7.csv')
os.remove('8.csv')
os.remove('9.csv')
os.remove('10.csv')
os.remove('11.csv')
os.remove('12.csv')
os.remove('13.csv')
os.remove('14.csv')
os.remove('15.csv')
os.remove('16.csv')
os.remove('17.csv')
os.remove('18.csv')
os.remove('19.csv')
os.remove('20.csv')
os.remove('21.csv')


# READ BOTH FILES AS TABULAR DATA STRUCTURE
# PROVIDE FILE PATH
csv_file = pd.read_csv("22.csv")

# REPLACE EMPTY VALUES WITH NULL IN CSV ONE
csv_file.fillna(value='NULL', inplace=True)
csv_file.to_csv("FINAL.csv", index=False)

