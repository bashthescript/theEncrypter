import base64, os
from simplecrypt import encrypt

key = "password"

routeToEncode = 'C:\\Users\\mattw\\Desktop\\Python\\Pictures\\toEncode\\'
routeToDecode = 'C:\\Users\\mattw\\Desktop\\Python\\Pictures\\toDecode\\'

for file in os.listdir(routeToEncode):
    if file.endswith(".jpg"):
        with open(routeToEncode + file, "rb") as image_file:
            encodedImageText = base64.standard_b64encode(image_file.read())
        enc = encrypt(key, encodedImageText)
        with open(routeToDecode + file + ".enc", 'wb') as fo:
            fo.write(enc)
