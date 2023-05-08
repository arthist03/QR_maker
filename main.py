import qrcode as qr
from PIL import Image
from urllib.parse import urlparse

# Get input link from user
input_link = input("Enter a link: ")

# Extract website name from input link
parsed_url = urlparse(input_link)
website_name = parsed_url.netloc.split('.')[1]

# Create QR code with input link
qr_code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr_code.add_data(input_link)
qr_code.make(fit=True)

# Create QR code image and save as PNG file with website name
img = qr_code.make_image(fill_color="black", back_color="white")
img.save(website_name + ".png")

print("QR code saved as " + website_name + ".png")
