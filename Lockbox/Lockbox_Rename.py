import os
import glob
import time
import shutil

list_of_files = glob.glob('Z:\\Folder_1\\Lockbox\\*') # * means all if need specific format then *.csv
latest_folder = max(list_of_files, key=os.path.getctime)

date = time.strftime('%m.%d.%Y')

os.rename(latest_folder, 'Z:\\Folder_1\\Lockbox\\Lockbox_Files')