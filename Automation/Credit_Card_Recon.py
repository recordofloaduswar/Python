import pandas as pd

# read CSV files
CRM_report = pd.read_csv('CRM.csv')
Payment_report = pd.read_csv('Payments.csv')

#Rename column in payment processor file to set a key
Payment_report = Payment_report.rename(columns={'Merchant Reference Number':'External Payment Gateway ID'})

#Join files based on the key, return rows from CyberSource that appear in the CRM
inner_join = pd.merge(Payment_report, CRM_report, on = 'External Payment Gateway ID', how = 'inner')

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
