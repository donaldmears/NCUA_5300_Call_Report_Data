# -*- coding: utf-8 -*-
"""
@author: donald
"""

import pandas as pd
import glob

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# read in AcctDesc.txt file
acct_desc = pd.read_csv('AcctDesc.txt')

# convert 'Account' column to upper case
acct_desc['Account'] = acct_desc['Account'].str.upper()

# get data file names
path = r'C:\Users\donald\Desktop\Python\callreport' 
filenames = glob.glob(path + "/*.xlsx")

dfs = [] # an empty list to store the dataframes

for filename in filenames:
    df = pd.read_excel(filename) # read excel file
    dfs.append(df) # append to list

# concatenate all dataframes in the list
big_df = pd.concat(dfs, ignore_index=True)

# convert column names to upper case
big_df.columns = big_df.columns.str.upper()

# modify column names
new_col_names = {}
for col in big_df.columns:
    if col != 'ACCOUNT': # skip the 'Account' column
        # get the corresponding account name from the AcctDesc.txt file
        try:
            acct_name = acct_desc[acct_desc['Account'] == col]['AcctName'].values[0]
        except IndexError:
            # handle index error if the account does not exist in AcctDesc.txt
            print(f"Warning: Account {col} does not exist in AcctDesc.txt")
            continue
        # blend the account name with the existing column name
        new_col_name = f"{acct_name} ({col})"
        new_col_names[col] = new_col_name

big_df.rename(columns=new_col_names, inplace=True)

# save the modified dataframe to csv
big_df.to_csv(r'C:\Users\donald\Desktop\Python\callreport\data\master_call_report_data.csv', index=False)

acct_desc.head()