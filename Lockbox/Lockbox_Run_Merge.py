import os

root = os.getcwd()

for d in ['Z:\\Folder_1\\Lockbox\\Lockbox_Files']:
    os.chdir(os.path.join(root, d))
    print('dir:', os.getcwd())
    exec(open('Z:\\Folder_1\\Lockbox\\Lockbox_Files\\Lockbox_File_Prep.py').read())