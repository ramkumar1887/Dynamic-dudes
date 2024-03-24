import sqlite3
import qrcode
import webbrowser
from io import BytesIO

# Function to get user info from the database
def get_user_info(username):
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Query the database to fetch user information
    cursor.execute('''SELECT first_name, last_name, phone_number FROM users WHERE username = ?''', (username,))
    user_info = cursor.fetchone()

    conn.close()

    return user_info

# Function to generate QR code and save it to a file
def generate_and_save_qr(order_id, username):
    # Generate HTML content for order details
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Order Details</title>
        </head>
        <body>
            <h1>Order Details</h1>
            <p>Order ID: {order_id}</p>
            <p>Username: {username}</p>
            <form>
                <label for="phone_number">Enter your phone number:</label><br>
                <input type="text" id="phone_number" name="phone_number" required><br><br>
                <button type="submit">Request Call</button>
            </form>
        </body>
        </html>
        """

    # Save HTML content to a file
    with open(f"order_details.html", "w") as f:
        f.write(html_content)

    # Construct the data to be encoded in the QR code
    qr_data = f"Order ID: {order_id}\nUsername: {username}"

    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(f"{order_id}_qr.png")

if __name__ == '__main__':
    # Example usage:
    order_id = "12345"
    username = "example_user"
    generate_and_save_qr(order_id, username)
