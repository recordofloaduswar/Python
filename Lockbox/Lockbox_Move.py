import os
import glob
import shutil

list_of_files = glob.glob('Z:\\Folder_1\\Lockbox\\*') # * means all if need specific format then *.csv
latest_folder = max(list_of_files, key=os.path.getctime)

shutil.copy('Z:\\Folder_1\\Lockbox\\Lockbox_File_Prep.py', latest_folder)