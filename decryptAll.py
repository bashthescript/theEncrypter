import base64, os
from simplecrypt import decrypt

key = "password"

routeToDecode = 'C:\\Users\\mattw\\Desktop\\Python\\Pictures\\toDecode\\'
routeDecodedImages = 'C:\\Users\\mattw\\Desktop\\Python\\Pictures\\decodedImages\\'

for file in os.listdir(routeToDecode):
    if file.endswith(".enc"):
        with open(routeToDecode + file, 'rb') as text_file:
            ciphertext = text_file.read()
        dec = decrypt(key, ciphertext)
        with open(routeDecodedImages + file + ".jpg", 'wb') as picture:
            picture.write(base64.standard_b64decode(dec))