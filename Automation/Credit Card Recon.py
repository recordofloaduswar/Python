import pandas as pd

# read CSV files
CRM_Pre = pd.read_csv('CRM.csv')
CyberSource_Pre = pd.read_csv('CyberSource.csv')

#Rename column in CyberSource file to set a key
CyberSource_Pre = CyberSource_Pre.rename(columns={'Merchant Reference Number':'External Payment Gateway ID'})

#Join files based on the key, return rows from CyberSource that appear in the CRM
inner_join = pd.merge(CyberSource_Pre, CRM_Pre, on = 'External Payment Gateway ID', how = 'inner')

#Delete rows containing 'Fail' or 'Reversal' in the 'Applications' column
inner_join = inner_join[~inner_join.Applications.str.contains("Fail")]
inner_join = inner_join[~inner_join.Applications.str.contains("Reversal")]

#Select columns to display
inner_join = inner_join[['Date and Time', 'External Payment Gateway ID', 'Last Name', 'First Name', 'Email',
                         'Amount', 'Currency', 'Applications', 'Payment Method', 'Transaction Reference Number',
                         'Authorization Code', 'Billing Address1', 'Billing City', 'Billing State', 'Billing Postal Code',
                         'Billing Country', 'Appeal']]

#Save csv file to drive
inner_join.to_csv('Drive:\File_Name.csv')

print(inner_join)
