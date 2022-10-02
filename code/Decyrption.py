# using the key
from cryptography.fernet import Fernet
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
fernet = Fernet(key)
 
# opening the encrypted file
with open('nba.csv', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('nba.csv', 'wb') as dec_file:
    dec_file.write(decrypted)