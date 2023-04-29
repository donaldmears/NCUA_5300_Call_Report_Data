# -*- coding: utf-8 -*-
"""
@author: donald
"""

import pandas as pd
import zipfile
import urllib.request
import os

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


os.chdir("C:\\Users\\donald\\Desktop\\Python\\callreport")

# Download the ZIP file from the NCUA website - change quarter to yyyy-03 or 06 or 09 or 12
quarter = '2022-12' #YYYY-MM representing the quarter - MM is 03, 06, 09, or 12
url = 'https://ncua.gov/files/publications/analysis/call-report-data-'+quarter+'.zip'
filename = quarter+'.zip'
urllib.request.urlretrieve(url, filename)

# Extract the contents of the ZIP file
with zipfile.ZipFile(filename, 'r') as zip_ref:
    zip_ref.extractall()

# Read the CSV files into dataframes
df_Acctdesc = pd.read_csv('AcctDesc.txt')
df_branches = pd.read_csv('Credit Union Branch Information.txt')
df_fs220 = pd.read_csv('FS220.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER', 'ACCT_010', 'ACCT_013', 'ACCT_025A', 'ACCT_031B', 'ACCT_041B', 'ACCT_083', 'ACCT_300', 'ACCT_340', 'ACCT_380', 'ACCT_457', 'ACCT_523', 'ACCT_524', 'ACCT_550', 'ACCT_602', 'ACCT_657', 'ACCT_671', 'ACCT_860C', 'ACCT_968', 'ACCT_025B'])
df_fs220a = pd.read_csv('FS220A.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER', 'Acct_010A', 'ACCT_115', 'ACCT_117', 'ACCT_119', 'ACCT_131', 'ACCT_210', 'ACCT_230', 'ACCT_250', 'ACCT_260', 'ACCT_270', 'ACCT_280', 'ACCT_290', 'ACCT_310', 'ACCT_320', 'ACCT_350', 'ACCT_360', 'ACCT_370', 'ACCT_381', 'ACCT_385', 'ACCT_396', 'ACCT_397', 'ACCT_452', 'ACCT_453', 'ACCT_454', 'ACCT_455', 'ACCT_458', 'ACCT_460', 'ACCT_617A', 'ACCT_618A', 'Acct_661A', 'Acct_730A', 'Acct_730B', 'Acct_997', 'Acct_998'])
df_fs220b = pd.read_csv('FS220B.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER', 'ACCT_065A4', 'ACCT_067A2', 'ACCT_068A', 'ACCT_069A', 'ACCT_966'])
df_fs220c = pd.read_csv('FS220C.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER', 'ACCT_690', 'ACCT_691', 'ACCT_730B1', 'ACCT_730B2'])
df_fs220d = pd.read_csv('FS220D.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER', 'Acct_700'])
df_fs220g = pd.read_csv('FS220G.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER','ACCT_658A', 'ACCT_691L', 'ACCT_851', 'ACCT_852', 'ACCT_853'])
df_fs220h = pd.read_csv('FS220H.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER','Acct_397A'])
df_fs220l = pd.read_csv('FS220L.txt', usecols=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER','ACCT_386A', 'ACCT_386B'])
df_fs220n = pd.read_csv('FS220N.txt', usecols=['CU_Number', 'CYCLE_DATE', 'JOIN_NUMBER','ACCT_AS0003', 'ACCT_AS0004', 'ACCT_AS0005', 'ACCT_AS0010'])
df_fs220n = df_fs220n.rename(columns={'CU_Number':'CU_NUMBER'})
df_fs220p = pd.read_csv('FS220P.txt', usecols=['CU_NUMBER', 'Cycle_date','join_number','ACCT_AS0007', 'ACCT_AS0008', 'ACCT_AS0009', 'ACCT_AS0013', 'ACCT_AS0016', 'ACCT_AS0017', 'ACCT_AS0036', 'ACCT_DL0002', 'ACCT_DL0030', 'ACCT_DL0037'])
df_fs220p = df_fs220p.rename(columns={'Cycle_date':'CYCLE_DATE', 'join_number':'JOIN_NUMBER'})
df_FOICU = pd.read_csv('FOICU.txt', usecols=['CU_NUMBER','CYCLE_DATE','JOIN_NUMBER','CU_NAME', 'CITY','STATE'])

dfs = [df_FOICU, df_fs220, df_fs220a, df_fs220b, df_fs220c, df_fs220d, df_fs220g, df_fs220h, df_fs220l, df_fs220n, df_fs220p]


# join the dataframes on cu_number, cycle_date, and join_number
merged_df = pd.merge(dfs[0], dfs[1], on=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER'], how='outer')
for i in range(2, len(dfs)):
    merged_df = pd.merge(merged_df, dfs[i], on=['CU_NUMBER', 'CYCLE_DATE', 'JOIN_NUMBER'], how='outer')


merged_df.to_excel(quarter + '.xlsx')