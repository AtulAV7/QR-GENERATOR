import qrcode 


from PIL import Image


import qrcode.constants

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=15,border=5)
qr.add_data("")#Give the link that you want to convert to qrcode form within the " "
qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="black")
img.save("")