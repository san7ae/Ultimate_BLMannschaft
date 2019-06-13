import pandas as pd

# READ BOTH FILES AS TABULAR DATA STRUCTURE
# PROVIDE FILE PATH
csv_file = pd.read_csv("merge23.csv")

# REPLACE EMPTY VALUES WITH NULL IN CSV ONE
csv_file.fillna(value='NULL', inplace=True)
csv_file.to_csv("mergeFinal.csv", index=False)
