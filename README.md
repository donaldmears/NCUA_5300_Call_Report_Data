# NCUA_5300_Call_Report_Data
Python code to pull National Credit Union Administration (NCUA) 5300 Call Report Data. This will allow you to gather multiple quarters for trending purposes or for use in exploratory data analysis or an ML model.
________________________________________________________________________________
There are two py files:

• **callreportdata.py** pulls the data files from the NCUA website, selects key fields from various tables, and consolidates them into one csv file for all Credit Unions for a particular quarter

• **concat_call_reports.py** concatenates all of the quarterly csv files produced by the callreportdata.py code into a single csv file 

There are also two Jupyter Notebook files:

• **callreport.ipynb** Jupyter Notebook file containing code from both **callreportdata.py** and **concat_call_reports.py**

• **concat_callreport_with_avg_assets.ipynb** Jupyter Notebook file containing updated code from **concat_call_reports.py** that also includes a calculated field for average assets which is used in various metrics such as Return on Assets (ROA)

________________________________________________________________________________

It will be necessary for you to change the directory / path and quarter variables

Features in the data set include the following (and others can be added if you modify the code):
|Column |
|-------|
|CU_NUMBER|
CYCLE_DATE
JOIN_NUMBER
CU_NAME
CITY
STATE
TOTAL ASSETS (ACCT_010)
Total Amount of Shares (ACCT_013)
Total number of Loans and Leases (ACCT_025A)
Total amount of Loans and Leases (ACCT_025B)
Amount of Loans Granted Year-to-Date (ACCT_031B)
Total Amount of Delinquent Loans & Leases (Two or more months) (ACCT_041B)
Number of current members (not number of accounts) (ACCT_083)
Provision for Loan & Lease Losses (ACCT_300)
Interest on Borrowed Money (ACCT_340)
Dividends on Shares (Includes dividends earned during current period) (ACCT_380)
Non-Member Deposits (ACCT_457)
Interest Rate of New Vehicle Loans (ACCT_523)
Interest Rate of Used Vehicle Loans (ACCT_524)
Total Amount of All Loans Charged Off Year-to-Date (ACCT_550)
Net Income (unless the amount is already included in Undivided Earnings) (ACCT_602)
Amount of Regular Shares (ACCT_657)
Total Non-Interest Expense (Sum of items 18-27) (ACCT_671)
Total Borrowings (ACCT_860C)
Number of Used Vehicle Loans (ACCT_968)
(Less) Interest Refunded (ACCT_119)
Fee Income (ACCT_131)
Employee Compensation and Benefits (ACCT_210)
Travel and Conference Expense (ACCT_230)
Office Occupancy Expense (ACCT_250)
Office Operations Expense (ACCT_260)
Educational and Promotional Expense (ACCT_270)
Loan Servicing Expense (ACCT_280)
Professional and Outside Services (ACCT_290)
Member Insurance (ACCT_310)
Operating Fees (Examination and/or supervision fees) (ACCT_320)
Miscellaneous Operating Expenses (ACCT_360)
Amount of Used Vehicle Loans (ACCT_370)
Interest on Deposits (Total interest expense for deposit accounts) (SCU Only) (ACCT_381)
Amount of New Vehicle Loans (ACCT_385)
Amount of Unsecured Credit Card Loans (ACCT_396)
Amount of All Other Unsecured Loans/Lines of Credit (ACCT_397)
Number of Accounts for Share Drafts (ACCT_452)
IRA/KEOGH Accounts (ACCT_453)
Number of Accounts for Regular Shares (ACCT_454)
All other shares (ACCT_455)
Money Market Shares (ACCT_458)
Number of Accounts for Total Shares and Deposits (Sum of items 15-16) (ACCT_460)
Total Interest Income (ACCT_115)
Total Non-Interest Income (ACCT_117)
Total Interest Expense (Sum of items 6-8) (ACCT_350)
Net Income (Loss) (line 11 plus line 17 less line 28) (ACCT_661A)
Average of Daily Assets over the calendar quarter (ACCT_010A)
Cash on Hand (Coin and Currency) (ACCT_730A)
Total Cash on Deposit (Amounts Deposited in Financial Institutions) (ACCT_730B)
Total Net Worth (ACCT_997)
Net Worth Ratio (ACCT_998)
Number of Outstanding Indirect Loans (ACCT_617A)
Total Amount of Outstanding Indirect Loans (ACCT_618A)
Total Shares (ACCT_966)
Total Uninsured Member Shares and Deposits > $250K (A+A1+B+C+D+E) (ACCT_065A4)
Total Uninsured Nonmember Shares and Deposits > $250K (G+H+I) (ACCT_067A2)
Total Uninsured Shares and Deposits > $250K (F+J) (ACCT_068A)
Total Insured Shares and Deposits > $250K (item 17 less item K) (ACCT_069A)
Amount of Participation Loans Purchased Year-to-Date (ACCT_690)
Amount of Participation Loans Sold Year-to-Date (ACCT_691)
Cash on Deposit in Corporate Credit Unions (ACCT_730B1)
Cash on Deposit in Other Financial Institutions (ACCT_730B2)
Net Worth Classification if credit union is not new (Based upon Call Report data only. See instructions) (ACCT_700)
Equity Acquired in Merger (ACCT_658A)
Total Outstanding Amount of Participation Loans Purchased By Type (ACCT_691L)
Total Value of Investments in CUSOs (ACCT_851)
Total Amount Loaned to CUSOs (ACCT_852)
Total Aggregate Cash Outlay in CUSOs (ACCT_853)
Amount of Payday Alternative Loans (PAL loans) (ACCT_397A)
Amount of Total Loans/Lines of Credit Secured by Junior Lien 1-4 Family Residential Properties (ACCT_386A)
Amount of All Other Real Estate Loans/Lines of Credit (ACCT_386B)
Cash on Deposit in the Federal Reserve Bank (ACCT_AS0003)
Coin and Currency (ACCT_AS0004)
Cash Items in Process of Collection (ACCT_AS0005)
(CECL) indicator for early adoption of CECL (ACCT_AS0010)
Time deposits in commercial banks, S&Ls, savings banks, natural person credit unions, or corporate credit unions (ACCT_AS0007)
All other deposits (ACCT_AS0008)
Total Cash and Other Deposits (ACCT_AS0009)
Total Investment Securities (ACCT_AS0013)
All other investments (ACCT_AS0016)
Total Other Investments (ACCT_AS0017)
Total Other Assets (ACCT_AS0036)
Unsecured Credit Card Loans  (ACCT_DL0002)
New Vehicle Loans  (ACCT_DL0030)
Used Vehicle Loans (ACCT_DL0037)
