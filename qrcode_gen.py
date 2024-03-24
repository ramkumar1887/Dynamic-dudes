import sqlite3
from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for
import qrcode
from io import BytesIO

app = Flask(__name__)

# Function to get user info from the database
def get_user_info(username):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Query the database to fetch user information
    cursor.execute('''SELECT first_name, last_name, phone_number FROM users WHERE username = ?''', (username,))
    user_info = cursor.fetchone()

    conn.close()

    return user_info

# Receiver function to generate QR code and return the image
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Get data sent by the client-side
    data = request.json
    order_id = data.get('order_id')
    username = data.get('username')

    # Get user information from the database
    user_info = get_user_info(username)
    if user_info:
        first_name, last_name, user_phone = user_info
    else:
        first_name, last_name, user_phone = None, None, None

    # Construct the data to be encoded in the QR code
    qr_data = f"Order ID: {order_id}\nUsername: {username}\nFirst Name: {first_name}\nLast Name: {last_name}"

    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    img_buffer.seek(0)

    # Redirect to the order details page
    return redirect(url_for('order_details', order_id=order_id, username=username, user_phone=user_phone))

@app.route('/order_details', methods=['GET', 'POST'])
def order_details():
    if request.method == 'POST':
        # Handle the form submission (HTTP request for call)
        order_id = request.form['order_id']
        username = request.form['username']
        phone_number = request.form['phone_number']
        user_phone = request.form['user_phone']

        # Perform HTTP request for call using the provided phone number and user's phone number

        return "Request for call has been sent!"

    else:
        # Render the order details page with QR code data
        order_id = request.args.get('order_id')
        username = request.args.get('username')
        user_phone = request.args.get('user_phone')
        return render_template('order_details.html', order_id=order_id, username=username, user_phone=user_phone)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
