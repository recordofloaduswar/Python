# Python
Scripts and small projects of the Python variety that I actively use to automate tasks.

## [Lockbox File Management](https://github.com/recordofloaduswar/Python/tree/main/Lockbox):bank:
These scripts are used to organize file images received from a bank lockbox. The bank sends a folder with TIFF images and an index file. The index file indicates which images are part of the same transaction. In this case, each transaction contains an image of a check and any accompanying documents (i.e. appeals, notes, check stubs). Using Windows Task Scheduler, I have the files programmed to run automatically at night to get the files prepared for the staff the next morning. The files run in the order below.
- Lockbox_Extract: This script decrypts the file transferred from the bank and extracts the files from the zip file to a folder.
- Lockbox_Move: Moves the Lockbox_File_Prep file to the same folder as the extracted files. In this case, it will be the latest folder created.
- Lockbox_Rename: Renames the latest folder created.
- Lockbox_Run_Merge: This script runs the Lockbox_File_Prep script.
- Lockbox_File_Prep: Prepares the lockbox images by doing the following:
  - Creates a timestamped folder
  - Reads the index file
  - Concatenates the respective images together into one JPEG file (converted from TIFF images)
  - Names the file according to check number and check amount
  - Saves the file into the timestamped folder
  - Repeats the process until it has looped through the index file

## [Credit Card Recon](https://github.com/recordofloaduswar/Python/blob/71c79994eb5f2875133a8586b12633933fe6a1b2/Automation/Credit_Card_Recon.py):moneybag:
I use this file to determine if any sucessful credit card transactions processed through our online giving site are missing from our CRM. It is basically an inner join of a report from our CRM to a report from our payment processor. Each row is a transaction. The inner join returns the transactions that are missing from the CRM report.
