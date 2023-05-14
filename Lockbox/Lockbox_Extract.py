import zipfile
import glob
import gnupg
import os

files = glob.glob('Z:\\Folder_1\\Downloads\\*.zip.gpg')
last_file = max(files)

gpg = gnupg.GPG(gnupghome = 'C:\\gpgFolder\\GNuPG')

imported_keys = gpg.import_keys_file('C:\\keysFolder\\secret_key.asc')

public_keys = gpg.list_keys()
private_keys = gpg.list_keys(True)

with open (last_file, 'rb') as f:
    decrypted = f.name
    suffix = '.zip'
    new_decrypt = decrypted[:decrypted.rindex(suffix) + len(suffix)]
    status = gpg.decrypt_file(f, passphrase = 'passphrase', output = new_decrypt)

with zipfile.ZipFile(new_decrypt, mode = 'r') as archive:
    archive.extractall('Z:\\Folder_1\\Lockbox')

print(status.ok)
print(status.stderr)