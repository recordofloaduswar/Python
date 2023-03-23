# Python
Scripts and small projects of the Python variety that I actively use to automate tasks.

## [Lockbox File Prep](https://github.com/recordofloaduswar/Python/blob/b483ba29d0496e416936988195b3a3bd2f6ecd2d/Automation/Lockbox_File_Prep.py):bank:
These scripts are used to organize file images received from a bank lockbox. The bank sends a folder with TIFF images and an index file. The index file indicates which images are part of the same transaction. In this case, each transaction contains an image of a check and any accompanying documents (i.e. appeals, notes, check stubs). After running the Python script in the same folder as the images and index file, the script does the following:
- Creates a timestamped folder
- Reads the index file
- Concatenates the respective images together into one TIFF file
- Names the file according to check number and check amount
- Saves the file into the timestamped folder
- Repeats the process until it has looped through the index file

## [Credit Card Recon](https://github.com/recordofloaduswar/Python/blob/71c79994eb5f2875133a8586b12633933fe6a1b2/Automation/Credit_Card_Recon.py):moneybag:
I use this file to determine if any sucessful credit card transactions processed through our online giving site are missing from our CRM. It is basically an inner join of a report from our CRM to a report from our payment processor. Each row is a transaction. The inner join returns the transactions that are missing from the CRM report.
