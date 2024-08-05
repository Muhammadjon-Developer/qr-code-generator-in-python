import qrcode  # download this (how: pip install qrcode)
import image   # download this (how: pip install image)

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

data = input("Enter any URL or Link: ")

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")
