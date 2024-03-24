import qrcode

order_id = 'order_id'
username = 'username123'

# Construct the data to be encoded in the QR code
qr_data = f"Order ID: {order_id}\nUsername: {username}"

# Generate the QR code
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(qr_data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
filename = f"qr_{order_id}_{username}.png"
img.save(filename)